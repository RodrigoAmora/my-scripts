function gerarCalendario() {
  const hoje = new Date();
  const ano = hoje.getFullYear();
  const diaAtual = hoje.getDate();
  const mes = hoje.getMonth(); // 0-11

  // Array com nomes dos meses em PT-BR
  const meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
  ];

  // Dias do mês atual
  const totalDias = new Date(ano, mes + 1, 0).getDate();

  // Descobre o primeiro dia da semana (0=Domingo, 1=Segunda, ..., 6=Sábado)
  const primeiroDia = new Date(ano, mes, 1).getDay();

  let dias = [];
  for (let d = 1; d <= totalDias; d++) {
    dias.push(d);
  }

  // Criação da tabela
  let tabela = "<table border='0' cellspacing='5' cellpadding='0'>";
  tabela += `<tr><td colspan='7' bgcolor='gray'><center><b>${meses[mes]}/${ano}</b></center></td></tr>`;
  tabela += "<tr><td>D</td><td>S</td><td>T</td><td>Q</td><td>Q</td><td>S</td><td>S</td></tr>";

  let cont = 0;

  for (let linha = 0; linha < 6; linha++) {
    tabela += "<tr>";
    for (let coluna = 0; coluna < 7; coluna++) {
      let pos2 = cont - primeiroDia;

      if (pos2 < 0 || dias[pos2] === undefined) {
        tabela += "<td><center>-</center></td>";
      } else {
        if (dias[pos2] === diaAtual) {
          tabela += `<td bgcolor='darkgray'><b><center><font color='blue'>${dias[pos2]}</font></center></b></td>`;
        } else {
          tabela += `<td><center>${dias[pos2]}</center></td>`;
        }
      }
      cont++;
    }
    tabela += "</tr>";
  }

  tabela += "</table>";
  return tabela;
}

// Exemplo de uso -> insere no body
document.body.innerHTML = gerarCalendario();
