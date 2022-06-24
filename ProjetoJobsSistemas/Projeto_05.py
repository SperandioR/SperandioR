# Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;



texto = input("Digite um texto para inverter: ")
textoInvertido = []
char = len(texto)-1

for i in texto:
    textoInvertido.append(texto[char])
    char -= 1

print("".join(textoInvertido))