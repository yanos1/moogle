import sys
import bs4
from HTML_functions import read_index_file, get_html_content, get_full_url

def get_relavent_sites(data):
    return read_index_file(data)


def words_dict():
    word_dict = dict()
    data = ""
    for site in get_relavent_sites(sys.argv[3]):
        html_content = get_html_content(get_full_url(sys.argv[2],site))
        soup = bs4.BeautifulSoup(html_content,"html.parser")
        for p in soup.find_all("p"):
            data += p.text
            data += "\n"
        list_of_words = data.replace("\t", " ").replace("\n", " ").split()
        for word in list_of_words:
            hafred_and_meshol(word_dict,site,word)
        data = ""
    return word_dict


def hafred_and_meshol(dic,site,word):
    if word in dic:
        dic[word][site] += 1
    else:
        dic[word] = {sit: 0 for sit in get_relavent_sites(sys.argv[3])}
        dic[word][site] = 1




