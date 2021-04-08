import copy


def is_rotation(given_arr,n):
    rot = [[0] * n  for i in range(0,n)]
    column_change = n 

    for i in range(n):
        column_change -= 1 
        row_to_change = 0
        for j in range(len(given_arr[i])):
            rot[row_to_change][column_change] = given_arr[i][j]
            row_to_change+=1
    return rot  

def flatten(arr):
    flats =  lambda l: sum(map(flatten,l),[]) if isinstance(l,(list,tuple)) else [l]
    return flats(arr)

a1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
a2 = [[7, 4, 1],[8, 5, 2],[9, 6, 3]]
b2 = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
b_check = [[13, 9, 5, 1],[14, 10, 6, 2],[15, 11, 7, 3],[16, 12, 8, 4]]


a_new = is_rotation(a1,3)
b_new = is_rotation(b2,4)
print(flatten(a_new) ==  flatten(a2))
print(flatten(b_new) == flatten(b_check))