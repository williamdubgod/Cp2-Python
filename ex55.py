# Armazenar um máximo de 20 valores em um vetor. A quantidade de valores a serem armazenados será escolhida pelo usuário. Enviar mensagem de erro, caso a quantidade de valores escolhida esteja fora da faixa possível e solicitar a quantidade novamente. Após a digitação dos valores, criar uma rotina de consulta, onde o usuário digita um número e o programa exibe em qual posição do vetor este número está localizado. Se o número não for encontrado, enviar mensagem “Valor não encontrado!”. Perguntar ao usuário se deseja ou não fazer uma nova consulta, consistir a resposta e encerrar o programa em caso negativo.

numeros = []
pos = -1
novamente = 's'

qtdValores = int(input("Digite a quantidade de valores que dejesa adicionar: "))

while qtdValores > 20 or qtdValores <= 0:
    print("Você pode adicionar de 1 a 20 valores!")
    qtdValores = int(input("Digite a quantidade de valores que dejesa adicionar: "))

for i in range(0, qtdValores, 1):
    x = int(input("Digite um número: "))
    numeros.append(x)

while novamente == "s":
    posicao = int(input("Digite o numero que queira saber a posição: "))

    for i in range(0, qtdValores, 1):
        if numeros[i] == posicao:
            pos = i

    if pos != -1:     
        print(f"Esse número está na posição: {pos}")
    else:
        print("Valor não encontrado!")

    novamente = input("Dejesa realizar uma nova consulta? (s/n): ")

print("Obrigado!")





        
        
    
        

    


