@echo off
@chcp 65001 >nul

:1
setlocal

:: Známka
set /p Znamka="Jakou jsi dostal známku: "

:: Porovnání známky s 5
if %Znamka% EQU 5 (
    echo Dostal jsi 5? jsi v řiti.
) else if %Znamka% EQU 1 (
    echo Dobře ty.
) else if %Znamka% EQU 2 (
    echo Pohoda.
) else if %Znamka% EQU 3 (
    echo Tady už je to docela o fous.
) else if %Znamka% EQU 4 (
    echo TO je taky blbí.
) else if %Znamka% LSS 1 (
    echo Jsi si jistej že jsi dostal tuhle známku?
) else if %Znamka% GTR 5 (
    echo Jsi si jistej že jsi dostal tuhle známku?
) else (
    Hmm.
)

endlocal
pause
cls
goto 1