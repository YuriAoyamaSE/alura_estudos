from datetime import datetime
# o timedelta pode ser útil quando precisar usar 
# variáveis temporais. Ex.: criar uma variável de
# 30 dias e 10 horas para aumentar ou deduzir de
# um objeto da classe datetime
# amanha = datetime.today() + timedelta(days=1)

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]

        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]
    
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
            tempo_cadastro = datetime.today() - self.momento_cadastro
            return tempo_cadastro
    
cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro.format_data())
print(cadastro.tempo_cadastro())

# %A retorna os dias da semana por extenso, como Sunday;
# %d exibe os dias do mês com números de 01 a 31;
# %m retorna meses em números de 01 a 12;
# %y mostra o ano com apenas dois dígitos;
# %Y apresenta o ano em formato de quatro números;
# %H retorna o horário no formato decimal, como 00, 001 e etc;
# %M exibe os minutos de forma decimal;
# %S apresenta os segundos em decimal.

# hoje = datetime.today()
# hoje_formatada = hoje.strftime("%d/%m/%Y")
# print(hoje)
# print(hoje_formatada)

# hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
# print(hoje_formatada)
# print(type(hoje))
# print(type(hoje_formatada))

