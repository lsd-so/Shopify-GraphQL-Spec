from pydantic import BaseModel
from typing import List


# The type def for a nav item link accessible on the Shopify docs
class NavItemLink(BaseModel):
    key: str # Key for DOM
    label: str # Human readable but code label (ie cartTransforms)
    href: str # The path to be appended to "https://shopify.dev/"
    monospace: bool # Appears to be true for most but keeping nonetheless


# The type def for a nav item child accessible on the Shopify docs
class NavItemChild(BaseModel):
    key: str # Key for DOM
    label: str # Human readable label (Queries, Mutations, Objects)
    children: List[NavItemLink] # A list of links referencing different APIs for this category

# Represents a single item that gets presented in the nav bar consisting of all APIs
class NavItem(BaseModel):
    key: str # Key for DOM
    label: str # Human readable label (top level)
    children: List[NavItemChild] # A list of types of APIs (queries, mutations, objects)

# The type def for a part of the overall Shopify docs nav
class ShopifyNavResponse(BaseModel):
    navItems: List[NavItem] # A collection of all nav items
