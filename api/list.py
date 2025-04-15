from lsd import run_lsd


GET_LIST_OF_ITEMS_SQL = """
list_item <| div[data-testid="primary-column"] > div:nth-of-type({n}) > div[data-testid="gql-list"]:first-of-type dt |

FROM {api_information_url}
|> GROUP BY list_item
|> SELECT list_item
"""


def get_list_of_items(api_information_url, n):
    global GET_LIST_OF_ITEMS_SQL
    return run_lsd(GET_LIST_OF_ITEMS_SQL.format(api_information_url=api_information_url, n=str(n)))
