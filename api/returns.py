from lsd import run_lsd

from .first_list import get_first_list
from .second_list import get_api_second_list
from .third_list import get_api_third_list


HAS_API_RETURNS_SQL = """
returns_anchor <| a#possiblereturns |

FROM {api_information_url}
|> GROUP BY returns_anchor
|> SELECT returns_anchor
"""


def get_api_returns(api_information_url, start_at_second, prior_list_found):
    global HAS_API_RETURNS_SQL

    results = run_lsd(HAS_API_RETURNS_SQL.format(api_information_url=api_information_url))
    if len(results) == 0:
        return []

    returns_list = []
    if not start_at_second and not prior_list_found:
        returns_list = get_first_list(api_information_url)
    elif start_at_second and not prior_list_found:
        returns_list = get_api_second_list(api_information_url)
    elif start_at_second and prior_list_found:
        returns_list = get_api_third_list(api_information_url)

    return returns_list
