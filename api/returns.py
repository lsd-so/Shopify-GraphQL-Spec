from lsd import run_lsd

from .second_list import get_api_second_list


HAS_API_RETURNS_SQL = """
returns_anchor <| a#possiblereturns |

FROM {api_information_url}
|> GROUP BY returns_anchor
|> SELECT returns_anchor
"""


def get_api_returns(api_information_url):
    global HAS_API_RETURNS_SQL

    results = run_lsd(HAS_API_RETURNS_SQL)
    if len(results) == 0:
        return []

    second_list = get_api_second_list(api_information_url)
    return [nested_list[0] for nested_list in second_list] if len(second_list) > 0 else []
