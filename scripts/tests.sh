#!/usr/bin/env bash

# https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin
# -e  Exit immediately if a command exits with a non-zero status.
# -x Print commands and their arguments as they are executed.
set -e

COVER_PROJECT_PATH=.
TESTS_PROJECT_PATH=tests
REPORTS_FOLDER_PATH=tests-reports

PYTHONPATH=. pytest $TESTS_PROJECT_PATH -n auto -vv --doctest-modules \
  --cov=$COVER_PROJECT_PATH \
  --cov-report=xml:$REPORTS_FOLDER_PATH/coverage.xml \
  --cov-report=html:$REPORTS_FOLDER_PATH/html \