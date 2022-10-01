# lterar o programa anterior, no sentido de controlar o layout final de tela, para que o usuário pressione uma tecla para visualizar os dados das pessoas passo a passo, por exemplo, de dez em dez pessoas.

arrayNome = []
arrayIdade = []
arraySexo = []
soma = 0

for i in range (0, 100, 1):
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
    
for i in range (0, 100, 1):
    if arrayIdade[i] > 18:
        print(f"Nome: {arrayNome[i]}")
        print(f"Idade: {arrayIdade[i]}")
        print(f"Idade: {arraySexo[i]}")
        soma += 1
print(f"Existem {soma} maiores de 18 anos.")