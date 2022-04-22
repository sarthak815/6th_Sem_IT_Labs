from itertools import combinations
data = [['A','B','C'], ['B','C','D'],['A','D','B']]
x = []
for val in data:
    k = list(combinations(val,2))
    print(k)
    for i in k:
        print(i)
        if i not in x:
            print("Not Present")
            x.append(i)
print(x)
l3_s = list()

