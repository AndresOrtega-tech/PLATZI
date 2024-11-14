import random

countries = ['col', 'mex', 'bol', 'peru']

population_v2 = {j:random.randint(1,100) for j in countries}
print(population_v2)


result = {country:population for (country, population) in population_v2.items() if population > 50}
print(result)

text = 'Hola a todos, esta es una cadena de texto de prueba'
unique = {c:c.upper() for c in text if c in 'aeiou'}
print(unique)

unique_v2 = {c:text.count(c) for c in text if c in 'aeiou'}
print(unique_v2)