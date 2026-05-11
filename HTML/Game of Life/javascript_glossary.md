# Slovníček použitých prvků v JavaScriptu

Tento dokument vysvětluje obecný význam příkazů a klíčových slov, které jsme použili v kódu pro Game of Life.

## Proměnné a Konstanty

### const
`const` slouží k deklarování konstant. Typicky jde o důležité hodnoty, které se **nemají nikdy měnit** během běhu programu (např. nastavení, pevné počty, neměnné odkazy na HTML prvky).
*   *Příklad*: `const pi = 3.14;` (Hodnota pí se nezmění).

### let
`let` slouží k deklarování proměnných, jejichž hodnota se **bude měnit**. Používáme ho pro počítadla, přepínače stavů nebo dočasné hodnoty.
*   *Příklad*: `let skore = 0;` (Skóre se bude v průběhu hry zvyšovat).

## Funkce a Logika

### function
`function` definuje blok kódu (podprogram), který má jméno a můžeme ho kdykoliv spustit (zavolat). Funkce pomáhají organizovat kód do logických celků.
*   *Příklad*: `function pozdrav() { console.log("Ahoj!"); }`

### if / else if
`if` je podmínka. Říká: "Pokud je toto pravda, udělej X". `else if` říká: "Jinak, pokud je pravda toto, udělej Y".
*   *Příklad*: `if (vek >= 18) { console.log("Dospělý"); }`

### return
`return` okamžitě ukončí bežící funkci a volitelně vrátí nějakou hodnotu zpět tomu, kdo funkci zavolal.
*   *Příklad*: `function secti(a, b) { return a + b; }`

### for (cyklus)
`for` slouží k opakování kusu kódu. Typicky se používá, když víme, kolikrát chceme něco udělat (např. projít všech 32 řádků).
*   *Příklad*: `for (let i = 0; i < 10; i++) { ... }` (Opakuj 10x).

### ? : (Ternární operátor)
Zkrácený zápis podmínky `if/else`. Má formát: `podmínka ? hodnota_při_pravdě : hodnota_při_nepravdě`.
*   *Příklad*: `let stav = (vek >= 18) ? "Dospělý" : "Dítě";`

## Práce s HTML (DOM)

### document.getElementById()
Najde v HTML stránce **jeden** konkrétní prvek, který má zadané [id](file:///c:/Users/pelcs/OneDrive%20-%20VO%C5%A0,%20SP%C5%A0%20a%20SO%C5%A0,%20Varnsdorf,%20p.o/HTML-tutorial/Game%20of%20Life/javascript.js#38-82). Je to nejrychlejší způsob, jak "chytit" prvek do JavaScriptu.
*   *Příklad*: `const tlacitko = document.getElementById('moje-tlacitko');`

### document.querySelector() / querySelectorAll()
Univerzálnější hledání prvků pomocí CSS selektorů (např. podle třídy `.trida`). `querySelectorAll` najde všechny výskyty.
*   *Příklad*: `const vsechnyBunky = document.querySelectorAll('.cell');`

### document.createElement()
Vytvoří v paměti nový, čistý HTML prvek (zatím není na stránce vidět). Musíme ho někam vložit pomocí `appendChild`.
*   *Příklad*: `const novyDiv = document.createElement('div');`

### element.appendChild()
Vezme prvek vytvořený v paměti a vloží ho "dovnitř" jiného prvku na stránce (jako poslední dítě).
*   *Příklad*: `rodic.appendChild(dite);`

### element.innerHTML
Vlastnost, která obsahuje veškerý HTML obsah uvnitř prvku. Často se používá prázdný řetězec `''` k vymazání obsahu prvku.
*   *Příklad*: `kontejner.innerHTML = '';` (Smaže vše uvnitř).

### element.classList.add() / .remove()
Přidává nebo odebírá CSS třídy danému prvku. Tím můžeme měnit vzhled prvku za běhu (např. rozsvítit buňku).
*   *Příklad*: `bunka.classList.add('ziva');`

### element.dataset
Umožňuje číst a zapisovat vlastní data do HTML atributů (např. `data-row="5"`). V JS k nim přistupujeme jako `element.dataset.row`.
*   *Příklad*: `bunka.dataset.id = 123;`

### element.addEventListener()
"Posluchač". Čeká na určitou událost (např. 'click') na daném prvku a když nastane, spustí zadanou funkci.
*   *Příklad*: `tlacitko.addEventListener('click', spustHru);`

## Časování

### setInterval()
Spouští zadanou funkci **opakovaně** v pravidelných intervalech (v milisekundách). Vrací ID, které potřebujeme pro zastavení.
*   *Příklad*: `setInterval(tikTak, 1000);` (Každou sekundu).

### clearInterval()
Zastaví opakování nastavené pomocí `setInterval`.
*   *Příklad*: `clearInterval(idCasovace);`

## Pole (Arrays)

### .push()
Přidá novou položku na **konec** pole.
*   *Příklad*: `batoh.push('Svačina');`

### .map()
Vytvoří **nové pole** tak, že vezme každou položku ze starého pole a něco s ní udělá (nebo ji zkopíruje). V kódu jsme to použili pro vytvoření kopie mřížky.
*   *Příklad*: `const cisla = [1, 2]; const dvojnasobky = cisla.map(x => x * 2);`
