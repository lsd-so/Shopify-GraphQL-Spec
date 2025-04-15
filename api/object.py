from .description import get_api_description
from .fields_and_connections import get_api_fields_or_connections
from .models import Object
from .returns import get_api_returns


def get_object_info(label, api_information_url):
    print("here is where we would be getting object info")
    name = label
    description = get_api_description(api_information_url)
    fields_and_connections = get_api_fields_or_connections(api_information_url)
    fields_and_connections_found = len(fields_and_connections) > 0
    returns = get_api_returns(api_information_url)
    examples = get_api_examples(api_information_url)

    return Object(
        name=name,
        description=description,
        fields_and_connections=fields_and_connections,
        examples=examples,
    )
