from bs4 import BeautifulSoup as bs
import requests as r
from dataclasses import dataclass

def get_stat():
    pass

def get_query_string(first, last):

    query_string = "/players/" + last[0].lower() + "/"
    if len(last) < 5:
        first_name_length = 7 - len(last)
        query_string += last[0:len(last)] + first[0:first_name_length] + "01.html"
    
    else:
        query_string += last[0:5] + first[0:2] + "01.html"
    new_qs = query_string.lower()
    return new_qs

print(get_query_string("Lebron", "James"))



    