#!/bin/sh -eu
nosetests ./api/test/test* ./api/test/unit_test/unit_test* --with-coverage --cover-package=api --cover-xml --cover-xml-file=reports/coverage.xml