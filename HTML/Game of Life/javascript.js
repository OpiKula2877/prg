/**
 * HRA ŽIVOTA (GAME OF LIFE) - vysvětlení kódu
 * 
 * Tento soubor obsahuje veškerou logiku pro naši hru.
 * Javascript zde funguje jako "mozek", který rozhoduje, která buňka přežije a která zemře.
 */

// --- 1. NASTAVENÍ A PROMĚNNÉ ---

// Velikost naší mřížky. Máme 32 řádků a 32 sloupců.
const rows = 32; 
const cols = 32;

// 'grid' je naše hlavní paměť. Bude to pole polí (2D pole), 
// které uchovává stav každé buňky (0 = mrtvá, 1 = živá).
let grid = []; 

// 'intervalId' slouží k uložení ID našeho časovače. 
// Potřebujeme ho, abychom mohli hru později zastavit (clearInterval).
let intervalId = null; 

// 'isRunning' nám říká, jestli hra zrovna běží, nebo stojí.
let isRunning = false; 

// Počítadlo generací, abychom věděli, kolik kol už proběhlo.
let generation = 0;

// Zde si "chytáme" prvky z HTML stránky, abychom s nimi mohli pracovat.
// document.getElementById najde prvek podle jeho ID v HTML.
const gridElement = document.getElementById('grid'); // Kontejner pro mřížku
const startBtn = document.getElementById('start-btn'); // Tlačítko Start
const resetBtn = document.getElementById('reset-btn'); // Tlačítko Reset
const generationCount = document.getElementById('generation-count'); // Text s číslem generace


// --- 2. FUNKCE PRO VYTVOŘENÍ MŘÍŽKY ---

/**
 * Funkce createGrid()
 * Tato funkce se spustí na začátku. Jejím úkolem je:
 * 1. Vyčistit starou mřížku (pokud existuje).
 * 2. Vytvořit nové HTML čtverečky (divy) pro každou buňku.
 * 3. Připravit naše pole 'grid' plné nul (mrtvých buněk).
 */
function createGrid() {
    // Nejdřív vymažeme vše, co je uvnitř elementu #grid v HTML.
    gridElement.innerHTML = '';
    
    // Vyresetujeme naše pole grid na prázdné pole.
    grid = [];

    // První cyklus: Jdeme řádek po řádku (i = 0 až 31).
    for (let i = 0; i < rows; i++) {
        let row = []; // Vytvoříme prázdný řádek pro naše data.

        // Druhý cyklus: V každém řádku jdeme sloupec po sloupci (j = 0 až 31).
        for (let j = 0; j < cols; j++) {
            // Vytvoříme nový HTML prvek <div>. To bude jedna buňka na obrazovce.
            const cell = document.createElement('div');
            
            // Přidáme mu třídu 'cell', aby vypadal jako čtvereček (podle CSS).
            cell.classList.add('cell');
            
            // Uložíme si do něj souřadnice, abychom při kliknutí věděli, kde jsme.
            cell.dataset.row = i;
            cell.dataset.col = j;
            
            // Přidáme "posluchač událostí" (EventListener). 
            // Říkáme: "Když na tebe někdo klikne, spusť funkci toggleCell se souřadnicemi i, j".
            cell.addEventListener('click', () => toggleCell(i, j));
            
            // Přidáme hotový čtvereček do stránky (do elementu #grid).
            gridElement.appendChild(cell);
            
            // Do našeho datového pole přidáme 0 (mrtvá buňka).
            row.push(0); 
        }
        // Až máme celý řádek hotový, přidáme ho do hlavního pole grid.
        grid.push(row);
    }
}


// --- 3. INTERAKCE S UŽIVATELEM ---

/**
 * Funkce toggleCell(r, c)
 * Spustí se, když uživatel klikne na buňku.
 * r = číslo řádku, c = číslo sloupce.
 */
function toggleCell(r, c) {
    // Pokud hra běží, zakážeme klikání, aby se nám nerozbily výpočty.
    if (isRunning) return; 
    
    // Změníme stav buňky v našem poli.
    // Pokud je 1 (živá), změní se na 0 (mrtvá). Pokud je 0, změní se na 1.
    // Tomuhle se říká "ternární operátor" (zkrácená podmínka if/else).
    grid[r][c] = grid[r][c] ? 0 : 1;
    
    // Po změně dat musíme aktualizovat i vzhled na obrazovce.
    updateUI();
}

/**
 * Funkce updateUI()
 * Tato funkce se podívá na naše data (pole grid) a podle toho obarví buňky na obrazovce.
 */
function updateUI() {
    // Najdeme všechny čtverečky (elementy s třídou .cell) na stránce.
    const cells = document.querySelectorAll('.cell');
    let index = 0; // Pomocné počítadlo, abychom věděli, u kterého divu zrovna jsme.

    // Projdeme celou naši mřížku data...
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            // Pokud je v datech 1 (živá)...
            if (grid[i][j] === 1) {
                // ...přidáme HTML elementu třídu 'alive' (změní barvu na zelenou).
                cells[index].classList.add('alive');
            } else {
                // ...jinak třídu 'alive' odebereme (bude šedá).
                cells[index].classList.remove('alive');
            }
            index++; // Posuneme se na další div v pořadí.
        }
    }
    // Nakonec aktualizujeme číslo generace v patičce stránky.
    generationCount.innerText = generation;
}


