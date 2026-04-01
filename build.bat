@echo off
setlocal
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

echo [1/5] Creating virtual environment...
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

echo [2/5] Installing dependencies with uv (fast!)...
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
echo [3/5] Building executable with PyInstaller...
echo ======================================================================
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

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
echo [4/5] Copying ffmpeg and license files...
echo.
copy README.md dist\README.md >nul
copy ffmpeg-LICENSE dist\ffmpeg-LICENSE >nul
copy ffmpeg-README.txt dist\ffmpeg-README.txt >nul
powershell -NoProfile -Command ^
    "$cmd = Get-Command ffmpeg -ErrorAction Stop; " ^
    "$item = Get-Item $cmd.Source -Force; " ^
    "$ffmpegPath = if ($item.Target) { $item.Target[0] } elseif ($item.DirectoryName -like '*\chocolatey\bin') { Join-Path $env:ChocolateyInstall 'lib\ffmpeg\tools\ffmpeg\bin\ffmpeg.exe' } else { $item.FullName }; " ^
    "if (-not (Test-Path $ffmpegPath)) { throw ('Resolved ffmpeg binary not found: ' + $ffmpegPath) }; " ^
    "Copy-Item -LiteralPath $ffmpegPath -Destination 'dist\ffmpeg.exe' -Force"

if errorlevel 1 (
    echo.
    echo [ERROR] Failed to copy ffmpeg distribution files!
    echo Install ffmpeg or make sure it is available in PATH.
    pause
    exit /b 1
)

echo.
echo ======================================================================
echo [5/5] Build completed successfully!
echo ======================================================================
echo.
echo Executable location: dist\MagicLanternTagger.exe
echo.
echo You can now:
echo   1. Copy MagicLanternTagger.exe and ffmpeg.exe to any folder with music files
echo   2. Keep README.md, ffmpeg-LICENSE, and ffmpeg-README.txt with the distribution
echo   3. Double-click MagicLanternTagger.exe to run
echo.
echo Note: The .exe file does NOT require Python to be installed!
echo.

pause
