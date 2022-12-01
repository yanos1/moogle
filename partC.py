import sys
import bs4
from partA import get_full_url, get_html_content, read_index_file, create_pickle_file


def get_relavent_sites(data):
    return read_index_file(data)


def word_dict_creation():
    word_dict = dict()
    data = ""
    for site in get_relavent_sites(sys.argv[3]):
        html_content = get_html_content(get_full_url(sys.argv[2],site))
        soup = bs4.BeautifulSoup(html_content,"html.parser")
        for p in soup.find_all("p"):
            data += p.text
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

if __name__ == '__main__':
    create_pickle_file(sys.argv[4],word_dict_creation())

