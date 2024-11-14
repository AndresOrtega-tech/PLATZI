def find_volume(len=1, width=1, depth=1):
    return len * width * depth, width,'Hola'

result = find_volume(5,6,7)
print(result)

result_2 = find_volume()
print(result_2)

result_3 = find_volume(width=8)
print(result_3)
print(result_3[1])

result_4, width, text = find_volume(10,5,10)
print(result_4, width, text)