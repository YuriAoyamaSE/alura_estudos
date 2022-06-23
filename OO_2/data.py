from datetime import date

data_atual = date.today()

data_em_texto = "{}/{}/{}".format(data_atual.day, data_atual.month, data_atual.year)

print(data_atual)
print(data_em_texto)

data_em_texto = data_atual.strftime("%d/%m/%Y")

print(data_em_texto)

##########################################
print("\n")

from datetime import datetime, timezone, timedelta

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y")

print(data_e_hora_em_texto)

"""
O construtor timedelta recebe vários outros argumentos além da hora, nessa ordem:

days (dias)
seconds (segundos)
microseconds (microsegundos)
milliseconds (milisegundos)
minutes (minutos)
hours (horas)
weeks (semanas)
"""

diferenca = timedelta(hours = -3)
fuso_horario = timezone(diferenca)
print(fuso_horario)

### Para converter tempo da máquina para a UTC, usar método astimezone()

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d/%m/%Y %H:%M")

print(data_e_hora_sao_paulo_em_texto)