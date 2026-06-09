import tkinter as tk
from conta import Conta
import json

def cadastrar():
    agencia = input_agencia.get()
    titular = input_titular.get()
    cpf = input_cpf.get()

    # Cria a nova conta
    nova_conta = Conta(titular, agencia, cpf)

    # Le os dados do arquivo JSON
    try:
        with open("clientes.json", "r") as clientes_leitura:
            clientes = json.load(clientes_leitura)
    except FileNotFoundError:
        clientes = []

    clientes.append({
        "titular": nova_conta.titular,
        "agencia": nova_conta.agencia,
        "numero": nova_conta.numero,
        "cpf": nova_conta.cpf,
        "saldo": nova_conta.saldo,
        "senha": nova_conta.senha,
        "chavepix": nova_conta.chavepix
    })

    # Salva os dados no arquivo JSON
    # Note: Usei "clientes.json" em ambos para manter o padrão
    with open("clientes.json", "w") as clientes_escrita:
        json.dump(clientes, clientes_escrita, indent=4)

    # Atualiza o texto da label de resposta
    label_resposta.configure(
        text=f"Conta: {nova_conta.numero} | Titular: {nova_conta.titular} cadastrado com sucesso!",
        fg="green"
    )

# -- Configuração da Janela --
app = tk.Tk()
app.title("Cadastro de Clientes")
app.geometry("400x300")

# Agência
label_agencia = tk.Label(app, text="Agência:")
label_agencia.pack(pady=5)
input_agencia = tk.Entry(app)
input_agencia.pack()

# Titular
label_titular = tk.Label(app, text="Titular:")
label_titular.pack(pady=5)
input_titular = tk.Entry(app)
input_titular.pack()

# CPF
label_cpf = tk.Label(app, text="CPF:")
label_cpf.pack(pady=5)
input_cpf = tk.Entry(app)
input_cpf.pack()

# Label de Resposta (Resultado)
label_resposta = tk.Label(app, text="", fg="green", font=("Arial", 10, "bold"))
label_resposta.pack(pady=10)

# Botão de Enviar
botao = tk.Button(app, text="Enviar", command=cadastrar)
botao.pack(pady=10)

app.mainloop()