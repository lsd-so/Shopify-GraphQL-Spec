from time import sleep

from constants import EXAMPLE_LANGUAGE
from lsd import run_lsd

from .models import CodeExample


CODE_EXAMPLES_EXISTENCE_SQL = """
PORTAL <| OPEN |

container <| ul[class*="Examples"] li |
item <| li |

FROM {api_information_url}
|> GROUP BY container
|> SELECT item
"""

CODE_EXAMPLE_SQL = """
PORTAL <| OPEN |

example_code_container <| div[class*="Examples"] |
example_code <| code[title="{language}"] |

FROM {modified_url}
|> GROUP BY example_code_container
|> SELECT example_code
"""


def get_api_example_code(api_information_url, example_description, retrying=False):
    simplified_language = EXAMPLE_LANGUAGE.lower() if "." not in EXAMPLE_LANGUAGE else EXAMPLE_LANGUAGE[:EXAMPLE_LANGUAGE.index(".")].lower()
    simplified_example = example_description.replace(" ", "-").lower()
    modified_url = f"{api_information_url}?language={simplified_language}&example={simplified_example}"

    try:
        actual_example = run_lsd(CODE_EXAMPLE_SQL.format(language=EXAMPLE_LANGUAGE, modified_url=modified_url))
    except Exception as e:
        # Likely no rows returned from this page
        return ''

    if len(actual_example) == 0 or len(actual_example[0]) == 0:
        return ''

    if len(actual_example[0]) > 0 and ('Failed to obtain new columns' in actual_example[0][0] or 'Failed to [FROM]' in actual_example[0][0]):
        if retrying:
            return ''
        sleep(1)
        return get_api_example_code(api_information_url, example_description, True)

    return actual_example[0][0] if type(actual_example[0]) is list else actual_example[0]

def get_available_examples(api_information_url):
    available_examples = run_lsd(CODE_EXAMPLES_EXISTENCE_SQL.format(api_information_url=api_information_url))

    if len(available_examples) == 0:
        return []

    if type(available_examples[0]) is list:
        available_examples = [item for row in available_examples for item in row]

    if 'Failed to obtain new columns' in available_examples[0]:
        sleep(1)
        return get_available_examples(api_information_url)

    return available_examples

def get_api_examples(api_information_url):
    available_examples = get_available_examples(api_information_url)

    if len(available_examples) == 0:
        return []

    if type(available_examples[0]) is list:
        available_examples = [item for row in available_examples for item in row]

    api_examples = []
    for code_example in available_examples:
        actual_code = get_api_example_code(api_information_url, code_example)
        if len(actual_code) > 0:
            api_examples += [CodeExample(
                description=code_example.strip(),
                code=actual_code,
            )]

    return api_examples
