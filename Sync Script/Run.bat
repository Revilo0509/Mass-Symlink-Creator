@echo off

REM Find the path to python.exe
set PYTHON_PATH=
for /f "usebackq tokens=*" %%i in (`where python`) do (
    set PYTHON_PATH=%%i
    goto :found_python
)

:found_python
if "%PYTHON_PATH%"=="" (
    echo Python not found in PATH.
    exit /b 1
)

echo Python found at %PYTHON_PATH%

REM Run the Python script
"%PYTHON_PATH%" "%~dp0\Main.py"

REM Optionally, pause to see the output
pause
