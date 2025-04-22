from shopagent.models import Object

from .code_examples import get_api_examples
from .description import get_api_description
from .fields_and_connections import get_api_fields_or_connections
from .returns import get_api_returns


def get_object_info(label, api_information_url):
    name = label
    description = get_api_description(api_information_url)
    fields_and_connections = get_api_fields_or_connections(api_information_url, True)
    returns = get_api_returns(api_information_url, False, len(fields_and_connections) > 0)
    examples = get_api_examples(api_information_url)

    obj = Object(
        name=name,
        description=description.strip(),
        fields_and_connections=fields_and_connections,
        examples=examples,
    )

    return obj
