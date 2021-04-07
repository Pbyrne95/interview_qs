class mineSweeper:

    def insert_bombs(self,bombs,rows,columns):
        nested_arr = [[0] * columns for i in range(0,rows)] 

        for i in range(len(bombs)):
            nested_arr[bombs[i][0]][bombs[i][1]] = -1
        return nested_arr

    def insert_warning(self,arr):
        for i in range(len(arr)):
            # deffing legal moves 
            check_up  = i == 0
            check_down = i + 1 < len(arr)
            check_left = i - 1 < 0
            check_right = i + 1 >= len(arr[i])
            for j in range(0,len(arr[i])):
                # always check the left cell
                upward = i -1
                downward = i + 1
                up_right = j + 1
                up_left = j - 1
                current_pos = arr[i][j]

                if( up_left >= 0 ):
                    if(arr[i][up_left] == -1 and current_pos >= 0):
                        arr[i][j] += 1

                if( up_right < len(arr[i])) :
                    if arr[i][up_right] == -1 and current_pos >=0:
                        arr[i][j] +=1
                
                if check_down:
                    if (arr[downward][j] == - 1 and current_pos >= 0):
                        arr[i][j] += 1
                    if (arr[downward][up_left] == - 1 and current_pos >= 0):
                        arr[i][j] += 1
                    if (up_right < len(arr[i])):
                        if (arr[downward][up_right] == - 1 and current_pos >= 0):
                            arr[i][j] += 1

                if not check_up:
                    if (arr[upward][j] == -1 and current_pos >= 0):
                        arr[i][j] +=1 
                    if not check_left and j - 1 >= 0 :
                        if(arr[upward][up_left] == - 1 and current_pos >= 0):
                            arr[i][j] += 1
                    if not check_right and j + 1 < len(arr[i]):
                        if(arr[upward][up_right] == - 1 and current_pos >= 0):
                            arr[i][j] += 1
        return arr

    def flatten(self,arr):
        flats =  lambda l: sum(map(self.flatten,l),[]) if isinstance(l,list) else [l]
        return flats(arr)

if __name__ == "__main__":
    temp = mineSweeper()
    # print(temp.insert_warning(temp.insert_bombs([[0,0],[0,1]], 3, 4)))
    # print(temp.insert_warning(temp.insert_bombs([[0, 0], [0, 1], [1, 2]], 3, 4)))
    # print(temp.flatten(temp.insert_warning(temp.insert_bombs([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5))))
    x = temp.flatten(temp.insert_warning(temp.insert_bombs([[0, 2], [2, 0]], 3, 3)))
    check_1 = temp.flatten([[0, 1, -1],[1, 2, 1],[-1, 1, 0]])
    print(x)
    print(check_1)
    print(x == check_1)