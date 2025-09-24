import base64

def decriptar(texto_cifrado: str, chave: str) -> str:
    texto_cifrado_bytes = base64.b64decode(texto_cifrado)
    texto_claro = []
    for i, c in enumerate(texto_cifrado_bytes):
        k = ord(chave[i % len(chave)])
        dec = (c - k) % 256
        texto_claro.append(dec)

    texto_claro_bytes = bytes(texto_claro)
    return texto_claro_bytes.decode()


input_texto_cifrado = input("Digite o texto a ser decriptado: ")
input_chave = input("Digite a chave de criptografia: ")

print("Texto decriptado:", decriptar(input_texto_cifrado, input_chave))