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


def encriptar(texto_claro, chave):
    texto_encriptado = []
    for i, c in enumerate(texto_claro):
        p = ord(c)
        k = ord(chave[i % len(chave)])
        cifra = (p + k) % 256
        texto_encriptado.append(chr(cifra))
    return "".join(texto_encriptado)
input_texto_claro = input("Digite o texto a ser cifrado: ")
input_chave = input("Digite a chave de criptografia: ")

print("Texto cifrado:", encriptar(input_texto_claro, input_chave))
