import jogo_adivinhacao 
import jogo_forca

def escolher_jogo():
    while True:
        print("######### Escolha o seu Jogo! #########")
        print("(1) Adivinhação")
        print("(2) Forca")
        print("(3) Sair")

        try:
            opcao = int(input("Qual jogo? "))

            if opcao == 1:
                print("Jogando Adivinhação...\n")
                jogo_adivinhacao.jogar()
            elif opcao == 2:
                print("Jogando Forca...\n")
                jogo_forca.jogar()
            elif opcao == 3:
                print("Saindo...")
                break 
            else:
                print("Opção inválida! Digite 1, 2 ou 3.\n")
        
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.\n")

if __name__ == "__main__":
    escolher_jogo()
