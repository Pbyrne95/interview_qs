import re

file = "items.txt"
capacity = 165
max_profit = 0

def get_data(filename=file):
    return_dict = {}
    layered_rato = {}
    with open(filename,"r") as opened:
        lis =  opened.readlines()
        lis = [i for i in lis if i != " "]
        for i in lis:
            i = i.split(",") 
            i = [re.sub("\n","",j).strip() for j in i if i]
            if i[0] != "":              
                return_dict[int(i[0])] = int(i[1])
                ratio = round(int(i[1])/int(i[0]),4)
                layered_rato[ratio] = [int(i[0])]
                layered_rato[ratio].append(return_dict.get(int(i[0])))
    upper_bound = dict(sorted(layered_rato.items(), key= lambda x:x[0] ,reverse=True))
    return upper_bound      

def knapsack():
    dic = get_data()
    upper_lim = 0
    upper_prof = 0
    most_profitable_items = []
    p1=1
    found = False

    for k in dic.keys():

        if(upper_lim +  dic[k][0] <= capacity):
            upper_lim += dic[k][0]
            upper_prof+=dic[k][1]
            most_profitable_items.append(p1)
            found = upper_lim>=capacity

        if found:
            break
        p1+=1

    return upper_prof,most_profitable_items

w = [i[0] for i in list(get_data().values())]

v = [i[1] for i in list(get_data().values())]

def niave_recursion(n,c):
    " this is the exponential way --> very bad "
  
    if n == 0 or c == 0:
        result = 0
    
    elif w[n] > c:
        result = niave_recursion(n-1,c)
    else:
        temp_one = niave_recursion(n-1,c)
        temp_two = v[n] + niave_recursion(n-1,c-w[n])
        result = max(temp_one,temp_two)
    return result 


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1]
                          + K[i-1][w-wt[i-1]], 
                              K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]

if __name__ == "__main__":

    v = [i[1] for i in list(get_data().values())]
    w = [i[0] for i in list(get_data().values())]

    val = v
    wt = w
    W = 165
    n = len(val)

    print(knapsack())
    # print(knapSack(W, wt, val, n))