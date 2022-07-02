import re


class ExtratorURL:
    def __init__(self, url):
        """Salva a url em um atributo do objeto (self.url = url) e verifica se a url é válida"""
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        if type(url) == str:
            return url.strip()
        return ""

    def valida_url(self) -> True:
        """Valida se a url está vazia e dentro do padrão"""
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("url invalida")
        else:
            #            print(match, "url válida")
            return True

    def get_url_base(self):
        """Retorna a base da url."""
        return self.url[:self.url.find('?')]

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        return self.url[self.url.find('?') + 1:]

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parametro `parametro_busca`."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url + '\n' + 'url base:' + self.get_url_base()
    
    def __eq__(self, other):
        return self.url == other.url


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

# usando métodos especiais:
print(f'Tamanho da url é: {len(extrator_url)}')
print(f'Print do extrator_url: {extrator_url}')