texto = input("Digite um texto para inverter: ")
textoInvertido = []
char = len(texto)-1

for i in texto:
    textoInvertido.append(texto[char])
    char -= 1

print("".join(textoInvertido))