# Armazenar vinte valores em um vetor. Após a digitação, exibir os valores em ordem crescente.

array = []

for i in range(0, 5, 1):
    v = int(input("Digite um valor: "))
    array.append(v)
print(sorted(array))




