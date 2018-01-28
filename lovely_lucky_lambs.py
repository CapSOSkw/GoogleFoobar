from math import sqrt, log

def answer(total_lambs):
    
    total_lambs = int(total_lambs)
    
    if 10 <= total_lambs <= 10 ** 9:    
        geo_seq_sum = 0
        geo_seq_n = 1

        while sum_geo_seq(geo_seq_n) <= total_lambs:
            geo_seq_n += 1
            if sum_geo_seq(geo_seq_n) > total_lambs:
                geo_seq_n -= 1
                break

        geo_seq_sum = sum(geo_seq(geo_seq_n))
        
        remainder = total_lambs - geo_seq_sum
        if remainder >= 2 ** (geo_seq_n - 1) + 2 ** (geo_seq_n - 2):
            geo_seq_n += 1

        # =========    
        fib_sum = 0
        fib_n = 1

        while fib_sum <= total_lambs:
            fib_sum = fib_sum + Fib(fib_n)
            if fib_sum > total_lambs:
                fib_n -= 1
                break
            fib_n += 1

        return abs(geo_seq_n - fib_n)

    else:
        return 0


def geo_seq(n):
    a, b = 1, 2
    for _ in range(n):
        yield a
        a, b = b, 2 * b

def sum_geo_seq(n):
    return (2 ** n) - 1

def Fib(n):
    return 1 if n == 1 else int((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

