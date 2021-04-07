class challenges:
    def higest_occ(self,arr):
        import collections
        return list(dict(sorted(dict(collections.Counter(arr)).items(), \
            key = lambda x: x[1] , reverse = True)).keys())[0]
        
    def common_elem(self,list_one,list_two):
        return [i for i in list_two if i in set(list_one)]   

  
if __name__ == "__main__":
    temp = challenges()
    # print(temp.higest_occ([3,3,1,3,2,1]))
    # print(temp.higest_occ([0, -1, 10, 10, -1, 10, -1, -1, -1, 1]))
    # list_a1 = [1, 3, 4, 6, 7, 9]
    # list_a2 = [1, 2, 4, 5, 9, 10]

    # list1 = [1, 2, 3, 4, 5, 6, 7]
    # list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    # list2b = [4, 5, 6, 7, 1, 2, 3]
    # print(temp.non_rep("abcab")) # should return 'c'
    # print(temp.non_rep("abab")) # should return None
    # print(temp.non_rep("aabbbc")) # should return 'c'
    # print(temp.non_rep("aabbdbc")) # should return 'd'
    # print(temp.is_rotation(list1,list2b))


