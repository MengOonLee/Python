#!/bin/bash

python3 -m venv env
source env/bin/activate
python3 -m pip install -U pip wheel
pip install -Ur requirements.txt --no-cache-dir
python3 setup.py install
python3 test/__main__.py
deactivate
rm -rf build dist env
