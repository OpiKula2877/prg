import requests, json
from api import StravaApi, Sid
from datetime import datetime
cookies = "NEXT_LOCALE=cs; multiContextSession=%7B%22printOpen%22%3A%7B%22value%22%3Afalse%2C%22expiration%22%3A-1%7D%7D"
username = "Pelc"
password = "SamuelPelc2009"
jidelna = 6218
autorization_token = Sid(username, password, jidelna, "")
sid = autorization_token.getSid()
api_session = StravaApi(sid, jidelna, cookies, "", username)
# zavoláme endpoint
jidelnicek_json = api_session.getJidelnicek()
jidelnicek = json.loads(jidelnicek_json) if isinstance(jidelnicek_json, str) else jidelnicek_json

# Získání dnešního data ve formátu DD.MM.YYYY
today = datetime.now().strftime("%d.%m.%Y")

# Projít všechny tabulky a najít jídla pro dnešní den
today_jidla_list = []
if isinstance(jidelnicek, dict):
    # Projít všechny klíče (table0, table1, table2, atd.)
    for table_key in sorted(jidelnicek.keys()):
        if table_key.startswith("table") and isinstance(jidelnicek[table_key], list):
            for jidlo in jidelnicek[table_key]:
                # Zkontrolovat, zda je jídlo pro dnešní den a má pocet == 1 (je vybrané)
                if isinstance(jidlo, dict) and jidlo.get("datum") == today and jidlo.get("pocet", 0) == 1:
                    today_jidla_list.append(jidlo)
elif isinstance(jidelnicek, list):
    # Pokud je jidelnicek přímo seznam (starší verze API)
    for jidlo in jidelnicek:
        # Zkontrolovat, zda je jídlo pro dnešní den a má pocet == 1 (je vybrané)
        if isinstance(jidlo, dict) and jidlo.get("datum") == today and jidlo.get("pocet", 0) == 1:
            today_jidla_list.append(jidlo)

# Formátování zprávy pro Discord
if today_jidla_list:
    message_parts = [f"-------------------------------------------------------------\n**Jídelníček na {today}**\n\n **Nedáme si dneska takovej menší špíček?**\n"]
    # Seřadit jídla podle druhu (Snídaně, Polévka, Oběd, Večeře, atd.)
    poradi_druhu = {"SN": 1, "PO": 2, "OB": 3, "VE": 4, "DW": 5, "BA": 6}
    today_jidla_list.sort(key=lambda x: poradi_druhu.get(x.get("druh", ""), 99))
    
    for jidlo in today_jidla_list:
        druh = jidlo.get("druh_popis", "Neznámý")
        nazev = jidlo.get("nazev", "Bez názvu")
        message_parts.append(f"**{druh}:** {nazev}")
    today_jidla = "\n".join(message_parts)+f"\n-------------------------------------------------------------"
else:
    today_jidla = f"Pro dnešní den ({today}) nejsou k dispozici žádná jídla.\n-------------------------------------------------------------"

# Vlož sem URL webhooku, který jsi zkopíroval z Discordu
WEBHOOK_URL = "https://discord.com/api/webhooks/1447693089027260436/9XvwodjM4IdzcydL8Gkm5DPQ8rN90DhKJs1cuG2TpzUEPW48yMpQ6tG2DOkzYJwBlm0M"

# Zpráva, kterou chceš poslat
data = {
    "content": today_jidla
}
# Odešli požadavek
response = requests.post(WEBHOOK_URL, json=data)

# Zkontroluj, jestli to fungovalo
if response.status_code == 204:
    print("Zpráva odeslána na Discord!")
else:
    print(f"Chyba: {response.status_code} – {response.text}")
