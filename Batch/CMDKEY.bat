@echo off
set /p Host="Enter a Host: "
set /p UserName="Enter a User Name: "
set /p Password="Enter a Password: "
cmdkey /add:%Host% /user:%UserName% /pass:%Password%