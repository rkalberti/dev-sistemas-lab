import random

def jogar():
    print("Bem-vindo ao jogo da Forca!")


    temas = {
        "1": "celulas.txt",
        "2": "taxonomia.txt",
        "3": "anatomia.txt"
    }

    print("Escolha o tema: [1] Células, [2] Taxonomia, [3] Anatomia")
    escolha = input("Digite o número: ")


    arquivo = open(temas[escolha], "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip().upper()) 
    arquivo.close()

    palavra = random.choice(palavras)
    #print(palavras)

    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")
    

    acertou = False
    enforcou = False
    limite_tentativas = len(palavra) + 6
    tentativa = 1

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")

    print("Tente adivinhar a palavra secreta: ")
    while(not acertou and not enforcou):
        # mostrar as letras acertadas
        mostrar_letras_acertadas()
        print("")
        chute = input("Digite uma letra: ")
        indice = 0
        for letra in palavra:
            if chute.upper() == letra:
                letras_acertadas[indice] = letra
            indice = indice + 1
        
        if tentativa == limite_tentativas:
            print("Você perdeu :(\nA palavra era: ", palavra)
            enforcou = True

        if letras_acertadas.count("_") == 0:
            print("Parabéns, você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            acertou = True

        tentativa = tentativa + 1
