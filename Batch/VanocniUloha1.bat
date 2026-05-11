@echo off
chcp 65001
setlocal enabledelayedexpansion

set /p vyska=Zadejte výšku stromku (v počtu řad): 

set dohromady=0
set ornaments=1

for /l %%i in (1,1,%vyska%) do (
    set /a dohromady+=ornaments
    set /a ornaments*=2
)
echo Celkovy pocet ozdob je %total%
pause