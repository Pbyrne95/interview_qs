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

def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      # Write your code here
      if index or weight == 0:
        matrix[index][weight] = 0
      elif weights[index-1] <= weight:
        including = values[index-1] + weights[weights-[index-1]]
        excluding = matrix[index-1][weight]
        matrix[index][weight] = max(including,excluding)
      else:
        matrix[index][weight] = matrix[index - 1][weight]
  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

x = get_data(file)
print(brute_force(x))
print(10**2)

