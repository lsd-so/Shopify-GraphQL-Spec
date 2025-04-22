from shopagent.lsd import run_lsd
from shopagent.models import ObjectFieldOrConnection

from .first_list import get_first_list
from .second_list import get_api_second_list


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

def get_api_fields_or_connections(api_information_url, should_get_first_list=False):
    global HAS_API_FIELDS
    global HAS_API_FIELDS_AND_CONNECTIONS

    results = run_lsd(HAS_API_FIELDS.format(api_information_url=api_information_url))
    fields_or_connections_list = []
    if len(results) > 0:
        fields_or_connections_list = get_first_list(api_information_url) if should_get_first_list else get_api_second_list(api_information_url)

    results = run_lsd(HAS_API_FIELDS_AND_CONNECTIONS.format(api_information_url=api_information_url))
    if len(results) > 0:
        fields_or_connections_list = get_first_list(api_information_url) if should_get_first_list else get_api_second_list(api_information_url)

    if len(fields_or_connections_list) == 0:
        return []

    fields_or_connections = []
    for field_or_connection in fields_or_connections_list:
        name = field_or_connection[0]
        description = field_or_connection[3]
        field_type = field_or_connection[1]
        not_nullable = len(field_or_connection[2]) > 0

        fields_or_connections += [ObjectFieldOrConnection(
            name=name,
            type=field_type,
            description=description.strip(),
            not_nullable=not_nullable,
        )]

    return fields_or_connections
