@echo off
@chcp 65001 >nul
setlocal
:CD
:: Dotaz na hodnotu CD
set /p CD="Zadej hodnotu pro CountDown: "

:: Snižování
:otazka
if %CD% GTR 0 (
    goto vetsi
) else if %CD% EQU 0 (
    goto stejne
) else (
    goto znova
)

:vetsi
set /a CD=CD-1
echo %CD%
goto otazka

:znova
echo zadej hodnotu větší jak 0
pause > nul
cls
goto CD

:stejne
echo START!!!!
pause > nul
endlocal
cls
goto CD