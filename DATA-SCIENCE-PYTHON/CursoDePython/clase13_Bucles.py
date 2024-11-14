frutas = ['Manzana', 'Pera', 'Uva', 'Naranja', 'Tomate']

for i in frutas:
    if i == 'Naranja':
        print('Fruta encontrada')

x = 0
while x <= 5:
    print(x)
    x += 1

for i in frutas:
    if i == 'Pera':
        continue
    print(i)
    