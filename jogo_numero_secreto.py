import random

def jogar():
    print("---------------------------------------------")
    print("Bem vindo ao jogo do numero secreto")
    print("---------------------------------------------")

    tentativas = 0
    numero_secreto = numero_secreto = random.randrange(1,101)
    pontos = 1000


    print("dificuldade")
    print("(1) facil  (2)medio (3)dificil")
    dificuldade = int(input("digite a deificuldade: "))

    if(dificuldade == 1):
        tentativas = 20
    elif(dificuldade == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1,tentativas +1):
        print("rodada:{} tentativas:{}".format(rodada , tentativas))
        chutestr = input("digite um numero entre 1 e 100 ")
        print("voce digitou:{}".format(chutestr))
        chute = int(chutestr)

        if(chute <1 or chute >100):
            print("voce precisa digitar um numero de 1 a 100")
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(numero_secreto == chute):
            print("parabens voce acertou-pontos:{}".format(pontos))
            break
        
        else:
           if(maior):
                print("o numero e maior do que o numero secreto")
           elif(menor):
                print("o numero e menor do que o numero secreto")
           numeros_perdidos = abs(numero_secreto - chute)
           pontos = pontos - numeros_perdidos
             
    print("fim de jogo")


if (__name__== "__main__"):
    jogar()
