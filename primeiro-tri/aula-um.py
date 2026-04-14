#Aula 1, print e variáveis!

print("Olá Mundo!")

#variaveis 
nome = "Ketlyn"      # str -> texto (string) 
idade = 16           # int -> número inteiro
altura = 1.55        # float -> número decimal
estudando = True     # bool -> true or false 


# Usar o print com variáveis:
print("Olá, meu nome é", nome, ", minha idade é", idade)

# F-Strings (forma mais moderna e organizada)
print(f'Olá, meu nome é {nome}, minha idade é {idade}')



# -------- Tipos de dados (type) --------


# Mostra o tipo de cada variável
print(type(nome))
print(type(idade))
print(type(altura))

# Forma mais explicativa
print(f"O tipo da variável 'nome' é: {type(nome)}")
print(f"O tipo da variável 'idade' é: {type(idade)}")
print(f"O tipo da variável 'altura' é: {type(altura)}")



# -------- Entrada de dados (input) --------


nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}!")

print(f"O tipo do nome digitado é: {type(nome_usuario)}")




# -------- Conversão de tipos --------

idade_usuario = int(input("Digite sua idade: "))  # converte para inteiro
print(f"Você tem {idade_usuario} anos")

print(f"O tipo da idade agora é: {type(idade_usuario)}")




# -------- Operações básicas --------

num1 = 10
num2 = 5

print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2}")



# -------- Strings --------


print(nome.upper())  # tudo maiúsculo
print(nome.lower())  # tudo minúsculo
print(len(nome))     # quantidade de letras