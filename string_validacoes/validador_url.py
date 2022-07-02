import re

# quando usa () quer dizer que o parametro deve ser
# exatamente igual. Pode até por dentro um do outro (())
# quando usar [], define um conjunto possível de parametros
# já o ? é para dizer que é opcional.
# assim, usar ()?define duas escolha: ou bota como tá ou não bota nada

# padrão de exemplo: https://www.bytebank.com.br/cambio
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

url = 'www.bytebank.com.br/cambio'

match = padrao_url.match(url)

if not match:
    raise ValueError("url invalida")
else:
    print(match, "url válida")
