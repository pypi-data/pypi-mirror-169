# -*- coding: UTF-8 -*-
# pylint: disable=C0103
# pylint: disable=C0410
# pylint: disable=C0301
# pylint: disable=C0200
#---------------------------------------------------------------------
# Copyright (c) 2019  by M.O.S.S. Computer Grafik Systeme GmbH
#                        Hohenbrunner Weg 13
#                        D-82024 Taufkirchen
#                        http://www.moss.de
#---------------------------------------------------------------------
# Windows:
# set HTTPS_PROXY=proxy2.muc.moss.itn:3128
# set HTTP_PROXY=proxy2.muc.moss.itn:3128
# oder %APPDATA%\pip\pip.ini
#
# pip install requests
# pip install argparse
#---------------------------------------------------------------------
# python U:\wega-ems\trunk\emsImpExp\src\main\python\emsExporter.py ^
# -u "http://wega-ems.muc.moss.itn:8080/ems/rest/wegaems_prj02""
# -c "b7ps04,b7ps03"
# -outSrs 25832
# -o C:\Users\suhlig\ownCloud\Projekte\EMS_Importer\_Testdaten_Ostwind_SHP\Test\Ergebnisse
# -l exportLog.log

"""
Exportieren von Feature-Daten im Format GeoJSON aus EMS via REST-Schnittstelle.
Erzeugt im Ausgabeverzeichnis fuer jede Objektklasse ein Unterverzeichnis, in dem fuer jeden Layer eine json-Datei
mit den Exportdaten abgelegt wird.
"""

import sys, traceback
import argparse, logging

VERSION = "1.0.6"
PROGNAME = "emsExport"

class ProjectError(Exception):
    """ Fehler beim Laden Objektklassen """
    def __init__(self):
        Exception.__init__(self, "ERROR - Objektklassen zum Projekt konnten nicht gelesen werden. Die angegeben Projekt-URL ist vermutlich nicht vorhanden!\n")
     
try:

    # init logging
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(levelname)s- %(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


    # READ PARAMS 
    parser = argparse.ArgumentParser(prog=PROGNAME)

    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-c', '--objectClasses', action="store", dest="inObjectClasses", help='Zu exportierende Objektklassen (..,..,..)', required=True)
    requiredNamed.add_argument('-outSrs', '--outSrs', action="store", dest="outSrs", help='Export-EPSG-Code', required=True, type=int)
    requiredNamed.add_argument('-u', '--url', action="store", dest="url", help='URL zum REST-Projekt', required=True)

    parser.add_argument('-l', '--logFile', action="store", dest="logFile", help='Pfad zum LogFile (optional)', default="")
    parser.add_argument('-log', '--logLevel', action="store", dest="logLevel", help='Loglevel: INFO,DEBUG,ERROR (optional)', default="INFO")
    parser.add_argument('-o', '--outPath', action="store", dest="outPath", help='Ergebnis-Ablageverzeichnis', default="")
    parser.add_argument('-t', '--token', action="store", dest="token", help='Authentifizierungs-Token', default="")
    parser.add_argument('-v', '--variant', action="store", dest="variant", help='Variantenliste (VarID,..,...)', default="")
    parser.add_argument('-vm', '--variantMaster', action="store", dest="master", help='Windpark-ID)', default="")
    parser.add_argument('--version', action='version', version='%(prog)s '+VERSION)
    parser.add_argument('-geb', '--gebiet', action="store", dest="gebiet", help='Exportgebiet', nargs='?', default="")
    results = parser.parse_args()

    if results.logLevel.upper() == "INFO": 
        logger.setLevel(logging.INFO)
    elif results.logLevel.upper() == "DEBUG": 
        logger.setLevel(logging.DEBUG)
    elif results.logLevel.upper() == "ERROR": 
        logger.setLevel(logging.ERROR)

    if results.logFile != "":
        logFile = results.logFile
        handler.setLevel(logging.ERROR)
        handler = logging.FileHandler(logFile, 'a', encoding='UTF-8')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info('*********    START EMS-EXPORTER    *********')
        logger.info('Logfile: %s', logFile)

##############################################################################################################
    from ems_cli_dump import EmsCliDump
    logger.info(results)
    
    initial=EmsCliDump(
        results.url,
        "wegaems_prj20",
        "Erfassung",
        "Erfassung",
        results.token
        )

    dumping=initial.ems_dump(
            results.inObjectClasses,
            results.outPath,
            results.variant,
            "csv",
            results.gebiet,
            results.outSrs,
            results.master,
            )

############################################################################################

except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    logger.error(pymsg)
    sys.exit(1)

else:
    logger.info("Exitstatus:0\n")
    sys.exit(0)

