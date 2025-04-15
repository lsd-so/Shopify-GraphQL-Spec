from .arguments import get_api_arguments
from .code_examples import get_api_examples
from .description import get_api_description
from .models import Query, QueryArgument, QueryReturn
from .returns import get_api_returns


def get_query_info(label, api_information_url):
    name = label

    print("Getting query description")
    description = get_api_description(api_information_url)

    print("Getting query arguments")
    arguments = get_api_arguments(api_information_url)

    print("Getting query returns")
    returns = get_api_returns(api_information_url, False, len(arguments) > 0)

    print("Getting query examples")
    examples = get_api_examples(api_information_url)

    return Query(
        name=name,
        description=description,
        arguments=[QueryArgument(
            name=argument[0],
            type=argument[1],
            required=len(argument[2]) > 0,
            description=argument[3].strip()
        ) for argument in arguments],
        returns=[QueryReturn(
            name=r[0],
            type=r[1],
            description=r[2],
        ) for r in returns],
        examples=examples,
    )
