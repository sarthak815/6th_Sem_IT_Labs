import csv
from itertools import combinations

rows = []
lastC = {}
C = {}
L = {}
answer = {}

def readCSV(fileloc='ap1.csv') :
    csvFile = open(fileloc, "r")
    csvreader = csv.reader(csvFile)
    for row in csvreader :
        rows.append(row)
    print(rows)

def getItemsetCount() :
    for row in rows :
        seenitems = []
        for item in row :
            if item != '' and item not in seenitems:
                seenitems.append(item)
                C[item] = C.get(item, 0) + 1
    print(C)

def getFrequentItemset(minsupport) :
    answer.update(L)
    L.clear()
    for k,v in C.items() :
        if v >= minsupport :
            L[k] = v
    print(L)
    print(answer, '*\n')

def secondCandidateItemset() :
    lastC.clear()
    lastC.update(L)
    C.clear()
    x = []
    for l1 in L.keys() :
        for l2 in L.keys() :
            if l1 >= l2 :
                continue
            x.append(l1)
            x.append(l2)
            C[str(x)] = 0
            x.clear()
    print(C)

def getCandidateCount() :
    for k in C.keys() :
        keylist = eval(k)
        for row in rows :
            flag = 0
            for item in keylist :
                if item not in row :
                    flag = 1
                    break
            if flag == 0 :
                C[k] += 1
    print(C)

def makeNextCandidateItemset() :
    lastC.clear()
    lastC.update(L)
    C.clear()
    x = []
    for l1str in L.keys() :
        for l2str in L.keys() :
            if l1str >= l2str :
                continue
            l1 = eval(l1str)
            l2 = eval(l2str)
            flag = 0
            for i in range(k-2) :
                if l1[i] != l2[i] :
                    flag = 1
                    break
            if flag == 0 :
                for i in range(k-2) :
                    x.append(l1[i])
                x.append(l1[k-2])
                x.append(l2[k-2])
                C[str(x)] = 0
                x.clear()
    print(C)

def prune() :
    xlist = []
    remlist = []
    for klast in lastC.keys() :
        listklast = eval(klast)
        xlist.append(listklast)
    for ky in C.keys() :
        klist = eval(ky)
        klist.sort()
        comb = combinations(klist,k-1)
        comb = list(comb)
        flag = 0
        for c in comb :
            c = list(c)
            if c not in xlist :
                flag = 1
                break
        if flag == 1 :
            remlist.append(str(ky))
    for remitem in remlist :
        C.pop(str(remitem))
    print(C)

def generateAssociationRules() :
    for freqset in answer.keys() :
        if(len(freqset) <= 1) :
            continue
        fset = eval(freqset)
        if (len(fset) == 2) :
            for item in fset :
                print(item, end=' -> ')
                for i2 in fset :
                    if i2 != item :
                        print(i2)
        else :    
            comb = combinations(fset, len(fset)-1)
            comb = list(comb)
            for c in comb :
                c = list(c)
                print(c, end=' ')
                for item in fset :
                    if item not in c :
                        print(' -> ', end=' ')
                        print(item)
        

# initialization
min_support = int(input("Enter minimum support: "))
k=1
readCSV()
# get C1
getItemsetCount()
# get L1
getFrequentItemset(min_support)
k+=1
#Next Iteration at k=2
secondCandidateItemset()
getCandidateCount()
getFrequentItemset(min_support)
k+=1
while C :
    makeNextCandidateItemset()
    getCandidateCount()
    prune()
    getFrequentItemset(min_support)
    k+=1
print("Frequent Dataset :")
for freqkey in answer.keys() :
    print(freqkey)

print('ASSOCIATION RULES')
generateAssociationRules()