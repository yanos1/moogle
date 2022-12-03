
import sys
from crawl import final_result,crawl
from page_rank import page_rank,start_dict
from words_dict import words_dict
from search import get_final_results, produce_relevant_pages, create_output_file
from HTML_functions import create_pickle_file


if sys.argv[1] == "crawl":
    create_pickle_file(sys.argv[4], final_result(crawl()))
elif sys.argv[1] == "page_rank":
    create_pickle_file(sys.argv[4], page_rank(start_dict()))
elif sys.argv[1] == "words_dict":
    create_pickle_file(sys.argv[4], words_dict())
elif sys.argv[1] == "search":
    create_output_file()
    get_final_results(produce_relevant_pages(sys.argv[3]), sys.argv[3])

