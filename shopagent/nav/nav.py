import json
import os.path
import sys

from requests import get
from rich import print

from shopagent.models import ShopifyAPI, ShopifyNavResponse
from shopagent.constants import SHOPIFY_BASE_URL, SHOPIFY_NAV_API_URL


def complete_nav_url(href):
    return f"{SHOPIFY_BASE_URL}{href}"


def get_top_level_operations():
    res = get(SHOPIFY_NAV_API_URL).json()
    shopify_nav = ShopifyNavResponse(**res)
    return shopify_nav


def print_data():
    if not os.path.exists("shopify_api.json"):
        sys.exit("Missing [shopify_api.json] file in your working directory. Please download from https://github.com/lsd-so/shopagent/blob/main/shopify_api.json")
        return

    with open("shopify_api.json", "r") as shopify_api_file:
        data = json.load(shopify_api_file)
        api_information = ShopifyAPI(**data)

        print(api_information)
