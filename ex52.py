# Armazenar dez valores na memória do computador. Após a digitação dos valores, criar uma rotina para ler os valores e achar e exibir o maior deles.

numeros = []

for i in range(0, 10, 1):
    x = int(input("Digite um número: "))
    numeros.append(x)
    
maior = numeros[0]

for i in range(0, 10, 1):
    if numeros[i] > maior:
        maior = numeros[i]

print(f"O maior valor é o {maior}")



