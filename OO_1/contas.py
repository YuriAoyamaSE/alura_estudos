class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto: {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        print(f"Saldo da conta {self.__numero}: R$ {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        montante_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= montante_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Saque não realizado. \nSem limite disponível.")

    def transferir(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    @staticmethod
    def codigo_banco():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