// --- 4. LOGIKA HRY (VÝPOČTY) ---

/**
 * Funkce countNeighbors(r, c)
 * Zjistí, kolik má buňka živých sousedů.
 * Prohledává 8 okolních políček kolem souřadnic [r, c].
 */
function countNeighbors(r, c) {
    let count = 0; // Tady budeme sčítat živé sousedy.

    // Procházíme řádky od -1 (nad námi) do +1 (pod námi).
    for (let i = -1; i <= 1; i++) {
        // Procházíme sloupce od -1 (vlevo) do +1 (vpravo).
        for (let j = -1; j <= 1; j++) {
            // Pokud je i=0 a j=0, jsme to my sami -> přeskočit (break/continue).
            if (i === 0 && j === 0) continue;
            
            // Vypočítáme souřadnice souseda.
            const nr = r + i; // Neighbor Row (řádek souseda)
            const nc = c + j; // Neighbor Col (sloupec souseda)
            
            // Důležitá kontrola: Jsme stále uvnitř mřížky?
            // Nesmíme kontrolovat řádek -1 nebo řádek 32, protože neexistují.
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                // Přičteme hodnotu souseda (0 nebo 1) k celkovému počtu.
                count += grid[nr][nc];
            }
        }
    }
    return count; // Vrátíme výsledný počet sousedů.
}

/**
 * Funkce nextGeneration()
 * Hlavní mozek hry. Vypočítá, jak bude vypadat další kolo.
 */
function nextGeneration() {
    // Vytvoříme KOPII naší mřížky (newGrid).
    // Důvod: Kdybychom měnili buňky rovnou v 'grid', ovlivnilo by to výpočet 
    // pro jejich sousedy v tom samém kole. Změny se musí stát "najednou".
    const newGrid = grid.map(arr => [...arr]); 

    // Projdeme každou buňku v mřížce...
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            const alive = grid[i][j];       // Je buňka teď živá? (1 nebo 0)
            const neighbors = countNeighbors(i, j); // Kolik má sousedů?

            // --- ZDE JSOU PRAVIDLA HRY ---
            
            // PRAVIDLO 1 & 3: Úmrtí
            // Pokud je živá A (má méně než 2 sousedy NEBO více než 3) -> zemře.
            if (alive === 1 && (neighbors < 2 || neighbors > 3)) {
                newGrid[i][j] = 0; 
            } 
            // PRAVIDLO 4: Zrození
            // Pokud je mrtvá A má přesně 3 sousedy -> oživne.
            else if (alive === 0 && neighbors === 3) {
                newGrid[i][j] = 1; 
            }
            // PRAVIDLO 2: Přežití
            // Buňka se 2 nebo 3 sousedy žije dál. (Tady nemusíme dělat nic, 
            // protože v kopii newGrid už hodnota 1 je).
        }
    }

    // Až máme vše vypočítané, přepíšeme starou mřížku tou novou.
    grid = newGrid;
    generation++; // Zvýšíme číslo generace.
    updateUI();   // Překreslíme obrazovku.
}


// --- 5. OVLÁDÁNÍ HRY ---

/**
 * Funkce toggleGame()
 * Spustí nebo zastaví simulaci.
 */
function toggleGame() {
    if (isRunning) {
        // Pokud hra běží -> zastavit.
        clearInterval(intervalId); // Zruší pravidelné opakování (timer).
        startBtn.innerText = 'Start'; // Změní nápis na tlačítku.
        isRunning = false;
    } else {
        // Pokud hra stojí -> spustit.
        // setInterval říká: "Spouštěj funkci nextGeneration každých 1000 ms (1 sekunda)".
        intervalId = setInterval(nextGeneration, 1000); 
        startBtn.innerText = 'Stop';
        isRunning = true;
    }
}

/**
 * Funkce resetGame()
 * Vrátí vše do původního stavu.
 */
function resetGame() {
    // Nejdřív zastavíme hru, kdyby náhodou běžela.
    clearInterval(intervalId);
    isRunning = false;
    startBtn.innerText = 'Start';
    
    // Vynulujeme generace.
    generation = 0;
    
    // Znovu vytvoříme mřížku (tím se vymažou všechny živé buňky).
    createGrid(); 
    
    // Aktualizujeme vzhled (vymažeme zelenou barvu).
    updateUI();
    
    // Aktualizujeme číslo generace na 0.
    generationCount.innerText = 0;
}

// Přidáme posluchače na tlačítka, aby reagovala na kliknutí.
startBtn.addEventListener('click', toggleGame);
resetBtn.addEventListener('click', resetGame);

// Na úplném konci skriptu zavoláme createGrid(), aby se mřížka objevila hned po načtení stránky.
createGrid();
