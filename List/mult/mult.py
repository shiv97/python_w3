def L(items):
    sum_numbers = 1
    for x in items:
        sum_numbers *= x
    return sum_numbers
print(L([1,2,8]))