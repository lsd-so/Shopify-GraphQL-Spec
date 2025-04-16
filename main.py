import json
import os
import sys

from rich import print

from api import get_api_information, get_api_examples, ShopifyAPI
from nav import get_top_level_operations


def get_data():
    shopify_nav = get_top_level_operations()
    api_information = get_api_information(shopify_nav)

    with open("shopify_api.json", "w") as shopify_api_file:
        json.dump(api_information.model_dump(), shopify_api_file)


def print_data():
    if not os.path.exists("shopify_api.json"):
        sys.exit("Missing [shopify_api.json] file")
        return

    with open("shopify_api.json", "r") as shopify_api_file:
        data = json.load(shopify_api_file)
        api_information = ShopifyAPI(**data)

        print(api_information)


def main():
    # get_data()
    print_data()


if __name__ == "__main__":
    main()
