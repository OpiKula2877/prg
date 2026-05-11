@echo off
@chcp 65001 >nul
@title OpiKula
:zacatek
cls
echo ----------------------------
echo.      1. Start
echo ----------------------------
echo.      2. Add Questions
echo ----------------------------
echo.      2. Exit
echo ----------------------------
set /p odpoved=">> "
if %odpoved%==1 goto 1
if %odpoved%==2 goto 2
if %odpoved%==3 goto 3
goto zacatek
:1
start source\Menu.bat
exit
:2
start source\AddQuestions.bat
exit
:3
echo Exiting program...
timeout 2 /nobreak > nul
exit