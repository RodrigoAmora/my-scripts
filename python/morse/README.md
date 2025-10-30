# Morse
Exemplos de uso
---------------
<b>Codificar texto diretamente:</b>
```bash
python morse.py -e -i "Olá mundo 2025!"
```
(vai codificar, mas observe que Ó será convertido para O — acentos não estão no mapa; você pode normalizar antes se quiser)

<b>Decodificar morse:</b>
```bash
python morse.py -d -i "... --- ..."
```

<b>Detectar automaticamente:</b>
```bash
python morse.py --auto -i "... --- ..."
```

<b>Usando pipe:</b>
```bash
echo "sos" | python morse.py (auto detect -> codifica)

echo "... --- ..." | python morse.py --auto (auto detect -> decodifica)
```

<b>Salvar resultado num arquivo:</b>
```bash
python morse.py -e -i "HELLO" -o saida.txt
```
