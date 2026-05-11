@echo off
@chcp 65001 >nul
mode con cols=51 lines=19
@title Mail

:nova
set /a v1=2
set /a v2=1
call MailPamet.bat
if %v1% equ %v2% (
goto cislo
)
goto cislovka
:cislovka
set /a nejakykod=%random%%random%
set /a cislo=%random% %% 49 + 1
set /a pam=%random% %% 2
set /a i=1
:cislo
goto %cislo%
:1 
set vydavatel=Adam Tomášek
goto X
:2 
set vydavatel=Aneta Šimačková
goto X
:3 
set vydavatel=Filip Havel
goto X
:4 
set vydavatel=Gabriela Kocourková
goto X
:5 
set vydavatel=Jan Doležal
goto X
:6 
set vydavatel=Klára Pospíchalová
goto X
:7 
set vydavatel=Kristýna Kadeřábková
goto X
:8 
set vydavatel=Marek Růžička
goto X
:9 
set vydavatel=Martin Vacek
goto X
:10 
set vydavatel=Pavel Konečný
goto X
:11 
set vydavatel=Tomáš Hrubý
goto X
:12 
set vydavatel=Veronika Pospíšilová
goto X
:13 
set vydavatel=Barbora Vávrová
goto X
:14 
set vydavatel=Dominika Švécová
goto X
:15 
set vydavatel=Jakub Kučera
goto X
:16 
set vydavatel=Jana Novotná
goto X
:17 
set vydavatel=Jan Rychlý
goto X
:18 
set vydavatel=Karolína Janotová
goto X
:19 
set vydavatel=Kristýna Dlouhá
goto X
:20 
set vydavatel=Lucie Kovaříková
goto X
:21 
set vydavatel=Lukáš Novák
goto X
:22 
set vydavatel=Marek Vaněk
goto X
:23 
set vydavatel=Martin Procházka
goto X
:24 
set vydavatel=Michal Urban
goto X
:25 
set vydavatel=Petr Malý
goto X
:26 
set vydavatel=Tereza Svobodová
goto X
:27 
set vydavatel=Tomas Prokop
goto X
:28 
set vydavatel=Veronika Maresová
goto X
:29 
set vydavatel=Andrea Prokopová
goto X
:30 
set vydavatel=Eva Vlasáková
goto X
:31 
set vydavatel=Jakub Kříž
goto X
:32 
set vydavatel=Jiří Bilek
goto X
:33 
set vydavatel=Kateřína Černá
goto X
:34 
set vydavatel=Lenka Chalupová
goto X
:35 
set vydavatel=Markéta Holubová
goto X
:36 
set vydavatel=Michaela Beránková
goto X
:37 
set vydavatel=Ondřej Beneš
goto X
:38 
set vydavatel=Tomáš Kučera
goto X
:39 
set vydavatel=Alena Jirásková
goto X
:40 
set vydavatel=David Macháček
goto X
:41 
set vydavatel=Jakub Šimůnek
goto X
:42 
set vydavatel=Jan Hruška
goto X
:43 
set vydavatel=Karolína Kratochvílová
goto X
:44 
set vydavatel=Lukáš Matějka
goto X
:45 
set vydavatel=Nikola Zemanová
goto X
:46 
set vydavatel=Pavel Zábranský
goto X
:47 
set vydavatel=Simona Štěpanová
goto X
:48 
set vydavatel=Václav Kučera
goto X
:49 
set vydavatel=Barbora Šťastná
goto X
:50 
set vydavatel=Eliška Horáčková
goto X
:X
(
echo set /a v2=2
echo set /a cislo=%cislo%
echo set /a nejakykod=%nejakykod%
echo set /a pam=%pam%
)>MailPamet.bat
:zacatek
cls
echo.
echo       ███╗   ███╗ █████╗ ██╗██╗
echo       ████╗ ████║██╔══██╗██║██║
echo       ██╔████╔██║███████║██║██║
echo       ██║╚██╔╝██║██╔══██║██║██║
echo       ██║ ╚═╝ ██║██║  ██║██║███████╗
echo       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
echo.
echo    ---------------------------------------------
echo     Nová zpráva od klienta %nejakykod%
echo    ---------------------------------------------
echo   *1. otevřít
echo.
set /p odpoved=">> "

if %pam%==1 (goto vyb2) else (goto vyb)

