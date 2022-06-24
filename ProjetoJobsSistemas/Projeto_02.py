num = int(input("Digite um número para verificar se este pertence a uma sequência do fibonacci: "))
a, b = 0, 1
fibonacci = []
while a <= num:
        fibonacci.append(a)
        a, b = b, a+b

print(fibonacci)

if (num in fibonacci):
    print("O número pertence a sequência Fibonacci")
else:
    print("O número NÃO pertence a sequência Fibonacci")