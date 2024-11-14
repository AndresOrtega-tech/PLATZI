set_a = {'col', 'mex', 'bol'}
set_b = {'peru', 'bol'}

# uninion
set_c = set_a.union(set_b)
print(set_c)

# operador para unir dos conjuntos
print(set_a | set_b)

# intersection
set_c = set_a.intersection(set_b)
print(set_c)

# operador para la interseccion de dos conjuntos
print(set_a & set_b)

# difference
set_c = set_a.difference(set_b)
print(set_c)

# operador para la diferencia de dos conjuntos
print(set_a - set_b)

# symmetric diferrence
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# operador para la diferencia simetrica
print(set_a ^ set_b)