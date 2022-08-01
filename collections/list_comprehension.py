matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposta = [[linha[i] for linha in matriz] for i in range(4)]
print(transposta)


lista_n = list(range(10))
print(lista_n)

lista_b= [1 if num >5 else 0 for num in lista_n]
print(lista_b)

lista_m = [num for num in lista_n if num > 5 and num < 8]
print(lista_m)

x = 'impar'
lista_p = [num for num in lista_n if (num % 2 == 0 and x == 'par') or (num % 2 == 1 and x == 'impar')]
print(lista_p)
