# Armazenar o nome, sexo e idade de cem pessoas. Consistir as entradas no sentido de aceitar apenas “F” ou “M” para o sexo e valores positivos para a idade. Após a digitação dos dados, exibir os dados (nome, sexo e idade) de todas as pessoas do sexo feminino.

arrayNome = []
arrayIdade = []
arraySexo = []

for i in range (0, 5, 1):
    nome = input("Digite seu nome: ")
    arrayNome.append(nome)

    idade = int(input("Digite a sua idade: "))
    while idade < 0:
        print("A idade deve ser maior que 0")
        idade = int(input("Digite novamente sua idade: "))
    arrayIdade.append(idade)

    sexo = input("Digite seu sexo (m/f): ")
    while sexo != "m" and sexo != "f":
        print("O sexo deve ser 'm' ou 'f'.")
        sexo = input("Digite novamente seu sexo (m/f): ")
    arraySexo.append(sexo)

print("As mulheres cadastradas são: ")

for i in range (0, 5, 1):
    if arraySexo[i] == "f":
        print(f"Nome: {arrayNome[i]}")
        print(f"Idade: {arrayIdade[i]}")
