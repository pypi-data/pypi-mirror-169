#
# The MIT License (MIT)
# Copyright (c) 2022 M.O.S.S. Computer Grafik Systeme GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT,TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import copy
import json
import logging
from pathlib import Path
from typing import List, Optional

from moss.ems.emslayer import EmsLayer
from moss.ems.emsproject import EmsProject
from moss.ems.emsservice import EmsServiceException, Service

logger = logging.getLogger(__name__)


try:
    from osgeo import gdal
except ImportError:
    logger.error("This function needs GDAL Python bindings.")
    raise ImportError("No GDAL Provided")


class EmsCliDumpException(Exception):
    pass


class EmsCliDump:
    """ """

    def __init__(
        self,
        url: str,
        project: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        token: Optional[str] = None,
    ):

        if username and password:
            logger.debug("Logging in using username and password.")
            try:
                self.service = Service(url, username=username, password=password)
            except EmsServiceException:
                logger.error("Can not connect to service using username and password.")
                raise EmsCliDumpException
        elif token:
            logger.debug("Logging in using token.")
            try:
                self.service = Service(url, token=token)
            except EmsServiceException:
                logger.error("Can not connect to service using token.")
                raise EmsCliDumpException
        else:
            logger.debug("Using service without authentication.")
            try:
                self.service = Service(url)
            except EmsServiceException:
                logger.error("Can not access WEGA-EMS Service using no authentication.")

        logger.debug("Accessing project %s", project)
        try:
            selected_project = self.service.project(project)
            if selected_project is not None:
                self.project: EmsProject = selected_project
            else:
                logger.error("The selected project %s is not defined", project)
                raise EmsCliDumpException
        except EmsServiceException:
            logger.error("The project %s does not exists in %s", project, url)
            raise EmsCliDumpException

    def _project_has_variant(self):
        """
        Check if project has variants
        """
        return self.project.variants_tree()  # Empty dict are False

    def ems_dump(
        self,
        output_path: str,
        variant_master_name: Optional[str] = None,
        variant_master_id: Optional[str] = None,
        objectclasses: Optional[str] = None,
        variants: Optional[str] = None,
        extension: str = "gpkg",
        output_filename: str = "variant",
    ):
        logger.info("Starting dump..")
        if variant_master_id is not None or variant_master_name is not None:
            logger.info("Starting dump using variants.")
            logger.info(
                "Variant master name: %s - Variant master id: %s ",
                variant_master_name,
                variant_master_id,
            )

        if variant_master_id and variant_master_name:
            logger.error("Please provide master name or the id, not booth.")
            raise EmsCliDumpException

        if not Path(output_path).exists():
            raise EmsCliDumpException("The output path %s not exists.", output_path)

        variants_tree, _ = self.project.variants_tree()

        selected_variant = {}

        try:
            variants_list = variants_tree["children"]
        except KeyError:
            logger.error("Error parsing variant Tree")
            raise EmsCliDumpException

        if variant_master_name:
            selected_variant = next(
                variant
                for variant in variants_list
                if variant["variant_name"] == variant_master_name
            )
            logger.debug(
                "Found this variant using name %s as selection: %s",
                variant_master_name,
                selected_variant,
            )

        if variant_master_id:
            selected_variant = next(
                variant
                for variant in variants_list
                if variant["id"] == int(variant_master_id)
            )
            logger.debug(
                "Found this variant using id %s as selection: %s",
                variant_master_id,
                selected_variant,
            )

        if selected_variant is None:
            logger.error("The selected variant can not be found.")
            raise EmsCliDumpException

        logger.info(
            "Starting export all the sub-variants inside %s",
            output_path,
        )

        exported_variants = []
        if variants is not None:
            exported_variants = variants.split(",")
        else:
            exported_variants = selected_variant["children"]

        for variant in exported_variants:

            try:
                variant_id = variant["id"]
            except TypeError:
                variant_id = int(variant)
                if variant_id == int(variant_master_id):
                    continue

            logger.info("Current variant id %s", variant_id)

            variant_geopackage = "{0}-{1}.{2}".format(
                output_filename, variant_id, extension
            )
            variant_geopackage_path = Path(output_path) / variant_geopackage

            export_objectclasses = []
            if objectclasses is not None:
                export_objectclasses = objectclasses.split(",")
            else:
                export_objectclasses = self.project.objectclasses

            for objectclass in export_objectclasses:
                logger.info("Processing objectclass %s", objectclass)

                if isinstance(objectclass, str):
                    objectclass = self.project.objectclass(objectclass)

                layers: Optional[List[EmsLayer]] = objectclass.layers
                if layers is not None:

                    for layer in layers:
                        logger.debug("Processing layer %s", layer)

                        layer_query = layer.query(
                            where="1=1", returnGeometry=True, variants=[variant_id]
                        )
                        if layer_query:
                            query_output = layer_query.resolve(with_catalog=True)

                            total_features = []
                            final_esri = {}

                            for query_index, query_item in enumerate(query_output):
                                if query_index == 0:
                                    final_esri = copy.deepcopy(query_item)

                                features = query_item.get("features")
                                if features is not None:
                                    total_features.extend(features)

                            cleaned_features = list(
                                filter(lambda item: "geometry" in item, total_features)
                            )

                            if cleaned_features:
                                final_esri["features"] = cleaned_features
                                final_esri["counts"] = len(cleaned_features)

                                temp_layer = "temp-{0}-{1}.json".format(
                                    objectclass, layer
                                )
                                temp_layer_path = Path(output_path) / temp_layer
                                temp_layer_name = temp_layer.split(".")[0]

                                with open(temp_layer_path, "w+") as esri_json:
                                    esri_json.write(json.dumps(final_esri))

                                if extension == "csv":
                                    csvpackage = "{0}.{1}".format(str(layer), extension)
                                    variant_dirname = "{0}-{1}".format(
                                        output_filename, variant_id
                                    )
                                    variant_path = Path(output_path) / Path(
                                        variant_dirname
                                    )
                                    variant_path.mkdir(parents=True, exist_ok=True)
                                    variant_geopackage_path = variant_path / csvpackage

                                logger.info(
                                    "Exporting current variant in %s",
                                    variant_geopackage_path,
                                )

                                if not variant_geopackage_path.exists():
                                    gdal.VectorTranslate(
                                        str(variant_geopackage_path),
                                        str(temp_layer_path),
                                        layerName=temp_layer_name,
                                    )
                                else:
                                    gdal.VectorTranslate(
                                        str(variant_geopackage_path),
                                        str(temp_layer_path),
                                        layerName=temp_layer_name,
                                        accessMode="update",
                                    )

                                temp_layer_path.unlink()

        logger.info("Closing the communication with WEGA-EMS")
        self.service.close()
