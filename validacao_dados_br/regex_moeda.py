import locale
# https://docs.python.org/3.6/library/locale.html

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar_formatado = locale.currency(15000.0, grouping=True)
print(valor_em_dolar_formatado)

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
valor_em_real_formatado = locale.currency(25135.7890, grouping=True)
print(valor_em_real_formatado)

