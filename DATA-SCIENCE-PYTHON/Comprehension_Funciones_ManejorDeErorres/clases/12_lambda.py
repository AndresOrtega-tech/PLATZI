def increment(x):
    return x + 1

increment_v2 = lambda x : x+1

result = increment(2)
print(result)

result_v2 = increment_v2(2)
print(result_v2)


full_name = lambda name, lastname : f'Full name is {name.title()} {lastname.title()}'

text = full_name('andres', 'tamez')
print(text)