@setlocal
@echo off
cls

if "%~1"=="run" set DO_RUN=1
if "%~1"=="test" set DO_TEST=1

@REM Init env
if not exist .venv (
    echo [.venv] Doesn't exist, creating...
    python -m venv .venv
    echo [.venv] Created.
)

call .venv\scripts\activate

@REM Look for any missing requirements.
set MISSING_REQUIREMENT_FOUND=0

for /F "tokens=1 delims==" %%A in (requirements.txt) do (
    @REM TODO... detect installations with embedded version
    if not exist .venv\Lib\site-packages\%%A (
        echo Not installed yet: [%%A]
        set MISSING_REQUIREMENT_FOUND=1
    )
)

@REM Install requirements if any found missing.
if "1" == "%MISSING_REQUIREMENT_FOUND%" (
    pip install -r requirements.txt
)

@REM Run
if "%DO_TEST%"=="1" ( python -m unittest discover )
if "%DO_RUN%"=="1" ( python main.py )

@REM Shutdown env
deactivate
