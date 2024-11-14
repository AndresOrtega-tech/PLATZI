import sys # sistema operativo
print(sys.path)

import re # expresiones regulares
text = 'Mi numero de telefono es 812 360 6206, el numero codigo del pais es 52, mi numero de la suerte es 999'
result = re.findall('[0-9]+', text)
print(result)

import time # fehcas y horas
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp)
print(local)
print(result)

import collections # utilidad para manejra listas
numbers = [1,1,2,2,2,3,3,3,4,4,4,4,5,5,6,7,8,8,9,9,9]
counter = collections.Counter(numbers)
print(counter)