@echo off
@chcp 65001 >nul
@title Menu
mode con cols=18 lines=10
:zacatek
cls
echo ------------------
echo      1. Start
echo ------------------
echo ------------------
echo      2. Reset
echo ------------------
echo ------------------
echo      3. Exit
echo ------------------
set /p odpoved=">> "
if %odpoved%==1 goto 1
if %odpoved%==2 goto 2
if %odpoved%==3 goto 3
goto zacatek
:1
start source\plocha.bat
exit
:2
call source\kredit.bat
cls
echo.
echo.
echo.
echo Resetování kreditů
echo.
echo %kredit% → 0
set /a kredit=0 > nul
echo set /a kredit=0 > source\kredit.bat
timeout 3 /nobreak > nul
goto zacatek
:3
exit