from collections import defaultdict
from typing import Counter

frase = "o rato possui um rato de vizinho que se tornou vizinho de outro rato"
palavras = frase.lower().split()
print(f"frase: {frase}")
print(f"conjunto de palavras = {set(palavras)}")
dicionario = dict()

for palavra in set(palavras):
    dicionario[palavra] = palavras.count(palavra)
# ou, para manter a ordem como apareceu:
# for palavra in palavras:
#     valor = dicionario.get(palavra, 0)
#     dicionario[palavra] = valor + 1

print(dicionario)

for chave, valor in dicionario.items():
    print(f"palavra {chave} aparece {valor} vezes")

# para evitar erro em chamar um item que não existe no dict 
# podemos usar o método get. Se a chave não existie, o get 
# retorna, por padrão, "None". Mas é possível por um valor default
item = 'gato'
print(f"\npalavra {item} aparece {dicionario.get(item, 0)} vezes")

# também podemo usar o defaultdict, que recebe uma função para valor default, sem precisar usar o get:
default_dict = defaultdict(int)
print(f"\ngato aparece {default_dict['gato']} vezes no default_dict")
# com isso, em vez da estrutura anterior, poderíamos fazer:
for palavra in palavras:
    default_dict[palavra] += 1
print(default_dict)
#perceba que sempre que é chamado, ele cria um item (veja o item 'gato': 0)
for chave, valor in default_dict.items():
    print(f"palavra {chave} aparece {valor} vezes")
    
    
    
# por fim, para algo como foi feito aqui, era mais fácil usar o Counter, 
# que vai gerar um tipo similar a dict onde os valores são contagens das chaves

contador = Counter(frase.lower().split())
print('\n',contador)
for chave, valor in contador.items():
    print(f"palavra {chave} aparece {valor} vezes")
    