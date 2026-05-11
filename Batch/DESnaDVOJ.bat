@echo off
@chcp 65001 >nul
setlocal enabledelayedexpansion

:set
setlocal enabledelayedexpansion
cls
set /p number="Zadejte číslo v desítkové soustavě: "
set binary=

:loop
if %number% lss 1 (
    goto end
)

set /a remainder=%number% %% 2
set /a number=%number% / 2
set binary=!remainder!!binary!
goto loop

:end
echo Dvojková soustava: !binary!
endlocal
pause > nul
goto set