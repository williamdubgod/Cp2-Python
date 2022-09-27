# Armazenar o nome e idade de cem pessoas. Após a digitação, exibir os dados (nome e idade) de todas as pessoas.

arrayNome = []
arrayIdade = []

for i in range (0, 5, 1):
    nome = input("Digite seu nome: ")
    arrayNome.append(nome)
    idade = int(input("Digite a sua idade: "))
    arrayIdade.append(idade)
    
for i in range (0, 5, 1):
    print(f"Nome: {arrayNome[i]}")
    print(f"Idade: {arrayIdade[i]}")

    
