import random
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")


    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de deficuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, total_de_tentativas+1):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute_int = int(chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("Você digitou {}, número inválido, digite um número entro 1 e 1oo".format(chute_int))
            continue

        print("Você digitou ", chute_str)
        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        elif (maior):
            print("O numero que você digitou foi maior!!")
        else:
            print("O número que você digitou foi menor!!")

        pontos_perdidos = abs(numero_secreto - chute_int)
        pontos = pontos - pontos_perdidos
        print("*********************************")

    print("Fim de jogo!!")
if(__name__ == "__main__"):
    jogar()
