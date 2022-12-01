import pickle
import sys
from partA import create_pickle_file

def file_data(data):
    with open(data, "rb") as trafic_dict:
        file = pickle.load(trafic_dict)
    return file

def start_dict():
    r = {key:1 for key in file_data(sys.argv[4])}
    return r


def rank_calculation(old_dict, name, item):
    try:
        calc = old_dict[name] * (file_data(sys.argv[4])[name][item]/sum(file_data(sys.argv[4])[name].values()))
    except:
        return 0
    return calc


def new_r_update(old_dic):

    for iteration in range(int(sys.argv[3])):
        new = {key: 0 for key in file_data(sys.argv[4])}
        for item in new: #items are names
            for name in old_dic:
                new[item] += rank_calculation(old_dic,name,item)
        old_dic.update(new)

    return old_dic


if __name__ == '__main__':
    create_pickle_file(sys.argv[5],new_r_update(start_dict()))



