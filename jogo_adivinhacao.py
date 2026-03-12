import random

tentativasMax = 3
tentativas = 1
errou = True

while True:
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    opcao = int(input("Digite a sua opção (1 a 3): "))

    if opcao == 1:
        sorteio_max = 10
        break
    elif opcao == 2:
        sorteio_max = 15
        break
    elif opcao == 3:
        sorteio_max = 20
        break
    else:
        print("Opção inválida, digite um número de 1 a 3")

numero = random.randint(0, sorteio_max)

while tentativas <= tentativasMax:
    print("Tentativa:", tentativas)
    chute = int(input(f"Digite o seu chute (0 a {sorteio_max}): "))

    if chute == numero:
        print("Parabéns, você é o bonzão mesmo")
        errou = False
        break
    else:
        print("Errou :c")

        if chute < numero:
            print("O número é maior")
        else:
            print("O número é menor")

    tentativas = tentativas + 1

if errou == True:
    print("O número sorteado era:", numero)

print("### FIM DO JOGO ###")