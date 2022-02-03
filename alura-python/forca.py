def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False
    letras_acertadas = []
    for i in palavra_secreta:
        letras_acertadas.append('_')
    print(*letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute
            index = index + 1

        print(*letras_acertadas)
        print("jogando ...")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