if %odpoved%==1 goto :vyb
:vyb
if %cislo%==1 goto A
if %cislo%==2 goto B
if %cislo%==3 goto C
if %cislo%==4 goto D
if %cislo%==5 goto E
if %cislo%==6 goto F
if %cislo%==7 goto G
if %cislo%==8 goto H
if %cislo%==9 goto I
if %cislo%==10 goto J
if %cislo%==11 goto K
if %cislo%==12 goto L
if %cislo%==13 goto M
if %cislo%==14 goto N
if %cislo%==15 goto O
if %cislo%==16 goto P
if %cislo%==17 goto Q
if %cislo%==18 goto R
if %cislo%==19 goto S
if %cislo%==20 goto T
if %cislo%==21 goto U
if %cislo%==22 goto V
if %cislo%==23 goto W
if %cislo%==24 goto X
if %cislo%==25 goto Y
if %cislo%==26 goto Z
if %cislo%==27 goto AA
if %cislo%==28 goto AB
if %cislo%==29 goto AC
if %cislo%==30 goto AD
if %cislo%==31 goto AE
if %cislo%==32 goto AF
if %cislo%==33 goto AG
if %cislo%==34 goto AH
if %cislo%==35 goto AI
if %cislo%==36 goto AJ
if %cislo%==37 goto AK
if %cislo%==38 goto AL
if %cislo%==39 goto AM
if %cislo%==40 goto AN
if %cislo%==41 goto AO
if %cislo%==42 goto AP
if %cislo%==43 goto AQ
if %cislo%==44 goto AR
if %cislo%==45 goto AS
if %cislo%==46 goto AT
if %cislo%==47 goto AU
if %cislo%==48 goto AV
if %cislo%==49 goto AW
if %cislo%==50 goto AX


:A
call source\MailPat.bat
if %odp%==738K6F4D9G2H1I3A5J goto wn
goto ls
:B
call source\MailPat.bat
if %odp%==2H6J7D3B8A4I9G1F5E goto wn
goto ls
:C
call source\MailPat.bat
if %odp%==9J8H4D7C6A2G1I5F3E goto wn
goto ls
:D
call source\MailPat.bat
if %odp%==4I8H1G7C5B3J9A6F2D goto wn
goto ls
:E
call source\MailPat.bat
if %odp%==3C9B5A1G7H8F4I6D2J goto wn
goto ls
:F
call source\MailPat.bat
if %odp%==7E2A1G3J4H9F8C6D5B goto wn
goto ls
:G
call source\MailPat.bat
if %odp%==5F8D4C2B1I9J7H6A3G goto wn
goto ls
:H
call source\MailPat.bat
if %odp%==1J9D5A8G2B7H4F3C6I goto wn
goto ls
:I
call source\MailPat.bat
if %odp%==6E4D3J2A1C7F5H8G9B goto wn
goto ls
:J
call source\MailPat.bat
if %odp%==2I7F8B6G9D5A3H1J4C goto wn
goto ls
:K
call source\MailPat.bat
if %odp%==5G3A7H1J4I8F6D9E2C goto wn
goto ls
:L
call source\MailPat.bat
if %odp%==9F1G5J7I4E6A8D3B2C goto wn
goto ls
:M
call source\MailPat.bat
if %odp%==2B7D8C4G6F1J9I5H3A goto wn
goto ls
:N
call source\MailPat.bat
if %odp%==6J4F8H3D1A2I7C9E5B goto wn
goto ls
:O
call source\MailPat.bat
if %odp%==3I9E1D5J6B8H7F2C4A goto wn
goto ls
:P
call source\MailPat.bat
if %odp%==1I6D4H8J7G5B2F9A3C goto wn
goto ls
:Q
call source\MailPat.bat
if %odp%==8A3G5E2C1J9D7H6B4F goto wn
goto ls
:R
call source\MailPat.bat
if %odp%==4I2C9A8J6F3G5E1D7B goto wn
goto ls
:S
call source\MailPat.bat
if %odp%==6H8A4C7B1E9I3F5J2D goto wn
goto ls
:T
call source\MailPat.bat
if %odp%==3F1A7H9I2G4J6D8C5E goto wn
goto ls
:U
call source\MailPat.bat
if %odp%==8C7B6D2J4E9I5H1A3G goto wn
goto ls
:V
call source\MailPat.bat
if %odp%==7B3H8C1G6J4A2D5I9F goto wn
goto ls
:W
call source\MailPat.bat
if %odp%==9J1D3C5E8F7G6H2I4A goto wn
goto ls
:X
call source\MailPat.bat
if %odp%==4C9D2J5A1G8H6I7F3B goto wn
goto ls
:Y
call source\MailPat.bat
if %odp%==6F4D7C8I9A5E2H1J3G goto wn
goto ls
:Z
call source\MailPat.bat
if %odp%==2H1J8G4E5D3B7C6F9A goto wn
goto ls
:AA
call source\MailPat.bat
if %odp%==1I3A7G9B4J8F5E2C6D goto wn
goto ls
:AB
call source\MailPat.bat
if %odp%==5E8H6F3C1A4G9B7I2J goto wn
goto ls
:AC
call source\MailPat.bat
if %odp%==2D7I4G1H9A6J5C3E8F goto wn
goto ls
:AD
call source\MailPat.bat
if %odp%==5A8C3B7F1D9J2I4G6H goto wn
goto ls
:AE
call source\MailPat.bat
if %odp%==6J9E4A1H2G7D5B8F3C goto wn
goto ls
:AF
call source\MailPat.bat
if %odp%==3C8B6J9F2H4G5D1I7A goto wn
goto ls
:AG
call source\MailPat.bat
if %odp%==1H5A7C3G6E4F9J2B8D goto wn
goto ls
:AH
call source\MailPat.bat
if %odp%==9D2I8C4A1B3E6H5G7J goto wn
goto ls
:AI
call source\MailPat.bat
if %odp%==7G3D6F5J8B9C2A1H4I goto wn
goto ls
:AJ
call source\MailPat.bat
if %odp%==4F6H2B8A7I3J9C5D1E goto wn
goto ls
:AK
call source\MailPat.bat
if %odp%==8E5C1A7J4F2D6G9B3I goto wn
goto ls
:AL
call source\MailPat.bat
if %odp%==2H9G5F3J6I7B1C8D4A goto wn
goto ls
:AM
call source\MailPat.bat
if %odp%==6C2D8G1F9H4A3I7B5E goto wn
goto ls
:AN
call source\MailPat.bat
if %odp%==4F7A1J5C2I6E3H8B9D goto wn
goto ls
:AO
call source\MailPat.bat
if %odp%==9I3D7F8E6A1C4J2B5H goto wn
goto ls
:AP
call source\MailPat.bat
if %odp%==2E8B6H7C4D5F1G3I9J goto wn
goto ls
:AQ
call source\MailPat.bat
if %odp%==1H9A5B6J7I3G8D2C4F goto wn
goto ls
:AR
call source\MailPat.bat
if %odp%==3D5J8C4B2F9E7G1H6I goto wn
goto ls
:AS
call source\MailPat.bat
if %odp%==8G4D2A6F3H5J7I9E1C goto wn
goto ls
:AT
call source\MailPat.bat
if %odp%==7I6C9H3E1B8A4J2D5F goto wn
goto ls
:AU
call source\MailPat.bat
if %odp%==5F1G3A4J2D9E7H8C6B goto wn
goto ls
:AV
call source\MailPat.bat
if %odp%==9J7I6E2D4H1B3A5C8F goto wn
goto ls
:AW
call source\MailPat.bat
if %odp%==3D8E5J6G9A7H1C4I2F goto wn
goto ls
:AX
call source\MailPat.bat
if %odp%==6I9H2C1B3J5F8D7E4A goto wn
goto ls

