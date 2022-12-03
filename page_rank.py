import sys
from HTML_functions import file_data


def start_dict():
    r = {key:1 for key in file_data(sys.argv[4])}
    return r


def rank_calculation(old_dict, name, item):
    try:
        calc = old_dict[name] * (file_data(sys.argv[4])[name][item]/sum(file_data(sys.argv[4])[name].values()))
    except:
        return 0
    return calc


def page_rank(old_dic):

    for iteration in range(int(sys.argv[3])):
        new = {key: 0 for key in file_data(sys.argv[4])}
        for item in new: #items are names
            for name in new:
                new[item] += rank_calculation(old_dic,name,item)
        old_dic.update(new)

    return old_dic





