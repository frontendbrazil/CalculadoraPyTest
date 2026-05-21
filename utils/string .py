def inverter(texto: str) -> str:
    return texto[::-1]

def contar_vogais(texto: str) -> int:
    return sum(1 for c in texto.lower() if c in "aeiou")

def e_palindromo (texto: str) -> bool:
    limpo = texto.lower().replace(" ", "")
    return limpo == limpo[::-1]

def truncar(texto: str, limite: int) -> str:
    return texto[:limite] + ("..." if len(texto) > limite else texto)