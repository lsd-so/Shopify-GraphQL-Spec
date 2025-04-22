# This is the base URL from which we are exploring docs
SHOPIFY_BASE_URL = "https://shopify.dev"

# This is the API URL that gets called internally to figure out what links to render in the navbar
SHOPIFY_NAV_API_URL = "https://shopify.dev/docs/api/admin-graphql/latest/nav"

# Available languages to view code examples in
EXAMPLE_LANGUAGES = ["GQL", "cURL", "Remix", "Node.js", "Ruby"]

# The language to be getting code examples in
EXAMPLE_LANGUAGE = EXAMPLE_LANGUAGES[4] # "Ruby"

# The Llama model to request from ollama
OLLAMA_MODEL = 'llama3.2'
