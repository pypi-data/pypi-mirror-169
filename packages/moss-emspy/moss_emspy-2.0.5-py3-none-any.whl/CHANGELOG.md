## Unreleased

### BREAKING CHANGE

- Since version 2.0.0 Python 2 is no more supported

### Fix

- Append a / at the end if not present
- Fix problems with jsonid in login

### Refactor

- Remove support for Python2

## v1.2.4 (2021-11-22)

## v.1.2.1 (2021-05-17)

### Fix

- restore missing Class needed for QGIS Plugin

## v1.2.0 (2021-05-12)

### BREAKING CHANGE

- the geometry parameter in query, accept an ESRI Geometry and it's used for spatial filter. Every other parameter for standard EMS can be added.

### Feat

- Add filter option for master: better handling of exception.
- Add asUrl for attachment info
- **28405**: WEGA EMSPY - CLI um ein Projekt zu exportieren/importieren
- add updateAttachment to layer
- add deleteAttachment to layer
- add registerAttachment to layer
- add registerAttachment to layer
- add method to download an attachment
- add files to use Jenkins
- remove configuration file for gitlab ci
- add configuration file for gitlab ci
- add configuration file for gitlab ci
- update postgresql version to 11-2.5

### Fix

- check if variants tree has a root node
- handle not existing preferred variant
- Fix typing in python2
- Fix python2 logging syntax
- Fix python2 logging syntax
- add support for old geometry boolean
- Add scripts to the package build
- add_attachment fix file name to avoid including the path
- Fix returning id only from EmsLayer Query
- Fix returning id only from EmsLayer Query
- remove formatter for logging
- remove linting errors
- correct name for gitlab CI
- correct name for gitlab CI
- remove temp Directory after tests
- Add Database password for PostgreSQL to avoid error on starting
- wrong spelling in pyproject.toml

### Refactor

- We check if ems is running, before tests This avoids to use sleep or random wait.
- Move code frm SVN to GIT
- Move code frm SVN to GIT
- Move code frm SVN to GIT
- Move code frm SVN to GIT
- Move code frm SVN to GIT
