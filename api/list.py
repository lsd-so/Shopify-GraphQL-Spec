from lsd import run_lsd


GET_LIST_OF_ITEMS_SQL = """
list_item <| div[data-testid="primary-column"] > div:nth-of-type({n}) > div[data-testid="gql-list"]:first-of-type dl > div[class*="GqlListItem"] |
list_item_name <| dt .group\/hashtarget > span |
list_item_type <| div > a.underline |
list_item_non_nullable <| span[class*="NonNullChip"]! |
list_item_description <| dd div.markdown |


FROM {api_information_url}
|> GROUP BY list_item
|> SELECT list_item_name, list_item_type, list_item_non_nullable, list_item_description
"""


def get_list_of_items(api_information_url, n):
    global GET_LIST_OF_ITEMS_SQL
    return run_lsd(GET_LIST_OF_ITEMS_SQL.format(api_information_url=api_information_url, n=str(n)))
