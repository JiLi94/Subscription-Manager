#!/bin/bash
# create virtual environment
python3 -m venv venv
source venv/bin/activate

# install required packages
pip install -r requirement.txt

# check python versions and run the appplication if python3 is installed
if [[ -x "$(command -v python)" ]]
then 
    if [[ $(python -V 2>&1) == 'Python 3'* ]]
    then
        python3 ./project/main.py
    else
        echo 'This application requires Python3 to be installed. Please install Python3 and try again.' >&2
        exit 1
    fi
else
    echo 'This application requires Python3 to be installed. Please install Python3 and try again.' >&2
    exit 1
fi