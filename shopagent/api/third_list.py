from .list import get_list_of_items


def get_api_third_list(api_information_url):
    counter = 0
    first_list_found = False
    second_list_found = False
    third_list = []

    while len(third_list) == 0 or not first_list_found or not second_list_found:
        third_list = get_list_of_items(api_information_url, counter)
        if len(third_list) > 0 and not first_list_found:
            third_list = []
            first_list_found = True
        elif len(third_list) > 0 and not second_list_found:
            third_list = []
            second_list_found = True

        counter += 1

    return third_list
