# Armazenar vinte valores na memória. Após a digitação, entrar com uma constante multiplicativa que deverá multiplicar cada um dos valores do vetor e armazenar o resultado em outro vetor, porém em posições equivalentes. Exibir os vetores na tela.

numeros = []
novo = []

for i in range(0, 5, 1):
    x = int(input("Digite um número: "))
    numeros.append(x)

multi = int(input("Digite por quanto você quer multiplicar esses números: "))

for i in range(0, 5, 1):
   novo.append(numeros[i] * multi)

print(f"Seu array era {numeros} e seu novo array é: {novo}")