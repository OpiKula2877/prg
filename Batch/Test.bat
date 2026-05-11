@echo off
@chcp 65001 >nul
setlocal
:zacatek

:: Dotaz na hodnotu A
set /p A="Zadej hodnotu pro A: "

:: Dotaz na hodnotu B
set /p B="Zadej hodnotu pro B: "

:: Sečtení hodnot A a B
set /a C=A+B

:: Výpis výsledku
echo Výsledek A + B je: %C%
pause > nul
cls
set /a C=0
set /a B=0
set /a A=0
goto zacatek
endlocal