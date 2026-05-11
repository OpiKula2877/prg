@echo off
@chcp 65001 >nul
setlocal enabledelayedexpansion

:zacatek
cls
set /p deset="Zadejte číslo, které chcete dát na dvojkovou soustavu: "
set binary=
:pocitani
set /a remainder=deset %% 2
set binary=!remainder!!binary!
set /a deset=deset / 2
if %deset% gtr 0 goto pocitani

echo.
echo Číslo je v dvojkové soustave %binary%
echo.
echo Pro pokračívání stiskněte enter.
pause >nul
goto zacatek