from collections import Counter


def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

# https://python.org.br/introducao/
texto1 = """Existem diversos cursos onlines onde você pode encontrar material. São cursos que você consegue aprender o básico da programação com Python como tipos de variáveis, como escrever funções, etc.

Devo usar o Interpretador do Python puro? Depende da sua preferência. Ele é uma ferramenta poderosa. Mas boa parte de profissionais usa o interpretador ipython pois este contém mais recursos visuais e de auxílio (como colorir as mensagens de erro).

Que IDE usar? Depende muito da sua preferência. Você pode usar qualquer editor de texto padrão, como o Notepad++, Gedit ou Sublime até o VI puro. Não existe padrão. Para quem vem do MATLAB ou R, o Spyder pode ser muito útil. O Pycharm é outro IDE muito utilizado na comunidade.

Aonde eu encontro os módulos para utilizar no meu projeto? Alguns módulos já vem por padrão no Python puro, por exemplo o módulo matemático. Outros, devem ser baixados de um repositório, como é o caso do Django ou Numpy. Hoje, mais de 107 mil projetos estão cadastros no repositório oficial. Caso você não ache o que procura, há muito incentivo para que você construa um módulo novo e inclua no repositório!

Se você não tem a menor ideia mesmo de que módulo você precise, dê uma procurada no Google e StackOverflow. De certo alguém já fez algo parecido com o que você precisa!"""

analisa_frequencia_de_letras(texto1)
