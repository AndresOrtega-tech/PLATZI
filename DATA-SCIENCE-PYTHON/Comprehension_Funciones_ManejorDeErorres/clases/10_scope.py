price = 100 # global scope (variable de alcance global)

def increment():
    price = 200
    result = price + 10 # local scope (variable de alcance local)
    return result

print(price)

price_2 = increment()
print(price_2)

# print(result) # result no tiene contexto aqui, solo dentro de la funcion increment