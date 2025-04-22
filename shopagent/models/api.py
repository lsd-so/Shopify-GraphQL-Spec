from pydantic import BaseModel
from typing import List, Optional

# The type def for a code example belonging to an graphql operation
class CodeExample(BaseModel):
    description: str
    code: str


# The type def for an argument belonging to a graphql mutation
class MutationArgument(BaseModel):
    name: str
    type: str
    required: Optional[bool]
    description: str


# The type def for a return value provided by a graphql mutation
class MutationReturn(BaseModel):
    name: str
    type: str
    description: str


# The type def for a graphql mutation offered by the Shopify API
class Mutation(BaseModel):
    name: str
    description: str
    arguments: List[MutationArgument]
    returns: List[MutationReturn]
    examples: List[CodeExample]


# The type def for a field or connection available to an object
class ObjectFieldOrConnection(BaseModel):
    name: str
    type: str
    description: str
    not_nullable: Optional[bool]


# The type def for a query involving a graphql object
class ObjectQuery(BaseModel):
    name: str
    type: str
    description: str


# The type def for an interface involving a graphql object
class ObjectInterface(BaseModel):
    name: str


# The type def for a graphql object offered by the Shopify API
class Object(BaseModel):
    name: str
    description: str
    fields_and_connections: List[ObjectFieldOrConnection]
    examples: List[CodeExample]


# The type def for an argument that can be provided to a particular graphql query
class QueryArgument(BaseModel):
    name: str
    type: str
    required: Optional[bool]
    description: str


# The type def for a possible return value for a graphql query
class QueryReturn(BaseModel):
    name: str
    type: str
    description: str


# The type def for a graphql query offered by the Shopify API
class Query(BaseModel):
    name: str
    description: str
    arguments: List[QueryArgument]
    returns: List[QueryReturn]
    examples: List[CodeExample]


# The type def for a breakdown of an API offered by Shopify
class ShopifyAPIBreakdown(BaseModel):
    name: str
    queries: List[Query]
    mutations: List[Mutation]
    objects: List[Object]


# The type def for the overall Shopify API
class ShopifyAPI(BaseModel):
    categories: List[ShopifyAPIBreakdown]
