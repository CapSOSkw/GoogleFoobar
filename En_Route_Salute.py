def answer(x):

    index_less = [index for index, i in enumerate(x) if i=="<"]
    index_more = [index for index, i in enumerate(x) if i==">"]
    count = 0
    
    for i in index_less:
        for j in index_more:
            if i > j:
                count += 2
            else:
                continue

    return count


print(answer(">>--<<>><<"))

