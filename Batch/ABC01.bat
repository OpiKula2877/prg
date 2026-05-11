@echo off
@chcp 65001 >nul

:zacatek
setlocal


set /p A="Zadejte hodnotu A: "
set /p B="Zadejte hodnotu B: "
set /p C="Zadejte hodnotu C: "
echo.
echo Pro pokračování stiskněte jakékoli tlačítko
pause > nul
goto x

:x
if %A% GTR %B% (
    goto AgtrB
) else
    goto NoAgtrB

:AgtrB
if %A% GTR %C% (
    goto AgtrC1
) else
    goto NoAgtrC1

:AgtrC1
if %B% GTR %C% (
    goto BgtrC1
) else
    goto NoBgtrC1

:BgtrC1
echo C
echo B
echo A
pause
cls
goto zacatek

:NoBgtrC1
echo B
echo C
echo A
pause
cls
goto zacatek

:NoAgtrC1
echo B
echo A
echo C
pause
cls
goto zacatek

::------------------------------------------------------

:NoAgtrB
if %A% GTR %C% (
    goto BgtrC2
) else
    goto NoAgtrC2

:NoAgtrC2
if %B% GTR %C% (
    goto BgtrC2
) else
    goto NoBgtrC2

:BgtrC2
echo C
echo A
echo B
pause
cls
goto zacatek

:BgtrC2
echo A
echo C
echo B
pause
cls
goto zacatek

:NoBgtrC2
echo A
echo B
echo C
pause
cls
goto zacatek



endlocal
pause
cls
goto 1