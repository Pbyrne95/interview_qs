import re

file = "items.txt"

def get_data(filename):
    return_dict = []
    index = 1
    with open(filename,"r") as data:
        for line in [re.sub('\n','',i) for i in data.readlines() if i not in [" ",",",'']]:
            if line:
                comma = str(line).rfind(",")
                return_dict.append((index, int(line[:comma].strip()),int(line[comma+1:].strip())))
                index+=1
    return return_dict
                
# dic = get_data(file)
# for i in dic:
#     print(i,dic[i])
 
test_bound = {1:[3,2],
              2:[8,12],
              3:[6,9],
              4:[2,5]
              }

def brute_force(items,max_weight=165):
    def power_set(items):
        res = [[]]
        for item in items:
            res.extend([r+[item] for r in res])
        return res
    
    knapsack=[]
    best_weight = 0
    best_value = 0

    for item_set in power_set(items):
        set_weight = sum([e[1] for e in item_set])
        set_value =  sum([e[2] for e in item_set])
        if set_weight <= max_weight and set_value > best_value:
            best_weight = set_weight
            best_value = set_value
            knapsack = [i[0] for i in  item_set]

    return knapsack , best_weight , best_value

# x = get_data(file)
# print(brute_force(x))
# print(10**2)

