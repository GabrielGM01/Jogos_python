import jogo_numero_secreto
import jogo_da_forca
    

print("----------------------------------")
print("--------Escolha o seu jogo--------")
print("----------------------------------")


print("(1)Forca  (2) Numero secreto ")

jogo = int(input("Digite o numero do jogo "))


if(jogo == 1):
    print("Jogando o jogo da forca")
    jogo_da_forca.jogar()
    
elif(jogo ==2):
    print("Jogando o jogo do  Numero secreto")
    jogo_numero_secreto.jogar()
