'''
Propiedades de los conjuntos
- Se pueden modificar
- No tienen un orden
- No pueden tener elementos duplicados
    - Si hay algun elemento duplicado, se elimina al momento de imprimir
'''

set_countries = {'col', 'mex' ,'bol', 'col'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,3,4,5}
print(set_numbers)

set_types = {1, 'Hola', False, 12.12}
print(set_types)

set_from_string = set('Hola')
print(set_from_string)

set_from_tuples = set(('abc', 'cvb', 'as', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)