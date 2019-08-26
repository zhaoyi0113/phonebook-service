#!/bin/sh -eu
nosetests ./api/test/test* --with-coverage --cover-package=api --cover-xml --cover-xml-file=reports/coverage.xml --debug=tests