class Quarto:  #cria a classe

    def __init__(self, numero, tipo, diaria):
        self.__numero = numero #self.__ (atributo privado) 
        self.__tipo = tipo
        self.__diaria = diaria
        self.__disponivel = True

    # Getters
    @property 
    #Permite acessar o atributo sem escrever diretamente
    def numero(self):
        return self.__numero

    @property
    def tipo(self):
        return self.__tipo

    @property
    def diaria(self):
        return self.__diaria

    @property
    def disponivel(self):
        return self.__disponivel

    # Métodos
    def exibir_detalhes(self): #Mostra as informações.
        print(f"Número: {self.__numero}")
        print(f"Tipo: {self.__tipo}")
        print(f"Diária: R${self.__diaria}")
        print(f"Disponível: {self.__disponivel}")

    def reservar(self): 
        if self.__disponivel:
            self.__disponivel = False
            print("Quarto reservado com sucesso!")
        else:
            print("O quarto já está ocupado!")

    def liberar(self):
        if not self.__disponivel:
            self.__disponivel = True
            print("Quarto liberado!")
        else:
            print("O quarto já está disponível!")

    def alterar_preco(self, novo_preco):
        self.__diaria = novo_preco
        print("Preço alterado com sucesso!")