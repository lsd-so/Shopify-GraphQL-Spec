from .code_examples import get_api_examples
from .description import get_api_description
from .fields_and_connections import get_api_fields_or_connections
from .models import Object
from .returns import get_api_returns


def get_object_info(label, api_information_url):
    name = label

    print("Getting object description")
    description = get_api_description(api_information_url)

    print("Getting object fields/connections")
    fields_and_connections = get_api_fields_or_connections(api_information_url, True)

    print("Getting object returns")
    returns = get_api_returns(api_information_url, False, len(fields_and_connections) > 0)

    print("Getting object examples")
    examples = get_api_examples(api_information_url)

    return Object(
        name=name,
        description=description,
        fields_and_connections=fields_and_connections,
        examples=examples,
    )
