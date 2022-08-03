# quando há armazenamento grande, poderá haver problema de memória insuficiente.
# Para resolver isso, podemos criar usar um iterador e seu método next(), que é
# o "lazy evaluation", que vai apenas pegando um trecho por vez e depois descartando.
# por exemplo, abaixo está uma solução para leitura de um arquivo muito grande, no qual
# se pretende filtrar sites sem protocolo de segurança.
# Se o arquivo fosse lido já para gerar uma list(), poderia acusar erro de memória, como,
# por exmeplo, usando um código:
# registro = open('acessos.log', 'r')
# sites_sem_https = [url for url in registro if url.startswith('http://')]

class IteradorHttp():
    def __init__(self):
        self.registro = open('acessos.log', 'r')
        self.linha_atual = ''

    def __iter__(self):
        return self

    def __next__(self):
        self.linha_atual = self.registro.readline()
        while self.linha_atual and not self.linha_atual.startswith('http://'):
            self.linha_atual = self.registro.readline()
        if self.linha_atual:
            return self.linha_atual
        raise StopIteration


iterador = IteradorHttp()

# print(next(iterador, 'Fim do iterador'))
# o for usa a função next e para quando não há mais. Se for usado diretamente o next,
# deve usar um valor default para evitar erro quando terminar os valores
for url in iterador:
    print(url)

# para criar iteradores, o python também conta com os "geradores".
# Para saber mais: https://docs.python.org/3/howto/functional.html#generators
