# () - tuplas, [] - listas, {} - dicionários
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # pode ser sem parênteses
print(lanche)
for pos, comida in enumerate(lanche):
    print(comida, pos)
print(lanche[-2])
print(lanche[1:3]) # fatiamento!
print(sorted(lanche))
# TUPLAS SÃO IMUTÁVEIS!

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(4)) # posição do 4
print(c.count(5)) # quantos 5 existem

pessoa = ('Hanna', 19, 'F', 65.7)
del(pessoa)