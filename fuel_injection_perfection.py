from math import log2
import pandas as pd

def myanswer(n):
    n = int(n)

    # power = int(log2(n))
    # print(power)
    res = 0

    while n != 1:
        print(n)

        if n % 2 == 0:
            n /= 2

        elif n == 3:
            n -= 1

        else:
            power = int(log2(n))
            # print(power)
            if (n + 1) % 4 == 0:
                n += 1

            else:
                n -= 1

        res += 1

    return res
