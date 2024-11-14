numbers = [1,2,3,4]
numbers_v2 = [i*2 for i in numbers ]

print(numbers, numbers_v2)

numbers_v3 = list(map(lambda i: i*2, numbers))
print(numbers_v3)




numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]
print(numbers_1, numbers_2)

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)