:vyb2
if %cislo%==1 goto A2
if %cislo%==2 goto B2
if %cislo%==3 goto C2
if %cislo%==4 goto D2
if %cislo%==5 goto E2
if %cislo%==6 goto F2
if %cislo%==7 goto G2
if %cislo%==8 goto H2
if %cislo%==9 goto I2
if %cislo%==10 goto J2
if %cislo%==11 goto K2
if %cislo%==12 goto L2
if %cislo%==13 goto M2
if %cislo%==14 goto N2
if %cislo%==15 goto O2
if %cislo%==16 goto P2
if %cislo%==17 goto Q2
if %cislo%==18 goto R2
if %cislo%==19 goto S2
if %cislo%==20 goto T2
if %cislo%==21 goto U2
if %cislo%==22 goto V2
if %cislo%==23 goto W2
if %cislo%==24 goto X2
if %cislo%==25 goto Y2
if %cislo%==26 goto Z2
if %cislo%==27 goto AA2
if %cislo%==28 goto AB2
if %cislo%==29 goto AC2
if %cislo%==30 goto AD2
if %cislo%==31 goto AE2
if %cislo%==32 goto AF2
if %cislo%==33 goto AG2
if %cislo%==34 goto AH2
if %cislo%==35 goto AI2
if %cislo%==36 goto AJ2
if %cislo%==37 goto AK2
if %cislo%==38 goto AL2
if %cislo%==39 goto AM2
if %cislo%==40 goto AN2
if %cislo%==41 goto AO2
if %cislo%==42 goto AP2
if %cislo%==43 goto AQ2
if %cislo%==44 goto AR2
if %cislo%==45 goto AS2
if %cislo%==46 goto AT2
if %cislo%==47 goto AU2
if %cislo%==48 goto AV2
if %cislo%==49 goto AW2
if %cislo%==50 goto AX2

