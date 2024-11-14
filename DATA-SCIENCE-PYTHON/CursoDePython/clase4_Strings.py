name = 'Andres'
last_name = '     TAMEZ Ortega    '

# Type, es para saber que tipo de varible es (string, int, bool...)
print(type(name))

# indexacion, para saber que letra esta en la posicion del index que pidamos, empiza desde el 0
print(name[2])
print(name[-1])

# Concatenar, es para unir cadenas de texto
print(name + ' ' +last_name)

# Replicacion, para multiplicar la cantidad que se imprime la cadena
print(name * 5)

# len, para saber la longitud de la cadena
print(len(name))
print(len(last_name))

# .lower(), es para poner toda la cadena en minusculas
print(last_name.lower())

# .upper(), es para poner toda la cadena en mayuscula
print(last_name.upper())

# .strip(), es para eliminar los espacios del principio y al final
print(last_name.strip())

#Capitaliza la primera letra.
texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#title()
#Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

#join(iterable)
#Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"