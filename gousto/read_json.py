import json
import os 
from decouple import config
import glob
import numpy as np

"CONSTANT VARS -> TO BE USED THROUGHOUT "

ROOT_STR = config("route_one")
FILENAMES = ["orders.json","boxes.json"]


def get_json_data(file_name,root_str=ROOT_STR):
    """ OPENS A JSON FILE LOCATED ANYWHERE ON THE LOCAL OS SYSTEM """
    if file_name not in os.listdir():
        try:
            file_found = [i for i in glob.glob(root_str+"/**/*.json",recursive=True) if file_name in i]
            if file_found:
                return open_j_file(file_found[0])
            return None

        except IOError:
            return None
            
    else:
        return open_j_file(file_name)


def open_j_file(file_name):
    """ returns a the data contained in a file """
    try:
        with open(file_name,"r") as f: return json.load(f)
    except IOError:
        return None


class calc_demension_class:
    def cm_to_mm(self,data):
        " turns cm to mm "
        return data * 10

    def surface_are(self,l,d,h):
        " calculate the surface area "
        return 2 * ( l * d + d * h + h * l)

    def calc_box_volume(self,a,w,d):
        " The actual volume inside of the box"
        return (a * w * d)/1000
    
    def space_radius(self,l,d,h):
        " Just incase it is needed "
        n = l **2 + d**2 + h ** 2
        return n ** .5

area_functions = calc_demension_class()

def get_total_volume(data):
    output_dict = dict()
    idx = 0 
    for dicts in data:
        total_cost = 0
        for ing_arr in dicts.get("ingredients"):
            total_cost += ing_arr.get("volumeCm3")
        output_dict[dicts.get("id")] = area_functions.cm_to_mm(total_cost)
    return output_dict

               
def convert_dem_vol(boxes_data):
    for dicts in boxes_data:
        
        volumes = (list(dicts.get("dimensions").values()))
        box_volumes = area_functions.calc_box_volume(volumes[0],volumes[1],volumes[-1])
        dicts["dimensions"] = area_functions.cm_to_mm(box_volumes)

    return boxes_data

def calculate_difference(orders_data, boxes_data):
    amount_each_box_type = {i.get("dimensions"):0 for i in boxes_data}
    lis = sorted(list(amount_each_box_type.keys()),reverse=True)
    carbon_sort_lrg_smal = {i.get("dimensions"):i.get("co2FootprintKg") for i in boxes_data}

    # iterate through orders_data comepare id : value -> compare_data.get(dimensions)
    for enteries in orders_data:
        order_volume = orders_data.get(enteries)
        # # for amounts in lis -> search for amount less then order_volume 
        for amounts in lis[::-1]:
            if order_volume <= amounts:
                amount_each_box_type[amounts] += 1 
                break
                
    total_amount_actaul = sum([(k,(v*carbon_sort_lrg_smal.get(k)))[1] for k,v in amount_each_box_type.items()])
    total_amount_max = sum([v for v in amount_each_box_type.values()]) * max(list(carbon_sort_lrg_smal.values()))
    
    return total_amount_max - total_amount_actaul > 1000.0 
    

if __name__ == "__main__":

    orders_dict = get_json_data(FILENAMES[0])
    boxes = get_json_data(FILENAMES[1])
    
    
    orders_cleaned = get_total_volume(orders_dict)
    boxes_cleaned = convert_dem_vol(boxes)
    large_demension = np.prod([20,100,50])/1000

    print(calculate_difference(orders_cleaned,boxes_cleaned))
