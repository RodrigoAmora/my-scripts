<?php
$ano = date("Y");
$cont = 0;
$dia = date("d");
$dias = array();
$mes = date("m");
$totalDias = date("t");
$primeiroDia = date("D", mktime(0, 0, 0, $mes, 1, $ano));

for($d = 0; $d < $totalDias; $d++)$dias[$d] = array_push($dias, $d+1);

switch($primeiroDia){
	case "Sun":
		$pos = 0;
	break;

	case "Mon":
		$pos = 1;
	break;

	case "Tue":
		$pos = 2;
	break;

	case "Wed":
		$pos = 3;
	break;

	case "Thu":
		$pos = 4;
	break;

	case "Fri":
		$pos = 5;
	break;

	case "Sat":
		$pos = 6;
	break;
}//Fim do switch

switch($mes){
	case 1:
		$mes2 = "Janeiro";
	break;

	case 2:
		$mes2 = "Fevereiro";
	break;

	case 3:
		$mes2 = "Março";
	break;

	case 4:
		$mes2 = "Abril";
	break;

	case 5:
		$mes2 = "Maio";
	break;

	case 6:
		$mes2 = "Junho";
	break;

	case 7:
		$mes2 = "Julho";
	break;

	case 8:
		$mes2 = "Agosto";
	break;

	case 9:
		$mes2 = "Setembro";
	break;

	case 10:
		$mes2 = "Outubro";
	break;

	case 11:
		$mes2 = "Novembro";
	break;

	case 12:
		$mes2 = "Dezembro";
	break;
}//Fim do switch

echo "<table border=0 cellspacing=0 cellpadding=0>";
echo "<tr><td bgColor='gray' colspan=7><center><b>$mes2/$ano</b></center></td></tr>";
echo "<tr><td>D</td><td>S</td><td>T</td><td>Q</td><td>Q</td><td>S</td><td>S</td></tr>";

for($linha = 0; $linha < 6; $linha++){
	echo "</tr>";
	for($coluna = 0; $coluna < 7; $coluna++){
		$pos2 = $cont - $pos;

		if(empty($dias[$pos2]))echo "<td><center>-</center></td>";
		else{
			if($dias[$pos2] == $dia)print_r ("<td bgColor='darkgray'><b><center><font color='blue'>".$dias[$pos2]."</font></center></b></td>");
			else print_r ("<td><center>".$dias[$pos2]."</center></td>");
		}//Fim do else

		$cont++;
	}//Fim do for
	echo "</tr>";
}//Fim do for

echo "</table>";
?>