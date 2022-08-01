class ContaCorrente: 

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f">>codigo {self.codigo} saldo {self.saldo}<<"


conta_gui = ContaCorrente(1)
conta_gui.deposita(1000)
conta_bia = ContaCorrente(2)
conta_bia.deposita(5000)
lista_contas = [conta_gui, conta_bia]
print(lista_contas)
for conta in lista_contas:
    print(conta)