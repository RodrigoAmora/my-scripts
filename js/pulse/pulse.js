function pulse(mensagens) {
  let i = 0;
  setInterval(() => {
    document.getElementById("letreiro").textContent = mensagens[i];
    i = (i + 1) % mensagens.length;
  }, 3000);
}