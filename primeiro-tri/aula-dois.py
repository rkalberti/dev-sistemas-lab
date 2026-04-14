# Aula 2 - While (laço de repetição) + Condicionais (if, elif, else)



# -------- O que é o while? --------

# while = laço de repetição
# Ele executa um bloco de código ENQUANTO a condição for verdadeira

contador = 1

while (contador <= 10):
    print(contador)
    contador = contador + 1    # evita loop infinito




# ---- Exemplo - Contagem regressiva ----


contador = 10

while (contador >= 1):
    print(contador)
    contador = contador - 1


# ---- Exemplo - Usando input ----


numero = int(input("Digite um número: "))
contador = 1

while (contador <= numero):
    print(contador)
    contador = contador + 1




# ---- Condicionais (if, elif, else) ----
# Servem para tomar decisões

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# -------- Exemplo com elif --------


nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")




# Misturando while + if (muito importante)


contador = 1

while (contador <= 5):
    
    # verifica se é par ou ímpar
    if contador % 2 == 0:
        print(f"{contador} é par")
    else:
        print(f"{contador} é ímpar")
    
    contador = contador + 1



# ---- Exemplo útil - somando valores ---;


contador = 1
soma = 0

while (contador <= 5):
    soma = soma + contador
    contador = contador + 1

print(f"Soma total: {soma}")