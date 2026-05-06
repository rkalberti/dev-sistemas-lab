# AULA 01(2TRI) --- PROGRAMAÇÃO ORIENTADA A OBJETOS (POO)
# MÉTODO CONSTRUTOR: cria um objeto conforme a nessessidade do usuário

import random

class Conta: 
    def __init__(self, titular, cpf, limite, chave_pix, senha):
        # atributos:
        self.__titular = titular
        self.__cpf = cpf
        self.__agencia = 2026       # 2026 valor fixo, vai aparecer em todos os objetos
        self.__conta = random.randint(100000, 999999)   # escolhe o número da conta 
        self.__saldo = 0
        self.__limite = limite 
        self.__chave_pix = chave_pix 
        self.__senha = senha


    # Funçãao para mostra os dados
    def mostrar(self):
        print(f"Titular: {self.__titular}\nAgência: {self.__agencia}\nConta: {self.__conta}\nSaldo: {self.__saldo}")


    def saca(self, valor):
        #verifica se pode sacar o valor
