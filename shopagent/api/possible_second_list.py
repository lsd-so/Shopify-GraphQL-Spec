from .first_list import get_first_list
from .second_list import get_second_list


def get_possible_second_list(api_information_url, first_list_found):
    if first_list_found:
        return get_second_list(api_information_url)
    return get_first_list(api_information_url)
