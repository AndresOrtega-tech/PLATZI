def increment (x):
    return x + 1

def high_ord_fun(x, func):
    return x + func(x)

result = high_ord_fun(2, increment)
print(result)


increment_v2 = lambda x : x + 1
high_ord_fun_v2 = lambda x, func : x + func(x)

result_v2 = high_ord_fun_v2(2, increment_v2)
print(result_v2)



result_v3 = high_ord_fun_v2(2, lambda x: x * 3)
print(result_v3)