from shopagent.lsd import run_lsd


API_DESCRIPTION_SQL = """
description <| div.text > div.markdown |

FROM {api_information_url}
|> SELECT description
"""


def get_api_description(api_information_url):
    global API_DESCRIPTION_SQL

    results = run_lsd(API_DESCRIPTION_SQL.format(api_information_url=api_information_url))
    return results[0][0] if len(results) > 0 else ""
