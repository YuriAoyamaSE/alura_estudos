import random

def jogar():

    print("||||||||||||||||||||||||||||||||||||||||")
    print("|| Bem vindos ao jogo de adivinhação! ||")
    print("||||||||||||||||||||||||||||||||||||||||")

    dificuldade_numero = [10,100,1000,1000]
    dificuldade_tentativas = [2,3,5,4]
    dificuldade = 0
    print("Níveis de dificuldade:")
    for dificuldade in range(0, len(dificuldade_numero)):
        print(f"{dificuldade + 1} = {dificuldade_tentativas[dificuldade]} tentativas e número secreto entre 1 e {dificuldade_numero[dificuldade]}")

    print("Escolha o nível de dificuldade: ")
    dificuldade = int(input()) - 1
    while(dificuldade < 0 or dificuldade >= len(dificuldade_numero)):
        print(f"Nível inválido. Escolha entre 1 e {len(dificuldade_numero)}")
        dificuldade = int(input()) - 1

    numero_max = dificuldade_numero[dificuldade]
    total_de_tentativas = dificuldade_tentativas[dificuldade]
    numero_secreto = random.randrange(1,numero_max + 1)
    rodada = 1
    pontos = numero_max

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input(f"Digite um número de 1 a {numero_max}: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        while(chute < 1 or chute > numero_max):
            print("Você digitou um número inválido. Tente novamente.")
            chute_str = input(f"Digite um número de 1 a {numero_max}: ")
            print("Você digitou: ", chute_str)
            chute = int(chute_str)

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("|||||||||||||||||||||||||||||")
            print("|| Parabéns! Você acertou! ||")
            print("|||||||||||||||||||||||||||||")
            break
        elif(rodada == total_de_tentativas):
            print("O número secreto era", numero_secreto)
        else:
            print("Você errou")
            if(maior):
                print("Seu chute foi MAIOR do que o número secreto.")
            elif(menor):
                print("Seu chute foi MENOR do que o número secreto.")

        pontos = pontos - abs(chute - numero_secreto)

    print(f"Pontuação: {int(pontos)} pontos")
    print("------------Fim do jogo------------")

if(__name__ == "__main__"):
    jogar()
