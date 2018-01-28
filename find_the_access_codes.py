def myanswer(l):

    list_size = len(l)
    count = 0

    for i in range(1, len(l)-1):

        # print(i,l[i], l[:i], l[i+1:])
        front = [item for item in l[:i] if l[i] % item == 0]

        behind = [item for item in l[i+1:] if item % l[i] == 0]

        # print(front, behind)
        count = count + len(front)*len(behind)

    return count
