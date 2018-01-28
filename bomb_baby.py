def answer(M, F):
    M, F = int(M), int(F)
    count = 0

    bigger, smaller = max(M, F), min(M, F)
    temp = 0
    while 1:
        if bigger % smaller != 0:
            temp = smaller
            count = count + bigger // smaller
            smaller = bigger - smaller * (bigger // smaller)
            bigger = temp

        else:
            temp = smaller
            count = count + (bigger // smaller) -1
            smaller = bigger - smaller * (bigger // smaller -1)
            bigger = temp

        if bigger == smaller == 1:
            break

        if bigger < 1 or smaller < 1 or bigger==smaller != 1:
            count = "impossible"
            break

    return str(count)


print(answer(6,12))
