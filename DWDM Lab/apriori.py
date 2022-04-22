import csv
from itertools import combinations


rows = []
answer = {}
lastC = {}
C = {}
L = {}
def read_csv(path = 'ap1.csv'):
    file = open(path, 'r')
    file_reader = csv.reader(file)
    for row in file_reader:
        rows.append(row)
    print(rows)
    
def get_candidateset():
    for row in rows:
        seen_items = []
        for val in row:
            if val not in seen_items and val!='':
                seen_items.append(val)
                C[val] = C.get(val,0)+1
    print(C)

def get_frequentset(min_supp):
    answer.update(L)
    L.clear()
    for item in C:
        if C[item]>=min_supp:
            L[item] = C[item]
    print(L)

def get_candidateset2():
    lastC.clear()
    lastC.update(L)
    C.clear()
    for k1 in L:
        for k2 in L:
            x = []
            if k1>=k2:
                continue
            x.append(k1)
            x.append(k2)
            C[str(x)] = 0
    L.clear()
    print(C)

def get_candidateset2_count():
    for item in C:
        fset = eval(item)
        for row in rows:
            if set(fset).issubset(set(row)):
                C[item] = C.get(item,0)+1
    print(C)

def make_next_itemset(k):
    print(L)
    lastC.clear()
    lastC.update(L)
    C.clear()
    x = []
    for k1 in L:
        for k2 in L:
            print("**********\n")
            print(k1)
            print(k2)
            if k1>=k2:
                print("More")
                continue
            print("Lesser")
            k1_l = eval(k1)
            k2_l = eval(k2)
            flag = 0
            for i in range(k-2):
                if L[k1]!=L[k2]:
                    flag = 1
                    break
            if flag==0:
                for i in range(k-2):
                    x.append(k1_l[i])
                
                x.append(k2_l[k-2])
                x.append(k2_l[k-2])
                C[str(x)] = 0
                x.clear()
    print(C)

def get_candidate_count():
    for item in C:
        fset = eval(item)
        for row in rows:
            if set(fset).issubset(set(row)):
                C[item] = C.get(item,0)+1
    print(C)

def prune():
    xlist = []
    remlist = []
    for klast in lastC:
        lklast = eval(klast)
        xlist.append(lklast)
    for ky in C:
        klist = eval(ky)
        klist.sort()
        comb = combinations(klist, k-1)
        comb = list(comb)
        flag = 0
        for c in comb:
            c = list(c)
            if c not in xlist:
                flag = 1
                break
        if flag == 1:
            remlist.append(str(ky))
    for item in remlist:
        C.pop(str(item))
    print(C)

def association_rules():
    for freq in answer:
        fset = eval(freq)
        if len(fset)<=1:
            continue    
        elif len(fset)==2:
            for item in fset:
                print(item, end='->')
                for i2 in fset:
                    if(i2!=item):
                        print(i2)
        else:
            comb = combinations(freq, len(fset)-1)
            comb = list(comb)
            for c in comb:
                c = list(c)
                print(c,end = "->")
                for item in fset:
                    if item not in c:
                        print(item)
    
min_supp = 2
read_csv()
k=1
get_candidateset()
get_frequentset(min_supp)
k+=1
get_candidateset2()
get_candidateset2_count()
get_frequentset(min_supp)
k+=1
while C:
    make_next_itemset(k)
    get_candidate_count()
    prune()
    get_frequentset(min_supp)
    k+=1
print("Frequent Itemsets: ")
for freq in answer:
    print(freq)

# print("Association Rules: ")
# association_rules()
