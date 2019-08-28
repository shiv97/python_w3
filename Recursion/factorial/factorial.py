def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))
numb=int(input('enter no.:'))
print(factorial(numb))