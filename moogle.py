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
