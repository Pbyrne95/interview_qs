import math


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    for i in range(math.ceil(n/2)):
        for j in range(math.floor(n/2)):
            tmp = [-1] * 4
            (current_i, current_j) = (i, j)
            for k in range(4):
                tmp[k] = given_array[current_i][current_j]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
            for k in range(4):
                given_array[current_i][current_j] = tmp[(k - 1) % 4]
                (current_i, current_j) = rotate_sub(current_i, current_j, n)
    return given_array


def rotate_sub(i, j, n):
    return j, n - 1 - i

def flatten(arr):
    flats =  lambda l: sum(map(flatten,l),[]) if isinstance(l,(list,tuple)) else [l]
    return flats(arr)

a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# rotate(a1, 3) should return:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
print(rotate(a1,3))
