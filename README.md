# shopagent

![GIF of generating a Shopify agent](media/landing.gif)

Generate a Shopify agent on the fly thanks to [Llama](https://ollama.com/) and [LSD](https://lsd.so).

## Contents

* [Getting started](#getting-started)
  * [One liner](#one-liner)
  * [From python package](#from-python-package)
	* [Generate agent](#generate-agent)
	* [Print data](#print-data)
	* [Get data](#get-data)
  * [From source](#from-source)
* [Why](#why)
* [Why only the admin API?](#why-only-the-admin-api)
* [Gimme the data](#gimme-the-data)
  * [Pretty printing the data](#pretty-printing-the-data)
  * [Getting the data yourself](#getting-the-data-yourself)
* [Help me vibe code this](#help-me-vibe-code-this)
* [Mining Shopify GraphQL yourself](#mining-shopify-graphql-yourself)
* [Mining](#mining)
* [LSD Cache](#lsd-cache)

## Getting started

![GIF of generating a Shopify agent](media/codegen.gif)

### One liner

This assumes you have [uv installed](https://docs.astral.sh/uv/getting-started/installation/) as well as [Ollama](https://ollama.com/download).

Replace the `{request}` in the below snippet for a one-liner to generate a Shopify agent

```bash
$ echo 'from shopagent import generate_agent;generate_agent("{request}")' | uv run --with shopagent -
```

For example:

```bash
$ echo 'from shopagent import generate_agent;generate_agent("Cancel an order")' | uv run --with shopagent -
```

### From python package

1. Install the [python package](https://pypi.org/project/shopagent/)

```
$ uv add shopagent
```

2. Import and run the method you're interested in

#### Generate agent

```
from shopagent import generate_agent

request = "Cancel an order"
generate_agent(request)
```

#### Generate agent from terminal input

```
from shopagent import gen_agent

gen_agent()
```

#### Print data

```
from shopagent import print_data

print_data()
```

#### Get data

```
from shopagent import get_data

get_data()
```

### From source

1. Clone the repo

```
$ git clone https://github.com/lsd-so/shopagent.git
```

2. Run `uv run main.py`

```
$ uv run main.py
```

3. Answer prompt

```
What would you like your agent to do? <your reply here>
```

4. Now you have an `agent.rb` file

## Why

![Shopify LSD diagram](media/Shopify_LSD.jpg)

[Gumroad](https://gumroad.com) recently went [open source](https://github.com/antiwork/gumroad) to [support AI writing Ruby code](https://x.com/shl/status/1908146557708362188). In order to assist the initiative towards a more AI-infused world, we gathered the Shopify GraphQL spec plus code examples to make it easy to generate Shopify agents.

## Why only the admin API?

The official Shopify MCP server explicitly prompts to not interact with [the storefront or functions APIs](https://github.com/Shopify/dev-mcp/blob/main/src/tools/index.ts#L92). If there is a specific dataset you're interested in that wouldn't bother Shopify, then feel free to [file an issue](https://github.com/lsd-so/shopagent/issues/new/choose).

## Gimme the data

If you're interested in the Shopify GraphQL being programmatically accessible, the two files you'd be most interested in are:

* [`api/models.py`](https://github.com/lsd-so/shopagent/blob/main/shopagent/api/models.py) -> Where the [Pydantic](https://docs.pydantic.dev/latest/) models for the derived GraphQL operations are defined
* [`shopify_api.json`](https://github.com/lsd-so/shopagent/blob/main/shopify_api.json) -> Where the Shopify GraphQL spec can be viewed as a JSON with code examples included.
  * This is structured as a [`ShopifyAPI` object](https://github.com/lsd-so/shopagent/blob/main/shopagent/api/models.py#L96)
  * For an example of working from the already obtained data, see [`get_data` in `main.py`](https://github.com/lsd-so/shopagent/blob/main/main.py#L11)

### Pretty printing the data

![](media/code_examples.png)

1.  Clone this repository.

```bash
$ git clone https://github.com/lsd-so/shopagent.git
```

2. Update the [`main.py` file](https://github.com/lsd-so/shopagent/blob/main/main.py) file to `print_data()` instead of `gen_agent()`

```diff
def main():
    # get_data()
-     gen_agent()
+    # gen_agent()
-    # print_data()
+    print_data()
```

3. Using [uv](https://docs.astral.sh/uv/getting-started/installation/) ([Why?](https://docs.astral.sh/uv/#highlights)), run the [`main.py` file](https://github.com/lsd-so/shopagent/blob/main/main.py) at the root of the project.

```bash
$ uv run main.py
```

### Getting the data yourself

If you'd like to get the data yourself or update to match a new version of the Shopify API, then [continue reading to learn how](#mining-shopify-graphql-yourself).

## Help me vibe code this

![Screenshot of Cursor generating code using the Shopify GraphQL API](media/cursor.png)

LLMs are already familiar with GraphQL so this gives them the ability to understand Shopify's GraphQL specifically.

1. Download the [JSON file](https://github.com/lsd-so/shopagent/blob/main/data/shopify_api.json) and [Python models](https://github.com/lsd-so/shopagent/blob/main/shopagent/models/api.py)
2. Place both the JSON file and Python file in your repo
   1. Make sure you are using the `models/api.py` file!
3. Go to Cursor, click "New chat", click "Add context", click "Files & folders", and add both files to your context
4. Vibe code with Cursor now understanding how to use the Shopify GraphQL API
   1. If something doesn't work, try checking the option for longer context

## Mining Shopify GraphQL yourself

1. Set the `LSD_USER` and `LSD_API_KEY` environment variables using [your authenticated credentials](https://lsd.so/profile).

```
$ export LSD_USER='your@email.domain'
$ export LSD_API_KEY='<api key from profile>'
```

2.  Clone this repository.

```bash
$ git clone https://github.com/lsd-so/shopagent.git
```

3. And update the [`main.py` file](https://github.com/lsd-so/shopagent/blob/main/main.py) file to `get_data()` instead of `gen_agent()`

```diff
def main():
-    # get_data()
+     get_data()
-     gen_agent()
+    # gen_agent()
    # print_data()
```

4. Use [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
$ uv run main.py
```

And there ya go.

## LSD Cache

When running this python project, it involves querying the same page more than once for different groups of elements (such as in [here](https://github.com/lsd-so/Shopify-GraphQL-Spec/blob/main/api/fields_and_connections.py#L28) or [here](https://github.com/lsd-so/shopagent/blob/main/shopagent/api/fields_and_connections.py#L33)). To prevent overloading Shopify's servers, pages in distinct states (whether statically off a public URL or following a sequence of deterministic interactions) are specifically cached for up to 15 minutes on LSD for scenarios like this.

Think of [LSD](https://lsd.so) as a language with caching that provides a more developer friendly [Wayback machine](https://web.archive.org/). Follow us on [Twitter](https://x.com/getlsd) to stay tuned!
