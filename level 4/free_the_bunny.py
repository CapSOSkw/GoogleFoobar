from itertools import combinations
import math

def combinational_number(m,n):
    return math.factorial(m)/(math.factorial(n) * math.factorial(m-n))

def myanswer(num_buns, num_required):

    factorial_n = num_buns - num_required + 1

    # total_combination = combinational_number(num_buns, factorial_n)

    bunny_index = list(combinations(range(num_buns), factorial_n))

    bunny_key_distribution = [[] for _ in range(num_buns)]

    for key_index, bunny in enumerate(bunny_index):
        for b in bunny:
            bunny_key_distribution[b].append(key_index)

    return bunny_key_distribution

print myanswer(5,3)

'''
Take answer(5,3) as example:

key_index   bunny_index
0           0,1,2
1           0,1,3
2           0,1,4
3           0,2,3
4           0,2,4
5           0,3,4
6           1,2,3
7           1,2,4
8           1,3,4
9           2,3,4

根据规律， 每个bunny_index的长度等于 (num_buns - num_required + 1) 5-3+1.
通过排列组合， C(5,3)=10. 所以总共有10个组合分别对应key的index。 最后把key_index
分别附给bunny， 根据bunny的index。 例， bunny_index=(0,1,2)对应key_inde=0，于是，
0，1，2的bunny就得到0号key.

'''

