from nav import complete_nav_url

from .models import ShopifyAPI, ShopifyAPIBreakdown
from .mutation import get_mutation_info
from .object import get_object_info
from .query import get_query_info


def get_api_information(shopify_nav):
    categories = []
    for i, nav in enumerate(shopify_nav.navItems):
        print(f"Working on {i+1} nav item of {len(shopify_nav.navItems)}")
        name = nav.label
        mutations = []
        objects = []
        queries = []

        for child in nav.children:
            if child.label == "Mutations":
                for mutation_child in child.children:
                    mutations += [get_mutation_info(mutation_child.label, complete_nav_url(mutation_child.href))]
            elif child.label == "Objects":
                for object_child in child.children:
                    objects += [get_object_info(object_child.label, complete_nav_url(object_child.href))]
            elif child.label == "Queries":
                for query_child in child.children:
                    queries += [get_query_info(query_child.label, complete_nav_url(query_child.href))]

        categories += [ShopifyAPIBreakdown(
            name=name,
            queries=queries,
            mutations=mutations,
            objects=objects
        )]    

    return ShopifyAPI(categories=categories)
