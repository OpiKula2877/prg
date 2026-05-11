@echo off
@chcp 65001 >nul
:start
cls
set "NowTime=%time: =0%"
set "HH=%NowTime:~0,2%"
set "MM=%NowTime:~3,2%"
set "Hours_Minutes=%HH%:%MM%"

echo Aktuální čas: %Hours_Minutes%
echo Hodina čas: %HH%
echo Minula čas: %MM%

if "%Hours_Minutes%" geq "08:05" if "%Hours_Minutes%" leq "08:50" (
    echo 1.hodina
    goto loop
) else if "%Hours_Minutes%" geq "09:00" if "%Hours_Minutes%" leq "09:45" (
    echo 2.hodina
    goto loop
) else if "%Hours_Minutes%" geq "10:05" if "%Hours_Minutes%" leq "10:50" (
    echo 3.hodina
    goto loop
) else if "%Hours_Minutes%" geq "11:00" if "%Hours_Minutes%" leq "11:45" (
    echo 4.hodina
    goto loop
) else if "%Hours_Minutes%" geq "11:55" if "%Hours_Minutes%" leq "12:40" (
    echo 5.hodina
    goto loop
) else if "%Hours_Minutes%" geq "12:45" if "%Hours_Minutes%" leq "13:30" (
    echo 6.hodina
    goto loop
) else if "%Hours_Minutes%" geq "13:35" if "%Hours_Minutes%" leq "14:20" (
    echo 7.hodina
    goto loop
) else (
    echo Přestávka
    goto loop
)
:loop
timeout /t 1 /nobreak >nul
set "current_time=%time: =0%"
set "current_min=%current_time:~3,2%"

if "%current_min%" neq "%MM%" (
    goto start
) else (
    goto loop
)