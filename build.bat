@echo off
chcp 65001 >nul
echo ======================================================================
echo   Magic Lantern Auto Tagger - Build Script
echo ======================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
echo.
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)

echo.
echo ======================================================================
echo [2/3] Building executable with PyInstaller...
echo ======================================================================
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"

REM Build with PyInstaller
pyinstaller --onefile ^
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
echo [3/3] Build completed successfully!
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
