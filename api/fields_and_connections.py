from lsd import run_lsd

from .first_list import get_first_list


HAS_API_FIELDS = """
api_fields <| a#fields |

FROM {api_information_url}
|> GROUP BY api_fields
|> SELECT api_fields
"""

HAS_API_FIELDS_AND_CONNECTIONS = """
api_fields_and_connections <| a#fieldsandconnections |

FROM {api_information_url}
|> GROUP BY api_fields_and_connections
|> SELECT api_fields_and_connections
"""

def get_api_fields_or_connections(api_information_url):
    global HAS_API_FIELDS
    global HAS_API_FIELDS_AND_CONNECTIONS

    results = run_lsd(HAS_API_FIELDS)
    if len(results) > 0:
        return get_first_list(api_information_url)

    results = run_lsd(HAS_API_FIELDS_AND_CONNECTIONS.format(api_information_url=api_information_url))
    if len(results) > 0:
        return get_first_list(api_information_url)

    return []
