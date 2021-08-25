@echo off

where /q python
IF ERRORLEVEL 1 (
    ECHO "Python is missing. Please make sure you have it installed and placed in your PATH."
    EXIT /B
) ELSE (
    pip install .
    python setup.py install
)
