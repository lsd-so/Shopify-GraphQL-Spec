from lsd import run_lsd

from .first_list import get_first_list


HAS_API_ARGUMENTS_SQL = """
arguments_anchor <| a#arguments |

FROM {api_information_url}
|> GROUP BY arguments_anchor
|> SELECT arguments_anchor
"""


def get_api_arguments(api_information_url):
    global HAS_API_ARGUMENTS_SQL

    results = run_lsd(HAS_API_ARGUMENTS_SQL.format(api_information_url=api_information_url))
    if len(results) == 0:
        return []

    first_list = get_first_list(api_information_url)
    return first_list[0] if len(first_list) > 0 else []
