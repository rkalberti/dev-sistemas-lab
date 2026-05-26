# AULA 01(2TRI) --- PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
# MÉTODO CONSTRUTOR: cria um objeto conforme a nessessidade do usuário

import random

class Conta: 
    def __init__(self, titular, cpf, limite, chave_pix, senha):

        # Propriedades
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = 2026
        self.__conta = random.randint(100000, 999999)
        self.__saldo = 0
        self.__limite = limite
        self.__chave_pix = chave_pix
        self.__senha = senha

    # Getter
    @property
    def titular(self):
        return self.__titular

    # Setter
    @titular.setter
    def titular(self, novo_nome):
        self.__titular = novo_nome

    # Extrato
    def extrato(self):
        print(f"""
Titular: {self.__titular}
Agência: {self.__agencia}
Conta: {self.__conta}
Saldo: R${self.__saldo}
""")

    # Sacar
    def sacar(self, valor):

        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            print("Saque efetuado com sucesso!")
            return True

        else:
            print("Não foi possível efetuar o saque!")
            return False

    # Depositar
    def depositar(self, valor):

        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado com sucesso!")

        else:
            print("Valor inválido!")

    # Transferir
    def transferir(self, valor, conta_destino):

        if self.sacar(valor):
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso!")

        else:
            print("Transferência não realizada!")