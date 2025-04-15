from .description import get_api_description
from .models import Query


def get_query_info(label, api_information_url):
    print("Here is where we are supposed to be getting query info")
    name = label
    description = get_api_description(api_information_url)
    arguments = []
    returns = []
    examples = []

    return Query(
        name=name,
        description=description,
        arguments=arguments,
        returns=returns,
        examples=examples,
    )
