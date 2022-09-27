#  Armazenar o nome, sexo e idade de cem pessoas. Consistir as entradas no sentido de aceitar apenas “F” ou “M” para o sexo e valores positivos para a idade. Após a digitação, exibir os dados (nome, sexo e idade) de todas as pessoas com idade superior a dezoito anos. Ao final da lista, exibir a quantidade de pessoas listadas.

arrayNome = []
arrayIdade = []
arraySexo = []
soma = 0

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

for i in range (0, 5, 1):
    if arrayIdade[i] > 18:
        print(f"Nome: {arrayNome[i]}")
        print(f"Idade: {arrayIdade[i]}")
        print(f"Idade: {arraySexo[i]}")
        soma += 1
print(f"O total de pessoas listadas foi: {soma}")
