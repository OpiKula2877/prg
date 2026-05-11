@echo off
@chcp 65001 >nul
setlocal enableextensions

:zacatek
setlocal

set /p A="Zadejte hodnotu A: "
set /p B="Zadejte hodnotu B: "
set /p C="Zadejte hodnotu C: "
echo.
echo Pro pokračování stiskněte jakékoli tlačítko
pause > nul

:porovnej
if %A% GTR %B% (
    if %A% GTR %C% (
        if %B% GTR %C% (
            echo A
            echo B
            echo C
        ) else (
            echo A
            echo C
            echo B
        )
    ) else (
        echo C
        echo A
        echo B
    )
) else (
    if %B% GTR %C% (
        if %A% GTR %C% (
            echo B
            echo A
            echo C
        ) else (
            echo B
            echo C
            echo A
        )
    ) else (
        echo C
        echo B
        echo A
    )
)

pause
cls
goto zacatek