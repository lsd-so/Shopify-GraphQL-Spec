from shopagent.lsd import run_lsd

from .list import get_list_of_items


def get_first_list(api_information_url):
    counter = 0
    first_list = []
    while len(first_list) == 0:
        first_list = get_list_of_items(api_information_url, counter)
        counter += 1

    return first_list
