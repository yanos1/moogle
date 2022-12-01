import sys
from partB import file_data
from partC import get_relavent_sites

#produce max results by choosing top 5 graded sites that contain all words of the query

word_dict = file_data(sys.argv[5])
rank_dict = file_data(sys.argv[4])




def sort_rank_dict(rank_dict):
    return dict(sorted(rank_dict.items(), key=lambda item:item[1],reverse=True))


def produce_relevant_pages(query):
    query_list = query.split()
    for word in query_list:
        if word not in word_dict:
            query_list.remove(word)
    sorted_by_ranks = sort_rank_dict(rank_dict)
    relavent_sites = {}
    for site in sorted_by_ranks:
        count = 0
        for word in query_list:
            if word_dict[word][site] > 0:
                count+=1
        if count == len(query_list):
            relavent_sites[site] = rank_dict[site]
        if len(relavent_sites) == int(sys.argv[6]):
            break
    return relavent_sites


def get_word_score(query,site):
    words = query.split()
    dict_of_words = dict()
    for word in words:
        try:
            dict_of_words[word] = word_dict[word][site]
        except:
            pass

    return sorted(dict_of_words.items(), key= lambda item:item[1])[0][1]


def get_final_results(relavent_sites,query):
    dic_of_final_scores = dict()
    for site in relavent_sites:
        score = rank_dict[site]* get_word_score(query,site)
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


if __name__ == '__main__':
    #print_search_results(get_final_results(produce_relevant_pages(sys.argv[3]),sys.argv[3]))
    create_output_file()
    get_final_results(produce_relevant_pages(sys.argv[3]),sys.argv[3])









