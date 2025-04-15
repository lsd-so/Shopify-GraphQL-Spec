from api import get_api_information
from nav import get_top_level_operations

"""
Get the code examples by grabbing

GROUP BY => ul[class*="ExamplesList"]
SELECT => li

Then fetch the URL with appending (or replacing if already present)
example => [li string from ^]
code => the code obtainable from grabbing the content inside
code[title="Node.js"]

Where the title string is whatever EXAMPLE_LANGUAGE is set to above
"""

"""
Mutations =>
name -> label
description -> first matching div.markdown

arguments -> first matching one for the num in nth-of-type
div[data-testid="primary-column"] > div:nth-of-type(5) > div[data-testid="gql-list"]:first-of-type

returns -> second matching one for the num in nth-of-type for above

Queries =>

name -> label
description -> first matching div.markdown

arguments -> first matching one
"""

# LSD SQL to obtain information about an API endpoint provided a URL
API_INFORMATION_SQL = """
"""
# LSD SQL to obtain the description of an API endpoint
API_DESCRIPTION_SQL = """
api_description <| div.text > div.markdown |

FROM {api_information_url}
|> SELECT api_information
"""

API_ARGUMENTS_SQL = """
FROM https://shopify.dev/docs/api/admin-graphql/latest/mutations/apprevokeaccessscopes
|> GROUP BY dt[role="listitem"]
|> SELECT span.font-property AS argument, -- The name of the argument
div[class*="GqlListItemHeaderAnnotations_38 a AS type -- The data type of the argument

div[data-testid="primary-column"] > div:nth-of-type(3) > div[data-testid="gql-list"]:first-of-type dt

argument_container <| div:has(header>div>a#arguments) dl dt |
argument <| 
FROM {api_information_url}
"""


    # Looping over each navItem

    # the key is the shopify api breakdown name
    # looping over each child -> the label is one of Queries/Mutations/Objects
    # based on the label then go through respective flow over children of this child of getting elements from page based on function
    # when done with each of the nav item links inside the children of child append to categories
    

def main():
    print("Hello from shopify-graphql!")
    shopify_nav = get_top_level_operations()
    print("we got this for shopify nav")
    print(shopify_nav)
    api_information = get_api_information(shopify_nav)
    print("and we got this for api information")
    print(api_information)


if __name__ == "__main__":
    main()
