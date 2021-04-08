def radix_sort(to_be_sorted):
    """ Non - comparasion sort -> uses base 10  """

    maximum_value = str(max(to_be_sorted))
    max_exponent = len(maximum_value)
    being_sorted = to_be_sorted[:]

    for exponent in range(max_exponent):

        position = exponent + 1
        index = -position
        digits = [[] for i in range(0,10)]

        for number in being_sorted:
            number_as_string = str(number)

            try:
                digits[int(number_as_string[index])].append(number)
                
            except IndexError:
                digits[0].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted



unsorted_list = [830, 921, 163, 373, 961, 559, 89, 199, 535, 959, 40, 641, 355, 689, 621, 183, 182, 524, 1]
print(radix_sort(unsorted_list))
print(unsorted_list)