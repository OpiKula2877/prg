@echo off
@chcp 65001 >nul
:zacatek
set /p A=Zadej hodnotu A: 
set /p B=Zadej hodnotu B: 
set /p C=Zadej hodnotu C: 

set /a vzdA=A-C
set /a vzdB=B-C

if %vzdA% LSS 0 set /a vzdA=-vzdA
if %vzdB% LSS 0 set /a vzdB=-vzdB

if %vzdA% EQU %vzdB% (
    echo A i B jsou k C stejně daleko
) else if %vzdA% LSS %vzdB% (
    echo A je blíž k C
) else (
    echo B je blíž k C
)

pause >nul
cls
goto zacatek