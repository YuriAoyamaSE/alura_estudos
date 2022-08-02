from functools import total_ordering
# com o total_ordering, não precisa criar um método para cada operador de comparação
# como o >=, <=

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

# aqui há uma comparação primária pelo saldo e secundária (saldos iguais), útil para ordenação
    def __lt__(self, outro):
        return self._saldo < outro._saldo

# O __lt__ já serve, não precisando do __gt__ para comparação:
    def __gt__(self, outro):
        return self._saldo > outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
