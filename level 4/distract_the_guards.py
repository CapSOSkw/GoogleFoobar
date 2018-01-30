multipler = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767,
             65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607,
             16777215, 33554431, 67108863, 134217727, 268435455, 536870911, 1073741823] # 投机，一共三十个数。题目要求最大数2**30-1


def possible_comb(bananas):
    all_possibles = []
    for i in range(len(bananas)):
        for j in range(i + 1, len(bananas)):
            bigger, smaller = max(bananas[i], bananas[j]), min(bananas[i], bananas[j])
            quotient = bigger / smaller

            if quotient in multipler and quotient * smaller == bigger:
                continue

            else:
                all_possibles.append([bananas[i], bananas[j]])

    return all_possibles   #返回所有可能的组合


def inf_loop(x, y):         #判断两个数会不会无限循环
    bigger, smaller = max(x, y), min(x, y)
    quotient = bigger / smaller
    return False if quotient in multipler and quotient * smaller == bigger else True   


def shortest_combination(x):  #返回数值运用 最少的组合
    return min(x, key=lambda l: len(l) or 100)

def pop_value(l, x, y):       #删除已经用过的数
    if x in l:
        l.pop(l.index(x))

    if y in l:
        l.pop(l.index(y))

    return l

def value_with_combination(l, value):  # return which combination is created by value
    return [i for i, j in enumerate(l) if j == value]  ## 返回由哪个数产生的组合的index


def answer(banana_list):
    # 初始化变量
    length_banana = len(banana_list)
    count = 0
    banana_list = sorted(banana_list)
    
    all_combinations = [[y for y in banana_list if inf_loop(x, y)] for x in banana_list]

    highest_priority = shortest_combination(all_combinations)

    while len(highest_priority) and len(filter(lambda x: len(x) > 0, all_combinations)) > 1:

        base_value0 = banana_list[all_combinations.index(highest_priority)]

        one_of_comb_value = highest_priority[0]

        for i in value_with_combination(banana_list, one_of_comb_value):
            if len(all_combinations[i]) != 0:
                del all_combinations[i][:]
                break

        del highest_priority[:]

        all_combinations = map(lambda x: pop_value(x, base_value0, one_of_comb_value), all_combinations)

        count += 2

        highest_priority = shortest_combination(all_combinations)

    return length_banana - count





