# EXECUTAR NO TERMINAL - python3 nomedoarquivo.py - ver se a classe foi importada corretamente 

from quarto import Quarto # importa a classe

quarto1 = Quarto(101, "Casal", 200.00) #cria um objeto

quarto1.exibir_detalhes() # mostra os dados

quarto1.reservar()

quarto1.exibir_detalhes()

quarto1.reservar()

quarto1.liberar()

quarto1.alterar_preco(250.00)

quarto1.exibir_detalhes()

quarto1.liberar()