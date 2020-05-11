import random

def jogar():
    print("-------------------------------")
    print("Bem vindo ao jogo da forca")
    print("-------------------------------")


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    erros = 6
    while(erros):
        print(letras_acertadas)
        tentativa = input("Digite uma Letra:")
        tentativa = tentativa.strip().upper()

        if(tentativa in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(tentativa == letra):
                    letras_acertadas[index] = letra
                index += 1
            acertou = "_" in letras_acertadas
            if(acertou == False):
                print(letras_acertadas)
                print("A palavra secreta é {}".format(palavra_secreta))
                print("Voce venceu")
                break
        else:
            erros -= 1
            if(erros == 0):
                print("A palavra secreta é {}".format(palavra_secreta))
                print("Voce perdeu")
                break
            print("Voce tem {} tentativas".format(erros))
       



if (__name__== "__main__"):

    jogar() 


