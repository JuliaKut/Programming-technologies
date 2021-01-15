#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run python3 monitoring.py --once || true
exit 0