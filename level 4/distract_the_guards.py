test = [1,7,3,21,13,19]


multipler = [1,3,7,15,31,63,127,255,511,1023,2047,4095,8191,16383,32767,
                 65535,131071,262143,524287,1048575,2097151,4194303,8388607,
                 16777215,33554431,67108863,134217727,268435455,536870911,1073741823]   # 2^n - 1


def possible_comb(bananas):

    all_possibles = []
    for i in range(len(bananas)):
        for j in range(i+1, len(bananas)):
            bigger, smaller = max(bananas[i], bananas[j]), min(bananas[i], bananas[j])
            quotient = bigger / smaller

            if quotient in multipler and quotient * smaller == bigger:   #整数倍
                continue

            else:
                all_possibles.append([bananas[i], bananas[j]])

    return all_possibles                          # 返还所有的可能性
    
    
    # 怎么从所有可能中，找到最少会剩余的数
