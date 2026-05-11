@echo off
@chcp 65001 >nul
setlocal
:zacatek
:: Dotaz na hodnotu A
set /p A="Zadej hodnotu pro A která se bude snižovat: "

:: Snižování
:otazka
if %A% GTR 0 (
    goto vetsi
) else if %A% LSS 0 (
    goto mensi
) else (
    goto uzvpoho
)

:vetsi
set /a A=A-1
echo %a%
goto otazka

:mensi
set /a A=A+1
echo %a%
goto otazka

:uzvpoho
pause > nul
endlocal
cls
goto zacatek