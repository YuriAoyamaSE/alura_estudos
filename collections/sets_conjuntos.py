set_a = {1,2,3,4}
set_a.add(0)
print(f"set_a = {set_a}")
set_b = {3,4,5,6}
set_b.add(7)
print(f"set_b = {set_b}")

uniao = set_a | set_b
print(f"uniao = {uniao}")

interseccao = set_a & set_b
print(f"interseccao = {interseccao}")

exclusao = set_a - set_b
print(f"exclusao = {exclusao}")

ou_exclusivo = set_a ^ set_b
print(f"ou_exclusivo = {ou_exclusivo}")

# o frozenset vai reber um iterável e transformar em um set, 
# mas que não pode ser modificado. Quase uma "Tupla-Set"
set_congelado = frozenset([1,2,3,4,4,4])
print(set_congelado)
