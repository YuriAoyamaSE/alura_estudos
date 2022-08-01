from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod
    def passa_o_mes():
        pass

    def __str__(self):
        return f">>codigo {self._codigo} saldo {self._saldo}<<"


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


def imprime_contas(contas):
    for conta in contas:
        print(conta)


conta_corrente = ContaCorrente(16)
conta_corrente.deposita(1000)
conta_poupanca = ContaPoupanca(17)
conta_poupanca.deposita(1000)
contas = (conta_corrente, conta_poupanca)

imprime_contas(contas)
conta_poupanca.passa_o_mes()
conta_corrente.passa_o_mes()
imprime_contas(contas)
