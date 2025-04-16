from .arguments import get_api_arguments
from .code_examples import get_api_examples
from .description import get_api_description
from .fields_and_connections import get_api_fields_or_connections
from .models import Mutation, MutationArgument, MutationReturn
from .returns import get_api_returns


def get_mutation_info(label, api_information_url):
    name = label

    print("Getting mutation description")
    description = get_api_description(api_information_url)

    print("Getting mutation arguments")
    arguments = get_api_arguments(api_information_url)

    print("Getting mutation returns")
    returns = get_api_returns(api_information_url, False, len(arguments) > 0)

    print("Getting mutation code examples")
    examples = get_api_examples(api_information_url)

    mutation = Mutation(
        name=name,
        description=description.strip(),
        arguments=[MutationArgument(
            name=argument[0],
            type=argument[1],
            required=len(argument[2]) > 0,
            description=argument[3].strip(),
        ) for argument in arguments],
        returns=[MutationReturn(
            name=return_[0],
            type=return_[1],
            description=return_[2].strip()
        ) for return_ in returns],
        examples=examples
    )

    print("Have the following for mutation: ", mutation)
    return mutation
