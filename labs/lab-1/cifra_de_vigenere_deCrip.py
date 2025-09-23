def decriptar(texto_encriptado, chave):
    texto_claro = []
    for i, c in enumerate(texto_encriptado):
        p = ord(c)
        k = ord(chave[i % len(chave)])
        dec = (p - k) % 256
        texto_claro.append(chr(dec))
    return "".join(texto_claro)


input_texto_cifrado = input("Digite o texto a ser decifrado: ")
input_chave = input("Digite a chave de criptografia: ")

print("Texto decifrado:", decriptar(input_texto_cifrado, input_chave))
