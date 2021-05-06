file = "items.txt"

def get_data(filename):
    return_dict = {}

    with open(filename,"r") as data:
        for line in data.readlines():
            print(line)

