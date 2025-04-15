from .arguments import get_api_arguments
from .description import get_api_description
from .fields_and_connections import get_api_fields_or_connections
from .models import Mutation, MutationArgument, MutationReturn
from .returns import get_api_returns


def get_mutation_info(label, api_information_url):
    name = label
    description = get_api_description(api_information_url)
    arguments = get_api_arguments(api_information_url)
    returns = get_api_returns(api_information_url)
    examples = []

    return Mutation(
        name=name,
        description=description,
        arguments=[MutationArgument(
            name=argument[0],
            type=argument[1],
            required=len(argument[2]) > 0,
            description=argument[3],
        ) for argument in arguments],
        returns=[MutationReturn(
            name=return_[0],
            type=return_[1],
            description=return_[2]
        ) for return_ in returns],
        examples=examples
    )
