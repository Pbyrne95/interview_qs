from random import randrange, shuffle,randint

def quicksort(list, start, end):
    """ Uses recurssion , partions and parrell swop a list until the start idx is > end_idx """

    # initial base_case -> to stop recurssion
    if start >= end:
        return 
    
    # generates random number in range from start -> end to garentee efficency 
    pivot_idx = randrange(start,end)

    pivot_element = list[pivot_idx]

    # parrell swop random element with the end paremeter 
    list[end],list[pivot_idx] = list[pivot_idx],list[end]

    lesser_then_pointer = start 

    for idx in range(start,end):
        if list[idx] < pivot_element:

            list[idx],list[lesser_then_pointer] = list[lesser_then_pointer],list[idx]
            lesser_then_pointer += 1

    # parrell swoping of end element to lesser then pointer 
    list[end],list[lesser_then_pointer] = list[lesser_then_pointer],list[end]

    print("{0} successfully partitioned".format(list[start: end + 1]))

    # recursive call on left side of partition
    quicksort(list,start,lesser_then_pointer-1)

    # recursive call on right side of partition
    quicksort(list,lesser_then_pointer+1,end)


" *** RANDOM TESTS *** " 
x = [5,3,1,7,4,6,2,8]
x1 = [randint(1,1000) for i in range(1,100)]
print(x1)
print(quicksort(x1 ,0 , len(x1)-1))
print(x1)
