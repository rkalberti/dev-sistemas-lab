# Aula 4 - Arquivos (ler e escrever)


# -------- Lendo arquivo --------

palavras = []

arquivo = open("palavras.txt", "r")  # "r" = modo leitura

for linha in arquivo:
    palavras.append(linha.strip())  # strip() remove o \n (quebra de linha)

arquivo.close()  # fecha o arquivo

print(palavras)



# -------- Explicação rápida --------
# open("arquivo", "r") -> abre para leitura
# linha -> cada linha do arquivo
# strip() -> remove espaços/quebras de linha
# close() -> fecha o arquivo



# Forma melhor (mais segura)
# o arquivo fecha sozinho

palavras = []

with open("palavras.txt", "r") as arquivo:
    for linha in arquivo:
        palavras.append(linha.strip())

print(palavras)



# -------- Escrevendo em arquivo --------


arquivo = open("novo.txt", "w")  # "w" = escrever (apaga o que tinha)

arquivo.write("Olá mundo\n")
arquivo.write("Outra linha\n")

arquivo.close()



# Adicionando conteúdo (sem apagar)

arquivo = open("novo.txt", "a")  # "a" = adicionar

arquivo.write("Mais uma linha\n")

arquivo.close()



# ---- Exemplo prático com lista ----


nomes = ["Ana", "Carlos", "Julia"]

with open("nomes.txt", "w") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")