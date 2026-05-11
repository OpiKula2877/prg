@echo off
@chcp 65001 >nul
setlocal enabledelayedexpansion

:setheslo
cls
echo.
echo.  /$$$$$$                      /$$   /$$                               /$$ 
echo. /$$__  $$                    ^| $$  ^| $$                              ^| $$ 
echo ^| $$  \__/  /$$$$$$  /$$$$$$$ ^| $$  ^| $$  /$$$$$$   /$$$$$$$  /$$$$$$ ^| $$ 
echo ^| $$ /$$$$ /$$__  $$^| $$__  $$^| $$$$$$$$ /$$__  $$ /$$_____/ /$$__  $$^| $$ 
echo ^| $$^|_  $$^| $$$$$$$$^| $$  \ $$^| $$__  $$^| $$$$$$$$^|  $$$$$$ ^| $$$$$$$$^| $$ 
echo ^| $$  \ $$^| $$_____/^| $$  ^| $$^| $$  ^| $$^| $$_____/ \____  $$^| $$_____/^| $$ 
echo ^|  $$$$$$/^|  $$$$$$$^| $$  ^| $$^| $$  ^| $$^|  $$$$$$$ /$$$$$$$/^|  $$$$$$$^| $$ 
echo  \______/  \_______/^|__/  ^|__/^|__/  ^|__/ \_______/^|_______/  \_______/^|__/ 
echo.

set -=
set --=--
set ---=--
set ----=--
set -----=--

set /p delka="Zadejte zde číslo, jak dlouhé bude heslo (1-99): "
if %delka%== set delka=1
if %delka% LSS 1 set delka=1
if %delka% GTR 99 set delka=99
if %delka% LSS 10 set -=---------------------------
if %delka% GEQ 10 set -=----------------------------

echo.!-!
echo. Nastavili jste délku na !delka!
echo.!-!
echo.

set /p MP="Chcete v heslu malá písmena? (Ano/Ne): "
set /p VP="Chcete v heslu velká písmena? (Ano/Ne): "
set /p C="Chcete v heslu čísla? (Ano/Ne): "
set /p SC="Chcete v heslu speciální znaky? (Ano/Ne): "

if %MP%==Ano set --=---
if %VP%==Ano set ---=---
if %C%==Ano set ----=---
if %SC%==Ano set -----=---

echo.!--!!---!!----!!-----!------------------------------------------------------------
echo. Písmena: Malá - %MP%, Velká - %VP% ^| Čísla - %C% ^| Speciální znaky - %SC%
echo.!--!!---!!----!!-----!------------------------------------------------------------

set pool=
if /i "%MP%"=="Ano" set "pool=!pool!abcdefghijklmnopqrstuvwxyz"
if /i "%VP%"=="Ano" set "pool=!pool!ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if /i "%C%"=="Ano" set "pool=!pool!0123456789"
if /i "%SC%"=="Ano" set "pool=!pool!*-_=+[]{}|;:,.<>?"

if "!pool!"=="" (
    echo.
    echo Chyba: Musíte vybrat alespoň jeden typ znaků!
    echo.
    echo. Chcete to zkusit znova? Zmáčkněte enter.
    pause >nul
    goto setheslo
)

set "pool_len=0"
set "temp_pool=!pool!"
:len_loop
if not "!temp_pool!"=="" (
    set /a pool_len+=1
    set "temp_pool=!temp_pool:~1!"
    goto len_loop
)

set "password="
for /L %%i in (1,1,%delka%) do (
    set /a "rand_idx=!random! %% pool_len"
    for /f "delims=" %%a in ("!rand_idx!") do (
        set "char=!pool:~%%a,1!"
        set "password=!password!!char!"
    )
)

echo.
echo Vaše nové heslo je:
echo.
echo.------------------------------------------------------------
echo.!password!
echo.------------------------------------------------------------
echo.
echo. Chcete nově vytvořit další heslo? Zmáčkněte enter.
pause >nul
goto setheslo