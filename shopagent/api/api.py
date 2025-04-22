from shopagent.models import ShopifyAPI, ShopifyAPIBreakdown
from shopagent.nav import complete_nav_url, get_top_level_operations

from .mutation import get_mutation_info
from .object import get_object_info
from .query import get_query_info


def get_api_information(shopify_nav):
    categories = []

    encountered_objects = 0
    total_objects = sum([sum(len(child.children) for child in nav.children) for nav in shopify_nav.navItems])

    for i, nav in enumerate(shopify_nav.navItems):
        print(f"Working on {i+1} nav item of {len(shopify_nav.navItems)}")
        name = nav.label
        mutations = []
        objects = []
        queries = []

        for j, child in enumerate(nav.children):
            print(f"Working on {j+1} nav item child of {len(nav.children)}")
            if child.label == "Mutations":
                for k, mutation_child in enumerate(child.children):
                    print(f"Working on {k+1} mutation nested child of {len(child.children)} <{encountered_objects}/{total_objects}>")
                    mutations += [get_mutation_info(mutation_child.label, complete_nav_url(mutation_child.href))]
                    encountered_objects += 1
            elif child.label == "Objects":
                for k, object_child in enumerate(child.children):
                    print(f"Working on {k+1} object nested child of {len(child.children)} <{encountered_objects}/{total_objects}>")
                    objects += [get_object_info(object_child.label, complete_nav_url(object_child.href))]
                    encountered_objects += 1
            elif child.label == "Queries":
                for k, query_child in enumerate(child.children):
                    print(f"Working on {k+1} query nested child of {len(child.children)} <{encountered_objects}/{total_objects}>")
                    queries += [get_query_info(query_child.label, complete_nav_url(query_child.href))]
                    encountered_objects += 1

        categories += [ShopifyAPIBreakdown(
            name=name,
            queries=queries,
            mutations=mutations,
            objects=objects
        )]    

    return ShopifyAPI(categories=categories)


def get_data():
    shopify_nav = get_top_level_operations()
    api_information = get_api_information(shopify_nav)

    with open("shopify_api.json", "w") as shopify_api_file:
        json.dump(api_information.model_dump(), shopify_api_file)
