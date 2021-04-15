class num_gen:
    """ Quistion 1 """
    def even_gen(self,range_of,divisor=3):
        
        for i in range(range_of):
            if i % 3 == 0:
                yield i

    def produce_nums(self,range_of,divisor=3):
        return sum(list(self.even_gen(range_of,divisor)))


def nums_up_to(num):
    """ Quistion 2 """
    if num:
        return_lis=[]
        counter = 1
        while( len(return_lis) - 1 < num):
            temp = []
            for i in range(1,counter):
                temp.append(i)
            counter+=1
            return_lis.append(temp)
        
        return [i for i in return_lis if i != []]
    return []

if __name__ == "__main__":
    print(nums_up_to(0))
    print(nums_up_to(1))
    print(nums_up_to(2))
    print(nums_up_to(3))
    print(nums_up_to(4))

    temp = num_gen()
    print(temp.produce_nums(102030))
