#!/usr/bin/env python3
# morse.py
# Script simples para codificar/decodificar Código Morse
# Autor: gerado por ChatGPT (adaptável)

from typing import Dict, Tuple
import argparse
import sys

# Mapa de texto -> morse
TEXT_TO_MORSE: Dict[str, str] = {
    # letras
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",
    # números
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",
    # sinais de pontuação e alguns símbolos comuns
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "$": "...-..-","@": ".--.-.",
    # espaço será tratada separadamente (palavras)
}

# Inverte o dicionário para morse -> texto
MORSE_TO_TEXT: Dict[str, str] = {v: k for k, v in TEXT_TO_MORSE.items()}

def encode(text: str, sep: str = " ", word_sep: str = " / ") -> str:
    """
    Converte texto para Código Morse.
    - sep: separador entre letras (por padrão ' ')
    - word_sep: separador entre palavras (por padrão ' / ')
    Caracteres desconhecidos são ignorados (podem ser substituídos por '?').
    """
    parts = []
    for word in text.strip().split():
        encoded_letters = []
        for ch in word:
            key = ch.upper()
            if key in TEXT_TO_MORSE:
                encoded_letters.append(TEXT_TO_MORSE[key])
            else:
                # opcional: append '?' para caracter desconhecido
                # encoded_letters.append('?')
                # simplesmente ignora
                pass
        if encoded_letters:
            parts.append(sep.join(encoded_letters))
    return word_sep.join(parts)

def decode(morse: str, sep: str = " ", word_sep: str = "/") -> str:
    """
    Converte Código Morse para texto.
    - sep: separador entre letras no input morse (por padrão ' ')
    - word_sep: separador entre palavras no input morse (por padrão '/')
    Retorna texto em maiúsculas. Caracteres desconhecidos viram '?'.
    """
    words = []
    # normaliza espaçamento: permite tanto ' / ' quanto '/'
    morse = morse.strip()
    # split em palavras por word_sep (considerando espaços extras)
    raw_words = [w.strip() for w in morse.split(word_sep)]
    for raw_word in raw_words:
        if not raw_word:
            continue
        letters = [l for l in raw_word.split(sep) if l != ""]
        decoded_letters = []
        for m in letters:
            if m in MORSE_TO_TEXT:
                decoded_letters.append(MORSE_TO_TEXT[m])
            else:
                decoded_letters.append("?")
        words.append("".join(decoded_letters))
    return " ".join(words)

def detect_input_kind(s: str) -> str:
    """
    Tenta detectar se a string é morse ('.' e '-' predominantes) ou texto normal.
    Retorna 'morse' ou 'text'.
    """
    s = s.strip()
    if not s:
        return "text"
    morse_chars = set(".- /")
    # se todos os caracteres estiverem no conjunto morse (ou muito maioria), considera morse
    non_space = [c for c in s if not c.isspace()]
    if not non_space:
        return "text"
    morse_like = sum(1 for c in non_space if c in ".-/")
    ratio = morse_like / len(non_space)
    return "morse" if ratio >= 0.6 else "text"

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="morse.py", description="Codificador/Decodificador de Código Morse")
    group = p.add_mutually_exclusive_group()
    group.add_argument("-e", "--encode", action="store_true", help="codificar texto para Morse")
    group.add_argument("-d", "--decode", action="store_true", help="decodificar Morse para texto")
    p.add_argument("-i", "--input", type=str, help="texto de entrada (se omitido, lê stdin)")
    p.add_argument("-o", "--output", type=str, help="arquivo para salvar o resultado (se omitido, imprime stdout)")
    p.add_argument("--sep", type=str, default=" ", help="separador entre letras Morse (default: ' ')")
    p.add_argument("--word-sep", type=str, default="/", help="separador entre palavras em Morse (default: '/')")
    p.add_argument("--auto", action="store_true", help="detectar automaticamente se entrada é texto ou morse")
    return p

def main(argv: Tuple[str, ...] = None):
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    # leitura da entrada
    if args.input:
        src = args.input
    else:
        # ler stdin
        if sys.stdin.isatty():
            # sem stdin piped e sem --input: mostrar uso curto
            parser.print_help()
            return
        src = sys.stdin.read()

    operation = None
    if args.encode:
        operation = "encode"
    elif args.decode:
        operation = "decode"
    elif args.auto:
        kind = detect_input_kind(src)
        operation = "decode" if kind == "morse" else "encode"
    else:
        # padrão: se houver apenas pontos/traços -> decode, senão encode
        operation = "decode" if detect_input_kind(src) == "morse" else "encode"

    if operation == "encode":
        result = encode(src, sep=args.sep, word_sep=(" " + args.word_sep + " ") if args.word_sep.strip() else args.word_sep)
    else:
        # para decode, garantir que word_sep no parser seja usado como delimitação simples
        result = decode(src, sep=args.sep, word_sep=args.word_sep)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
    else:
        print(result)

if __name__ == "__main__":
    main()
