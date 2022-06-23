import forca
import adivinha
print("Jogos disponíveis:")
print("(1) Forca")
print("(2) Adivinhação")

jogo_escolhido = int(input("Escolha o que você quer jogar: "))

if(jogo_escolhido == 1):
    forca.jogar()
elif(jogo_escolhido == 2):
    adivinha.jogar()
