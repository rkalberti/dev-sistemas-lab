# ANOTAÇÕES - PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)


# 1. Criar a classe
# 2. Fazer o __init__
# 3. Criar os atributos privados (__)
# 4. Criar os getters
# 5. Criar os métodos pedidos
# 6. Criar o arquivo teste.py
# 7. Importar a classe
# 8. Criar o objeto
# 9. Chamar os métodos
# 10. Executar:
#
# python3 teste.py



# CLASSE
# Classe = modelo/molde para criar objetos.

class Pessoa:
    pass


# OBJETO
# Um objeto é criado a partir da classe.

pessoa1 = Pessoa()


# CONSTRUTOR (__init__)
# O construtor é executado automaticamente quando criamos um objeto.

class Aluno:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade


aluno1 = Aluno("Ketlyn", 16)




# SELF
# self representa o próprio objeto.

# aluno1.__nome
# aluno1.__idade

# são armazenados como:

# self.__nome
# self.__idade



# ATRIBUTOS PRIVADOS
# Dois underlines (__) deixam o atributo privado.

class Produto:

    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco




# GETTER (@property)
# Getter = LER um atributo privado.

class Livro:

    def __init__(self, titulo):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo


livro = Livro("Carmilla")

print(livro.titulo)

# ERRADO
# print(livro.__titulo)





# SETTER
# Setter = ALTERAR um atributo privado.

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


animal = Animal("Rex")

animal.nome = "Thor"

print(animal.nome)





# MÉTODOS
# Métodos = funções da classe.

class Carro:

    def __init__(self, modelo):
        self.__modelo = modelo

    def mostrar(self):
        print(self.__modelo)


carro = Carro("Fusca")

carro.mostrar()



# IF
class Quarto:

    def __init__(self):
        self.__disponivel = True

    def reservar(self):

        if self.__disponivel:
            self.__disponivel = False
            print("Reservado")

        else:
            print("Já está ocupado")



# Arquivo: quarto.py
# Importação:  from quarto import Quarto




# ARQUIVO TESTE - teste.py

from quarto import Quarto

quarto1 = Quarto(101, "Casal", 200)

quarto1.exibir_detalhes()
quarto1.reservar()
quarto1.liberar()
