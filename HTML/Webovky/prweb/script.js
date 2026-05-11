console.log("Hello world! HELLO JS!")
let n = 2
let b = 1
for (;b <= 10;) {
    console.log((n * b))
    b = b* n
}
for (let i = 0; i < 5; i++) {
    console.log(2 ** i)
}
for (let i = 1; i <= 100; i *= 2) {
    console.log(i);
}
let x = 7;
let y = 1;
console.log(x * y)
console.log("součet x a y je: " + (x + y) )


document.write("Toto je výpis pomocí document.write " + (x * y))

const hdr = document.getElementById("hdr");
const btn = document.getElementById("btn");
const numberInput = document.getElementById("NUMBER");
const grid = document.getElementById("grid");

const colors = ["green", "blue", "red"];
let index = 0;

btn.onclick = function() {
    hdr.style.backgroundColor = colors[index];
    index = (index + 1) % colors.length;
};

function createGrid(size) {
    grid.innerHTML = "";

    grid.style.gridTemplateColumns = `repeat(${size}, 30px)`;

    for (let row = 0; row < size; row++) {
        for (let col = 0; col < size; col++) {
            const cell = document.createElement("div");
            cell.className = "cell";

            // šachovnicový vzor – střídání černá/bílá
            if ((row + col) % 2 === 0) {
                cell.classList.add("white");
            } else {
                cell.classList.add("black");
            }

            grid.appendChild(cell);
        }
    }
}
numberInput.addEventListener("input", function () {
    let value = parseInt(numberInput.value, 10);
    if (isNaN(value)) return;

    if (value < 1) value = 1;
    if (value > 16) value = 16;

    createGrid(value);
});

createGrid(parseInt(numberInput.value, 10) || 1);

/*
getelementbyid
dif
style-grid
createelement
appent child
*/