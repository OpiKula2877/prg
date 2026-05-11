@echo off
@chcp 65001 >nul
setlocal enableextensions

:zacatek
set /p A="Zadejte hodnotu A: "
if %A% EQU 0 (
goto nula
) else (
goto krat
)
:krat
set /a A=%A%*%A%
echo.
echo A*A = %A%
pause > nul
goto preskocit

:nula
echo Nula nejde dát na druhou.
pause > nul
goto preskocit

:preskocit
cls
goto zacatek