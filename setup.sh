#! /bin/bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install pywhispercpp
python3 setup_models.py
python3 main.py
