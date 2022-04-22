import numpy as np
import pandas as pd
from itertools import permutations  


def combine_sets(final_set, current_set):
    for cur in current_set:
        final_set.append(cur)
    return final_set

def get_permutations(item):
    no = len(item)
    item = list(item)
    valid_first_associations = []
    valid_to_associations = []
    for i in range(1, no):
        curr_set = list(permutations(item, i))

        for it in curr_set:
            curr_ass = item[:]
            for ele in it:
                curr_ass.remove(ele)
            valid_to_associations.append(tuple(curr_ass))
        combine_sets(valid_first_associations, curr_set)
        
    return valid_first_associations, valid_to_associations

def get_associations(frequent_sets, dataset):
    for freq in frequent_sets:
        if len(freq) > 1:
            first_ass, to_ass = get_permutations(freq)
            for i in range(0, len(first_ass)):
                conf = 0
                sup = 0
                # print(f"Item set {first_ass[i]} => {to_ass[i]} support = {sup}, confidence = {conf}")
                new_item = [l for l in first_ass[i]]
                for l in to_ass[i]:
                    new_item.append(l)
                # print(new_item)
                # print(set(first_ass[i]))
                for data in dataset:
                    # print(data, new_item)
                    if set(new_item).issubset(set(data)):
                        sup+=1
                    # print(set(data), set(first_ass[i]))
                    if set(first_ass[i]).issubset(set(data)):
                        conf+=1
                        # print("HERE")
                conf = sup/conf
                sup = sup/len(dataset)
                print(f"Item set {first_ass[i]} => {to_ass[i]} support = {sup}, confidence = {conf}")
            # print(first_ass)



if __name__=="__main__":
    print(get_permutations(('bread', 'butter', 'cheese')))