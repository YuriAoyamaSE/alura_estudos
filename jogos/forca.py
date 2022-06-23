import random

def jogar():
    layout_de_abertura()

    # Parâmetros de resultado
    enforcou = False
    acertou = False
    quantidade_de_erros = 0
    tentativas = 6

    # Gerando a palavra e parâmetros
    palavra_secreta = gerador_de_palavra()
    letras_secretas = list(palavra_secreta.upper())
    letras_reveladas = list("_" * len(letras_secretas))
    letras_erradas = {""}

    # principal
    while (not enforcou and not acertou):
        imprime_letras_reveladas(letras_reveladas)
        desenha_forca(quantidade_de_erros)

        # contabilizando tentativas restantes
        print(f"Você possui {tentativas - quantidade_de_erros} tentativas.")

        chute = recebe_chute()

        # Compara letras
        index = 0
        if chute in letras_secretas:
            for letra in letras_secretas:
                if chute == letra:
                    letras_reveladas[index] = chute
                index += 1
        else:
            letras_erradas.add(chute)
            quantidade_de_erros += 1

        #imprime erros
        print()
        print("Chutes errados: ", end="")
        for letra in letras_erradas:
            print(letra, end=" ")
        print()

        # Quebrando o loop / terminando o jogo
        enforcou = quantidade_de_erros == tentativas
        acertou = not "_" in letras_reveladas

    resultado_do_jogo(palavra_secreta, acertou, enforcou)

    print("------Fim do jogo------")

def layout_de_abertura():
    print("||||||||||||||||||||||||||||||||||")
    print("|| Bem vindos ao jogo da Forca! ||")
    print("||||||||||||||||||||||||||||||||||")
    print("Palavra Secreta:")

def gerador_de_palavra():
    lista_de_palavras = []
    with open("forca.txt", "r") as biblioteca:
        for palavra in biblioteca:
            palavra = palavra.strip()
            lista_de_palavras.append(palavra)
    return lista_de_palavras[random.randrange(0, len(lista_de_palavras))]

def recebe_chute():
    chute = input("Digite uma letra:")
    return chute.strip().upper()

def desenha_forca(quantidade_de_erros):
    print(" _______")
    print(" |     |")
    if quantidade_de_erros > 0:
        print(" |     O")
    else:
        print(" |")
    if quantidade_de_erros > 3:
        print(" |    ´|`")
    elif quantidade_de_erros > 2:
        print(" |    ´| ")
    elif quantidade_de_erros > 1:
        print(" |     | ")
    else:
        print(" |")
    if quantidade_de_erros > 4:
        print(" |    ´ ")
    else:
        print(" |     ")
    print("------------")

def imprime_letras_reveladas(letras):
    for letra in letras:
        print(letra, end=" ")
    print()

def resultado_do_jogo(palavra_secreta, acertou, enforcou):
    print(f"A palavra secreta é: {palavra_secreta.upper()}")
    if acertou:
        print("     Parabéns!                  ___________      ")
        print("Você escapou da forca!         '._==_==_=_.'     ")
        print("                               .-\\:      /-.    ")
        print(" _______                      | (|:.     |) |    ")
        print(" |     |                       '-|:.     |-'     ")
        print(" |                               \\::.    /      ")
        print(" |               O                '::. .'        ")
        print(" |              ´|`                 ) (          ")
        print("------------    ´ `               _.' '._        ")
        print("                                 '-------'       ")
    elif enforcou:
        print("Suas tentativas acabaram. Você foi enforcado!")
        print(" _______")
        print(" |     |")
        print(" |     O")
        print(" |    ´|`")
        print(" |    ´ `")
        print("------------")

if(__name__ == "__main__"):
    jogar()