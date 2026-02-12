@echo off
chcp 65001 >nul
echo ======================================================================
echo   Magic Lantern Auto Tagger - Build Script (with uv)
echo ======================================================================
echo.

REM Check if uv is installed
uv --version >nul 2>&1
if errorlevel 1 (
    echo [INFO] uv is not installed. Installing uv...
    echo.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to install uv!
        echo Please install manually from: https://github.com/astral-sh/uv
        echo.
        pause
        exit /b 1
    )
    echo [SUCCESS] uv installed successfully!
    echo.
)

echo [1/4] Creating virtual environment...
echo.
if not exist ".venv" (
    uv venv
    if errorlevel 1 (
        echo.
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
)

echo [2/4] Installing dependencies with uv (fast!)...
echo.
uv pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo ======================================================================
echo [3/4] Building executable with PyInstaller...
echo ======================================================================
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"

REM Build with PyInstaller (using uv run to use the virtual environment)
uv run pyinstaller --onefile ^
    --name "MagicLanternTagger" ^
    --icon=NONE ^
    --add-data "magic_lantern.jpeg;." ^
    --console ^
    --clean ^
    auto_tagger.py

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo.
echo ======================================================================
echo [4/4] Build completed successfully!
echo ======================================================================
echo.
echo Executable location: dist\MagicLanternTagger.exe
echo.
echo You can now:
echo   1. Copy MagicLanternTagger.exe to any folder with music files
echo   2. Make sure magic_lantern.jpeg is in the same folder
echo   3. Double-click MagicLanternTagger.exe to run
echo.
echo Note: The .exe file does NOT require Python to be installed!
echo.

pause
