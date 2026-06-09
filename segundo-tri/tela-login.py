import tkinter as tk
from clientes import Clientes

def login():
    cpf = input_cpf.get()
    senha = input_senha.get()

    for cliente in bd_clientes:
        if cliente["cpf"] == cpf and cliente["senha"] == senha:
            label_resposta.config(text="Login realizado com sucesso!", fg="green")
            return

    label_resposta.config(text="CPF ou senha incorretos!", fg="red")


app = tk.Tk()
app.title("Login")
app.geometry("300x200")

tk.Label(app, text="CPF:").pack()
input_cpf = tk.Entry(app)
input_cpf.pack()

tk.Label(app, text="Senha:").pack()
input_senha = tk.Entry(app, show="*")
input_senha.pack()

tk.Button(app, text="Entrar", command=login).pack(pady=10)

label_resposta = tk.Label(app, text="")
label_resposta.pack()

app.mainloop()