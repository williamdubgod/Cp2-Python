# Armazenar vinte valores em um vetor. Após a digitação, entrar com uma constante multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o resultado no próprio vetor, na respectiva posição.

numeros = []

for i in range(0, 20, 1):
    x = int(input("Digite um número: "))
    numeros.append(x)

multi = int(input("Por quanto você quer multiplicar esses números: "))

for i in range(0, 20, 1):
    numeros[i] = numeros[i] * multi

print(f"Seu array ficou assim: {numeros}")


       