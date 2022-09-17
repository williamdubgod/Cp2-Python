#  Armazenar dez números na memória do computador. Exibir os valores na ordem inversa à da digitação.

numeros = []

for i in range(0, 10, 1):
    x = int(input("Digite um número: "))
    numeros.append(x)

print("Os números que você digitou foram: ")

for i in range(9, -1, -1):
    print(numeros[i])