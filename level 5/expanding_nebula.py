import numpy as np

# Veritical patterns

VTF = [[1,1],[1,5],[2,4],[2,6],[2,11],[3,1],[3,5],[4,2],[4,7],[4,8]]
VTT = [[1,2],[1,4],[2,1],[3,4],[4,3]]
VFT = [[1,2],[1,4],[2,3],[3,2],[3,4],[4,1],[7,1],[9,1],[10,3]]
VFF = [[1,1],[1,5],[2,2],[2,7],[2,8],[3,1],[3,5],[4,4],[4,6],[4,11],[5,3],
       [5,9], [5,10], [5,12],[6,2],[6,7],[6,8],[7,4],[7,6],[7,11],[8,3],
       [8,9],[8,10],[8,12],[9,4],[9,6],[9,11],[10,2],[10,7],[10,8],[11,3],
       [11,9],[11,10],[11,12],[12,3],[12,9],[12,10],[12,12]]

pattern_dict = {
                "Veritical":{"00":[[1,1],[1,5],[2,2],[2,7],[2,8],[3,1],[3,5],[4,4],[4,6],[4,11],[5,3],
                                   [5,9], [5,10], [5,12],[6,2],[6,7],[6,8],[7,4],[7,6],[7,11],[8,3],
                                   [8,9],[8,10],[8,12],[9,4],[9,6],[9,11],[10,2],[10,7],[10,8],[11,3],
                                   [11,9],[11,10],[11,12],[12,3],[12,9],[12,10],[12,12]],
                             "01":[[1,2],[1,4],[2,3],[3,2],[3,4],[4,1],[7,1],[9,1],[10,3]],
                             "10":[[1,1],[1,5],[2,4],[2,6],[2,11],[3,1],[3,5],[4,2],[4,7],[4,8]],
                             "11":[[1,2],[1,4],[2,1],[3,4],[4,3]],
                             },

                "Horizonal":{}

                    }



def convert2int(l):
    return map(int, l)

test = [True, False, True]
d_test = convert2int(test)

test2 = [False, True, False]
d_test2 = convert2int(test2)


def convert2combination(l):
    return list(map(lambda x,y: str(x)+str(y), l[:-1], l[1:]))

result = []
for i in range(len(d_test)-2):
    for item in pattern_dict["Veritical"][convert2combination(d_test)[i]]:
        latter = item[-1]
        for j in pattern_dict["Veritical"][convert2combination(d_test)[i+1]]:
            if j[0] == latter:
                result.append(item + [j[1]])


result2 = []

for i in range(len(d_test2)-2):
    for item in pattern_dict["Veritical"][convert2combination(d_test2)[i]]:
        latter = item[-1]
        for j in pattern_dict["Veritical"][convert2combination(d_test2)[i+1]]:
            if j[0] == latter:
                result2.append(item + [j[1]])

for i in zip(test, test2):
    print convert2combination(convert2int(i))