import forca
import advinhacao

def escolhe_jogo():

    print("*********************")
    print("*Escolha o seu jogo!*")
    print("*********************")
    print("(1) Forca (2) Advinhacao")
    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    if(jogo == 2):
        print("Jogando advinhacao")
        advinhacao.jogar()
if (__name__ == "__main__"):
    escolhe_jogo()