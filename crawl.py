from HTML_functions import get_html_content,get_full_url,read_index_file
import sys
import bs4


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


def crawl():
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


def final_result(dict):
    for dic in dict.values():
        for key in read_index_file(sys.argv[3]):
            if key not in dic:
                dic[key] = 0
    return dict



