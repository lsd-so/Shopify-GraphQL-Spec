from requests import get

from constants import SHOPIFY_BASE_URL, SHOPIFY_NAV_API_URL

from .models import ShopifyNavResponse


def complete_nav_url(href):
    return f"{SHOPIFY_BASE_URL}{href}"


def get_top_level_operations():
    res = get(SHOPIFY_NAV_API_URL).json()
    shopify_nav = ShopifyNavResponse(**res)
    return shopify_nav
