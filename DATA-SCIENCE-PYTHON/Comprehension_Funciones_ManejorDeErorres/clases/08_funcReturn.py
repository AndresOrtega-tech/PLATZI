def sum_range (min, max):
    print(min, max)
    sum = 0
    for x in range(min, max+1):
        sum += x
    return sum

result = sum_range(10,15)
print(result)
result2 = sum_range(result, result+10)
print(result2)