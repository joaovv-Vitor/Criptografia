# C representa o caractere cifrado
#P é o caractere claro.
#K é a chave de criptografia.

# p = input("Digite o caractere Claro: ")
# k = input("Digite a chave de criptografia: ")

#c = p + k (mod 256)
#c = (p + k) % 256


# c = (ord(p) + ord(k)) % 256
# c = chr(c)


# for i in range(len(p)):
#     c = (ord(p[i]) + ord(k[i % len(k)])) % 256
#     c = chr(c)


# print("O caractere cifrado é: ", c)


import base64

def criptar(texto_claro: str, chave: str) -> str:
    texto_cifrado = []
    for i, c in enumerate(texto_claro):
        p = ord(c)
        k = ord(chave[i % len(chave)])
        enc = (p + k) % 256
        texto_cifrado.append(enc)

    texto_cifrado_bytes = bytes(texto_cifrado)
    return base64.b64encode(texto_cifrado_bytes).decode()


input_texto_claro = input("Digite o texto a ser cifrado: ")
input_chave = input("Digite a chave de criptografia: ")                                 

print("Texto cifrado:", criptar(input_texto_claro, input_chave))

