# Aula 3 - Listas + for + índice


# -------- Lista de opções --------


opcoes = ["Opção 1", "Opção 2", "Opção 3", "Opção 4", "Sair"]


# LISTA (explicação + exemplo)
# Lista guarda vários valores dentro de []

print("Lista completa:", opcoes)

# acessando pelo índice (posição)
print("Primeiro item:", opcoes[0])  # índice 0
print("Segundo item:", opcoes[1])   # índice 1



# FOR (explicação + exemplo)
# for = laço de repetição usado para percorrer listas

print("\nExemplo de FOR:")

for opcao in opcoes:
    print(opcao)

# aqui o for pega cada item da lista automaticamente



# ÍNDICE (explicação + exemplo)
# índice = posição do item na lista (começa em 0)

print("\nExemplo de índice:")

for i in range(len(opcoes)):
    print(f"Posição {i}: {opcoes[i]}")

# i = posição
# opcoes[i] = valor naquela posição




# Menu de opções


while True:
    print("\n1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")
    print("4 - Opção 4")
    print("5 - Sair")

    opcao = int(input("Digite a opção desejada (1 a 4): "))

    if opcao == 1:
        print("Selecionado opção 1")
    elif opcao == 2:
        print("Selecionado opção 2")
    elif opcao == 3:
        print("Selecionado opção 3")
    elif opcao == 4:
        print("Selecionado opção 4")
    elif opcao == 5:
        break
    else:
        print("Opção inválida, digite um número de 1 a 4")