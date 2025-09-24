import base64

def decriptar(texto_cifrado: str, chave: str) -> str:
    texto_cifrado_bytes = base64.b64decode(texto_cifrado)
    chave_bytes = chave.encode("utf-8")

    texto_claro = []
    for i, c in enumerate(texto_cifrado_bytes):
        k = chave_bytes[i % len(chave_bytes)]
        dec = (c - k) % 256
        texto_claro.append(dec)

    texto_claro_bytes = bytes(texto_claro)
    return texto_claro_bytes.decode("utf-8")  



input_texto_cifrado = input("Digite o texto a ser decriptado: ")
input_chave = input("Digite a chave de criptografia: ")

print("Texto decriptado:", decriptar(input_texto_cifrado, input_chave))
