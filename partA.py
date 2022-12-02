import urllib.parse
import pickle
import sys
import bs4
import requests


def read_index_file(url):
    with open(url,"r") as index_file:
        final = []
        list_of_relevant_sites = index_file.readlines()
        for item in list_of_relevant_sites:
            final.append(item.strip())
    return final


def get_full_url(base_url,relative_url):
    return urllib.parse.urljoin(base_url, relative_url)


def get_html_content(html_file):
    reponse = requests.get(html_file)
    return reponse.text



def basic_dic_creation():
    base_dict = {}
    soup = bs4.BeautifulSoup(get_html_content(sys.argv[2]), "html.parser")
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            base_dict[target] = {}

    return base_dict


def read_file_contents(url):
    list_of_targets = []
    soup = bs4.BeautifulSoup(get_html_content(url), "html.parser")
    for p in soup.find_all("p"):
        for link in p.find_all("a"):
            target = link.get("href")
            if target in read_index_file(sys.argv[3]):
                list_of_targets.append(target)

    return list_of_targets

def all_files_contents():
    trafic_dic = basic_dic_creation()
    for key in trafic_dic: # lets say dumbledore
        full_url = get_full_url(sys.argv[2],key) #dumbledore page
        target_urls = read_file_contents(full_url)
        for target in target_urls: #target is a name again
            if target in trafic_dic[key]:
                trafic_dic[key][target] +=1
            else:
                trafic_dic[key][target] = 1
    return trafic_dic


def create_pickle_file(configuration_argument,data):
    with open(configuration_argument,"wb") as out_file:
        pickle.dump(data,out_file)

def final_result(dict):
    for dic in dict.values():
        for key in read_index_file(sys.argv[3]):
            if key not in dic:
                dic[key] = 0
    return dict


if __name__ == '__main__':
    print(final_result(all_files_contents()))
    create_pickle_file(sys.argv[4],final_result(all_files_contents()))

