from conta import Conta
contaPatrick = Conta("Patrick", "123.456.789-00", 500, "1234", 5678)
contaPatrick.mostrar()

# criar os seguintes metodos
contaPatrick.depositar(1000)
contaPatrick.sacar(250)

conta2 = Conta("Fulano", "987.654.321-00", 500, "3333", 2314)
contaPatrick.pix(conta2, 250)