:A2
call source\MailPat2.bat
if %odp%==741952863 goto wn
goto ls2
:B2
call source\MailPat2.bat
if %odp%==483915726 goto wn
goto ls2
:C2
call source\MailPat2.bat
if %odp%==769824153 goto wn
goto ls2
:D2
call source\MailPat2.bat
if %odp%==215697384 goto wn
goto ls2
:E2
call source\MailPat2.bat
if %odp%==638471592 goto wn
goto ls2
:F2
call source\MailPat2.bat
if %odp%==954382167 goto wn
goto ls2
:G2
call source\MailPat2.bat
if %odp%==127546839 goto wn
goto ls2
:H2
call source\MailPat2.bat
if %odp%==896213475 goto wn
goto ls2
:I2
call source\MailPat2.bat
if %odp%==341759268 goto wn
goto ls2
:J2
call source\MailPat2.bat
if %odp%==572948316 goto wn
goto ls2
:K2
call source\MailPat2.bat
if %odp%==639714582 goto wn
goto ls2
:L2
call source\MailPat2.bat
if %odp%==741952863 goto wn
goto ls2
:M2
call source\MailPat2.bat
if %odp%==825136947 goto wn
goto ls2
:N2
call source\MailPat2.bat
if %odp%==497582163 goto wn
goto ls2
:O2
call source\MailPat2.bat
if %odp%==351679824 goto wn
goto ls2
:P2
call source\MailPat2.bat
if %odp%==914257638 goto wn
goto ls2
:Q2
call source\MailPat2.bat
if %odp%==783465219 goto wn
goto ls2
:R2
call source\MailPat2.bat
if %odp%==146328975 goto wn
goto ls2
:S2
call source\MailPat2.bat
if %odp%==572819346 goto wn
goto ls2
:T2
call source\MailPat2.bat
if %odp%==726591348 goto wn
goto ls2
:U2
call source\MailPat2.bat
if %odp%==834267915 goto wn
goto ls2
:V2
call source\MailPat2.bat
if %odp%==983726514 goto wn
goto ls2
:W2
call source\MailPat2.bat
if %odp%==615942783 goto wn
goto ls2
:X2
call source\MailPat2.bat
if %odp%==257138469 goto wn
goto ls2
:Y2
call source\MailPat2.bat
if %odp%==392684157 goto wn
goto ls2
:Z2
call source\MailPat2.bat
if %odp%==471359826 goto wn
goto ls2
:AA2
call source\MailPat2.bat
if %odp%==568214937 goto wn
goto ls2
:AB2
call source\MailPat2.bat
if %odp%==649813257 goto wn
goto ls2
:AC2
call source\MailPat2.bat
if %odp%==815426793 goto wn
goto ls2
:AD2
call source\MailPat2.bat
if %odp%==237594618 goto wn
goto ls2
:AE2
call source\MailPat2.bat
if %odp%==983175246 goto wn
goto ls2
:AF2
call source\MailPat2.bat
if %odp%==754362981 goto wn
goto ls2
:AG2
call source\MailPat2.bat
if %odp%==126947835 goto wn
goto ls2
:AH2
call source\MailPat2.bat
if %odp%==391258467 goto wn
goto ls2
:AI2
call source\MailPat2.bat
if %odp%==578641329 goto wn
goto ls2
:AJ2
call source\MailPat2.bat
if %odp%==462739185 goto wn
goto ls2
:AK2
call source\MailPat2.bat
if %odp%==679248513 goto wn
goto ls2
:AL2
call source\MailPat2.bat
if %odp%==524731968 goto wn
goto ls2
:AM2
call source\MailPat2.bat
if %odp%==318965247 goto wn
goto ls2
:AN2
call source\MailPat2.bat
if %odp%==896152734 goto wn
goto ls2
:AO2
call source\MailPat2.bat
if %odp%==457389621 goto wn
goto ls2
:AP2
call source\MailPat2.bat
if %odp%==263714859 goto wn
goto ls2
:AQ2
call source\MailPat2.bat
if %odp%==941637582 goto wn
goto ls2
:AR2
call source\MailPat2.bat
if %odp%==185476329 goto wn
goto ls2
:AS2
call source\MailPat2.bat
if %odp%==732598146 goto wn
goto ls2
:AT2
call source\MailPat2.bat
if %odp%==217865493 goto wn
goto ls2
:AU2
call source\MailPat2.bat
if %odp%==956341827 goto wn
goto ls2
:AV2
call source\MailPat2.bat
if %odp%==483729615 goto wn
goto ls2
:AW2
call source\MailPat2.bat
if %odp%==694158732 goto wn
goto ls2
:AX2
call source\MailPat2.bat
if %odp%==371492586 goto wn
goto ls2

:wn
call source\MailPatWN.bat
echo  > source\MailPamet.bat
call source\Kredit.bat
set kredit=%kredit% + 1 > nul
echo set /a kredit=%kredit% > source\Kredit.bat
timeout 3 > nul
goto cislovka

:ls
call source\MailPatLS.bat
timeout 3 > nul
goto vyb

:ls2
call source\MailPatLS2.bat
timeout 3 > nul
goto vyb2