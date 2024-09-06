def recursive_power(x, n):
    if n == 1: return x

    if n % 2 == 0:
        y = recursive_power(x, n/2)
        return y * y
    else:
        y = recursive_power(x, (n-1)/2)
        return y * y * x
    
print(recursive_power(3, 5))