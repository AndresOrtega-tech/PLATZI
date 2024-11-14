# Lista de ejemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ejemplos de slicing
sublista1 = lista[2:5]
sublista2 = lista[:4]
sublista3 = lista[5:]
sublista4 = lista[::2]
sublista5 = lista[1:7:2]

# Slicing con índices negativos
sublista6 = lista[-5:]
sublista7 = lista[:-5]
sublista8 = lista[-8:-2:2]

# Salida de resultados
print("Lista original:", lista)
print("Sublista del índice 2 al 4:", sublista1)
print("Sublista desde el inicio al índice 3:", sublista2)
print("Sublista desde el índice 5 al final:", sublista3)
print("Sublista con paso de 2:", sublista4)
print("Sublista del índice 1 al 6 con paso de 2:", sublista5)
print("Últimos 5 elementos:", sublista6)
print("Todos menos los últimos 5:", sublista7)
print("Sublista del índice -8 al -3 con paso de 2:", sublista8)