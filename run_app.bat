@echo off
REM Check if venv exists
if exist venv (
    echo Virtual environment found.
) else (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
call venv\Scripts\activate

REM Install requirements
pip install --upgrade pip
pip install -r requirements.txt

REM Run the app
python app.py
