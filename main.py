import json

from api import get_api_information, get_api_examples
from nav import get_top_level_operations


def main():
    shopify_nav = get_top_level_operations()
    api_information = get_api_information(shopify_nav)

    with open("shopify_api.json", "w") as shopify_api_file:
        json.dump(api_information.model_dump(), shopify_api_file)


if __name__ == "__main__":
    main()
