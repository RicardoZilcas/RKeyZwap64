import base64

# Diccionario explícito de codificación: solo MAYÚSCULAS → símbolo único
codificacion = {
    'A': '!', 'B': '"', 'C': '#', 'D': '$', 'E': '%', 'F': '&',
    'G': "'", 'H': '(', 'I': ')', 'J': '*', 'K': ',', 'L': '-',
    'M': '.', 'N': ':', 'O': ';', 'P': '<', 'Q': '>', 'R': '?',
    'S': '@', 'T': '[', 'U': '\\', 'V': ']', 'W': '^', 'X': '_',
    'Y': '`', 'Z': '{',
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9',
    '+': '+', '/': '/', '=': '=', ' ': ' '
}

# Diccionario explícito de decodificación: símbolo → letra MAYÚSCULA
decodificacion = {
    '!': 'A', '"': 'B', '#': 'C', '$': 'D', '%': 'E', '&': 'F',
    "'": 'G', '(': 'H', ')': 'I', '*': 'J', ',': 'K', '-': 'L',
    '.': 'M', ':': 'N', ';': 'O', '<': 'P', '>': 'Q', '?': 'R',
    '@': 'S', '[': 'T', '\\': 'U', ']': 'V', '^': 'W', '_': 'X',
    '`': 'Y', '{': 'Z',
    '0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9',
    '+': '+', '/': '/', '=': '=', ' ': ' '
}

def codificar_simqwerty(texto_b64):
    return ''.join(codificacion.get(c, c) for c in texto_b64)

def decodificar_simqwerty(texto):
    return ''.join(decodificacion.get(c, c) for c in texto)

def cifrar_doble(texto):
    texto_mayus = texto.upper()
    print(f"🔡 Texto convertido a MAYÚSCULAS: {texto_mayus}")
    b64 = base64.b64encode(texto_mayus.encode('utf-8')).decode('utf-8')
    print(f"🔐 Texto en Base64: {b64}")
    simbolos = codificar_simqwerty(b64)
    print(f"🔏 Texto cifrado con símbolos: {simbolos}")
    return simbolos

def descifrar_doble(texto_cifrado):
    simbolos = decodificar_simqwerty(texto_cifrado)
    print(f"🔍 Texto con símbolos decodificados (Base64): {simbolos}")
    try:
        texto = base64.b64decode(simbolos.encode('utf-8')).decode('utf-8')
        return texto
    except Exception as e:
        return f"❌ Error al decodificar Base64: {e}"
