# Autor: Seu Nome
# Algoritmo que imprime os números de 1 a 100

for i in range(1, 101):  # loop de 1 a 100
    print(i)  # imprime o número atual




# Autor: Seu Nome
# Algoritmo que exibe a tabuada de um número fornecido pelo usuário

numero = int(input("Digite um número para ver sua tabuada: "))  # recebe o número do usuário

for i in range(1, 11):  # loop de 1 a 10
    resultado = numero * i  # calcula o resultado da tabuada
    print(f"{numero} x {i} = {resultado}")  # imprime a tabuada




# Autor: Seu Nome
# Algoritmo que calcula a soma dos números pares de 1 a 50

soma = 0  # inicializa a soma

for i in range(1, 51):  # loop de 1 a 50
    if i % 2 == 0:  # verifica se o número é par
        soma += i  # adiciona o número par à soma

print(f"A soma dos números pares de 1 a 50 é: {soma}")  # imprime a soma total