let pocet = 24;

document.querySelectorAll('div').forEach(div => {
  div.addEventListener('click', () => {
    pocet=pocet-1;
    document.getElementById('PT').textContent = pocet;
  });
});