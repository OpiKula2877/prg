# Praktická úloha – konceptuální návrh databáze

## Téma: Evidence nasazených serverových služeb v malé infrastruktuře

### Obecné zadání

Malá firma provozuje několik **serverů**, na kterých běží různé **síťové / aplikační služby** (např. webový server, databázový server, DNS, VPN apod.).
Firma potřebuje jednoduchou databázi, která umožní evidovat:

* základní informace o serverech,
* jaké služby jsou na jednotlivých serverech nasazeny,
* kdy byla služba nasazena a v jakém režimu běží.

Databáze má sloužit jako podklad pro budoucí webovou administraci.

---

## Omezení návrhu

* **Maximálně 3 tabulky**
* **Maximálně 2 vztahy**
* Relační databáze **MySQL / MariaDB**
* Dokumentace a výstupy v **Markdownu**
* SQL skripty kompatibilní s MySQL / MariaDB

## Přehled dílčích zadání

## 1️⃣ Určení entitních a vztahových typů

### Zadání

Na základě obecného zadání:

* identifikuj **entitní typy**,
* identifikuj **vztahové typy**,
* stručně (1–2 věty) vysvětli, proč jsi zvolil právě tyto entity a vztahy.

### Požadovaný výstup

* seznam entitních a vztahových typů s textovým zdůvodněnín v Markdownu.

### Otázky k zamyšlení
1. Jaký význam mají v návrhu DB entitní a vztahový typ?

## 2️⃣ Diagram výskytu entit a vztahů

### (kardinalita a parcialita)

### Zadání

Pro navržené entity a vztahy:

* určete **kardinalitu vztahů** (1:1, 1:N, M:N),
* určete **parcialitu** (povinná / nepovinná účast entity ve vztahu),
* znázorněte diagram **textově** (např. pomocí odrážek nebo ASCII schématu).

### Požadovaný výstup

* slovní popis kardinality a parciality,
* jednoduchý diagram v Markdownu.

### Otázky k zamyšlení
1. Proč určujeme kardinalitu a parcialitu vztahů?

## 3️⃣ Určení atributů + normalizace (1. a 2. NF)

### Zadání

Navrhni atributy pro:

* každou entitu,
* vztahovou entitu (pokud vznikne).

Dále:

* ověř splnění **1. normální formy**,
* ověř splnění **2. normální formy**,
* případné úpravy návrhu zdůvodni.

### Požadovaný výstup

* seznam atributů po entitách,
* krátký komentář k 1. a 2. NF,
* vše v Markdownu.

### Otázky k zamyšlení
1. Jaký význam mají v relačním modelu atributy?
2. Proč provádíme normalizaci databáze?

## 4️⃣ Datové typy a integritní omezení

### Zadání

Pro každý atribut:

* navrhni **datový typ** (MySQL / MariaDB),
* určete **integritní omezení**, kde dávají smysl:

  * `PRIMARY KEY`
  * `NOT NULL`
  * `UNIQUE`
  * `FOREIGN KEY`
  * `CHECK`

### Požadovaný výstup

* tabulkový přehled atributů, datových typů a omezení (Markdown tabulky).

### Otázky k zamyšlení
1. Co jsou datové typy a jaký mají význam z hlediska uchovávání dat v DB?
2. Co jsou integritní omezení?

## 5️⃣ EER diagram (Markdown)

### Zadání

Vytvoř **zjednodušený EER diagram**, který bude:

* zachycen pomocí **Markdown tabulek**,
* přehledný a čitelný,
* obsahovat primární a cizí klíče.

### Požadovaný výstup

* EER diagram pouze v Markdownu (bez grafických nástrojů, např. pomocí dabulek).

### Otázky k zamyšlení
1. Co je EER diagram? Je nutné ho vždy využívat při tvorbě návrhu DB?
2. Co je primární, cizí a kandidátní klíč?

## 6️⃣ SQL CREATE SCRIPT

### Zadání

Na základě konceptuálního návrhu vytvoř:

* kompletní SQL skript pro vytvoření tabulek,
* včetně všech klíčů a omezení.

### Požadovaný výstup

* jeden SQL skript

### Otázky k zamyšlení
1. Co je SQL?
2. K čemu slouží dotaz CREATE?

## 7️⃣ Vytvoření databáze

### Zadání

* vytvoř databázi pomocí:

  * **phpMyAdmin** nebo
  * **mysql prompt**,
* importuj vytvořený SQL skript.

### Požadovaný výstup

* screenshot nebo krátký popis postupu,
* potvrzení úspěšného vytvoření tabulek.

### Otázky k zamyšlení
1. Jaký SW resp. služby jsou potřeba k vytvoření relační databáze?
2. Které z nich jsou nezbytné a které pomocné?

## 8️⃣ Naplnění databáze daty

### Zadání

* vytvoř:

  * minimálně **5 serverů**,
  * minimálně **5 služeb**,
  * odpovídající záznamy o nasazení,
* použij:

  * `INSERT` nebo `MULTI INSERT`.

### Požadovaný výstup

* SQL skript s INSERTy

### Otázky k zamyšlení
1. K čemu slouží dota INSERT a jak se liší od multi INSERT?
2. Na co si dávat při vkládání záznamů do DB pozor?
3. Jak zjistím id posledního vloženého záznamu?

## 9️⃣ Základní CRUD dotazy

### Zadání

Vytvoř ukázky:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`

Každý dotaz krátce okomentuj.

### Požadovaný výstup

* SQL skript s okomentovanými dotazy


## 🔟 Složitější dotazy

### Zadání

Vytvoř dotazy, které využívají:

* `JOIN`,
* agregační funkce (`COUNT`, `AVG`, …),
* alespoň jeden **vnořený dotaz** nebo `UNION`.

### Požadovaný výstup

* minimálně 4 složitější SQL dotazy v SQL skriptu se stručným popisem v komentáři,


## Poznámka pro žáky

Zaměř se **na návrh**, ne na objem dat. Důležitá je:

* logika návrhu,
* správná normalizace,
* srozumitelnost dokumentace (markdown soubory a komentáře),
* korektní SQL.

