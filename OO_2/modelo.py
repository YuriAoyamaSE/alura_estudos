from abc import ABCMeta, abstractmethod

class Programa(metaclass = ABCMeta):
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @abstractmethod
    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.likes} likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes"

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme("Vingadores - Guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
demolidor = Serie("Demolidor", 2016,2)
tmep = Filme("Todo mundo em pânico", 1999, 100)

vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor,tmep]
playlist_fds = Playlist("fim de semana", filmes_e_series)

print(f'Tamanho da playlist "{playlist_fds.nome}": {len(playlist_fds)}')

for programa in playlist_fds:
    print(programa)
