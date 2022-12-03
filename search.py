import sys
from HTML_functions import file_data


def get_word_dict():
    word_dict = file_data(sys.argv[4])
    return word_dict


def get_rank_dict():
    return file_data(sys.argv[3])


def sort_rank_dict(rank_dict):
    return dict(sorted(rank_dict.items(), key=lambda item:item[1],reverse=True))


def produce_relevant_pages(query):
    query_list = query.split()
    for word in query_list:
        if word not in get_word_dict():
            query_list.remove(word)
    sorted_by_ranks = sort_rank_dict(get_word_dict())
    relavent_sites = {}
    for site in sorted_by_ranks:
        count = 0
        for word in query_list:
            if get_word_dict()[word][site] > 0:
                count+=1
        if count == len(query_list):
            relavent_sites[site] = get_word_dict()[site]
        if len(relavent_sites) == int(sys.argv[6]):
            break
    return relavent_sites


def get_word_score(query,site):
    words = query.split()
    dict_of_words = dict()
    for word in words:
        try:
            dict_of_words[word] = get_word_dict()[word][site]
        except:
            pass

    return sorted(dict_of_words.items(), key= lambda item:item[1])[0][1]


def get_final_results(relavent_sites,query):
    dic_of_final_scores = dict()
    for site in relavent_sites:
        score = get_rank_dict()[site]* get_word_score(query,site)
        dic_of_final_scores[site] = score
    return sort_rank_dict(dic_of_final_scores)


def print_search_results(dic):
    for site in dic:
        print(f"{site} {dic[site]}")


def create_output_file():
    list_of_queries = ["scar", "Crookshanks", "Horcrux", "Pensieve McGonagall", "broom wand cape"]
    result = open("results.txt","w")
    for query in list_of_queries:
        data = get_final_results(produce_relevant_pages(query),query)
        for item in data:
            result.write(f"{item} {data[item]}")
            result.write("\n")
        result.write("**********")
        result.write("\n")
    result.close()









