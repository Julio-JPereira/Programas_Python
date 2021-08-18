import random
def jogar():
    print("*********************")
    print("Bem vindo ao jogo ae!")
    print("*********************")
    numero_secreto = random.randrange(1,101)
    total_tentativas = 0
    pontos = 1000

    print("Selecione o nível da dificuldade", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input())

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    for rodada in range(1,total_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite um numero entre 1 e 100: ")
        chute = int(chute)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #faz ele continuar no laço
        print("Você digitou ", chute)
        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
        if (acertou):
            print("Você acertou! E fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! Seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do game")
if(__name__ == "__main__"):
    jogar()