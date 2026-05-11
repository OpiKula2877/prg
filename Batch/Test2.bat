@echo off
@chcp 65001 >nul
setlocal

:: Dotaz na hodnotu A
set /p A="Zadej hodnotu pro A: "

:: Porovnání hodnoty A s 0
if %A% GTR 0 (
    echo A je větší než 0.
) else if %A% LSS 0 (
    echo A je menší než 0.
) else (
    echo A je rovno 0.
)

endlocal
pause