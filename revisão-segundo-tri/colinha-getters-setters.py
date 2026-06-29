# EXEMPLO DE GETTER E SETTER
# Objetivo: entender o encapsulamento em POO

class Pessoa:

    # Método construtor
    def __init__(self, nome, idade):
        # Os dois underlines (__) deixam o atributo "privado".
        # Isso faz parte do encapsulamento.
        self.__nome = nome
        self.__idade = idade


    # =========================
    # GETTER
    # =========================
    # O getter serve para LER um atributo privado.
    # Assim podemos fazer:
    # print(pessoa.nome)
    # sem acessar diretamente __nome.

    @property
    def nome(self):
        return self.__nome


    # =========================
    # SETTER
    # =========================
    # O setter serve para ALTERAR um atributo privado.
    # Assim podemos fazer:
    # pessoa.nome = "Maria"

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


    # Outro getter
    @property
    def idade(self):
        return self.__idade


    # Outro setter
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade


# =========================
# TESTE
# =========================

pessoa = Pessoa("João", 20)

# Getter (ler)
print(pessoa.nome)
print(pessoa.idade)

# Setter (alterar)
pessoa.nome = "Pedro"
pessoa.idade = 21

print(pessoa.nome)
print(pessoa.idade)

# ERRADO:
# print(pessoa.__nome)
# Gera erro, porque o atributo é privado.

# CERTO:
# print(pessoa.nome)
# Usa o getter.

# ERRADO:
# pessoa.__nome = "Carlos"

# CERTO:
# pessoa.nome = "Carlos"
# Usa o setter.