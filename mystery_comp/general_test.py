cache = {}
class fib:
    """ Quistion 1 """
    def __init__(self):
        self.outputList = []

    def first_n_fub(self,n):

        if n in cache:
            return cache[n]

        if n == 1 or n == 2:
            return 1

        else:
            result = self.first_n_fub(n-1) + self.first_n_fub(n-2)
            cache[n] = result
            return result

    def get_first_100(self,runLength):   
        counter = 2
        while( len(self.outputList) < runLength + 1 ):
            curr = self.first_n_fub(counter)
            if curr % 2 == 0:
                self.outputList.append(self.first_n_fub(counter))
            counter+=1
        return sum(self.outputList)

def common_elems(lis_one,lis_two):
    """ Quistion 2 """
    return list(sorted(set([i for i in lis_one if i in lis_two])))

def is_all_even(num):
    """ Quistion 3 """
    return ( len([int(i) for i in str(num) if int(i) % 2 == 0])  > 0 )

def sum_til_len(num,leng=4):
    """ Quistion 4 """
    return sum([int(str(num) * i) for i in range(1,leng+1)])
    

if __name__ == "__main__":
    print(sum_til_len(3)) 
    print(common_elems([1,1,1,1,1,1,1,1,1,4,5,9,3,49586,9102,32,999999,32,32,32,32,32],[1,1,1,1,1,1,1,1,1,1,2,3,4,40495,5,6,7,8,32,32,32,32,9,9,9,9,9,9,9]))
    temp = fib()
    print(temp.get_first_100(100))
    print(is_all_even(124))