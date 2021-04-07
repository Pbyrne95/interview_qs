class arr_challenges:
    def is_rotation(self,list1,list2):
        """ check if one array is a rotation of the other """
        if list1[0] not in list2 and len(list1) != len(list2):
            return False
        key = list1[0]
        index_to,flag = 0,False
        for i in range(len(list2)):
            if list2[i] == key:
                index_to = i
                flag = True
                break
        if not flag:
            return False         
        return list2[index_to:] + list2[:index_to] == list1
    
    def non_rep(self,strs):
        """ finds the first non repeating charecter in an array """
        import collections 
        lis = list({k:v for k,v in dict(collections.Counter([i for i in strs])).items() if v <= 1}.keys())
        return lis[0] if len(lis) >=1 else None
    

    def is_one_away(self,strs1,strs2): 
        """ Uses helper functions diff_size and same_size to determine if an array is one element away from the other"""      
        if len(max(strs1,strs2, key=len)) - len(min(strs1,strs2 , key=len)) > 1:
            return False
        elif (max(len(strs1),len(strs2)) - min(len(strs1),len(strs2))) == 1:
            return self.diff_size(strs1,strs2)
        else:
            return self.same_size(strs1,strs2)

    def diff_size(self,strs1,strs2):
        max_l = max(strs1,strs2, key=len)
        min_l = min(strs1,strs2 , key=len)

        max_set = [i for i in max_l if i not in min_l]
        if len(max_set) > 1:
            return False
        return "".join(sorted(list(max_l))) ==  "".join(sorted(list(min_l)+max_set))
        
    def same_size(self,strs1,strs2):
        count = 0
        for i in range(0,len(strs1)):
            if strs1[i] != strs2[i]:
                count+=1
                if count > 1:
                    return False
    
        return True

if __name__ == "__main__":
    temp = arr_challenges()
    print(temp.is_one_away("abcde", "abcd"))  # should return True
    print(temp.is_one_away("abde", "abcde"))  # should return True
    print(temp.is_one_away("a", "a"))  # should return True
    print(temp.is_one_away("abcdef", "abqdef"))  # should return True
    print(temp.is_one_away("abcdef", "abccef")) # should return True
    print(temp.is_one_away("abcdef", "abcde"))  # should return True
    print(temp.is_one_away("aaa", "abc"))  # should return False
    print(temp.is_one_away("abcde", "abc"))  # should return False
    print(temp.is_one_away("abc", "abcde"))  # should return False
    print(temp.is_one_away("abc", "bcc"))  # should return False