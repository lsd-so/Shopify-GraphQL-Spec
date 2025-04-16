# shopify graphql

![Shopify LSD diagram](media/Shopify_LSD.jpg)

This project mines Shopify API docs for the spec to their GraphQL API using [LSD](https://lsd.so).

## Contents

* [Give me the data](#give-me-the-data)
* [Setup](#setup)
* [Running](#running)
* [LSD Cache](#lsd-cache)

## Give me the data

If you are only interested in the spec to the GraphQL API, you can use the types defined in [`api/models.py`](https://github.com/lsd-so/Shopify-GraphQL-Spec/blob/main/api/models.py) to work with the [`shopify_api.json` file]() which is structured as a [`ShopifyAPI` object](https://github.com/lsd-so/Shopify-GraphQL-Spec/blob/main/api/models.py#L96).

If you'd like to run this project then continue reading to learn how.

## Setup

Set the `LSD_USER` and `LSD_API_KEY` environment variables using [your authenticated credentials](https://lsd.so/profile).

```
$ export LSD_USER='your@email.domain'
$ export LSD_API_KEY='<api key from profile>'
```

## Running

Use [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
$ uv run main.py
```

And there ya go.

## LSD Cache

When running this python project, it involves querying the same page more than once for different groups of elements (such as in [here](https://github.com/lsd-so/Shopify-GraphQL-Spec/blob/main/api/fields_and_connections.py#L28) or [here](https://github.com/lsd-so/Shopify-GraphQL-Spec/blob/main/api/fields_and_connections.py#L33)). To prevent overloading Shopify's servers, pages in distinct states (whether statically off a public URL or following a sequence of deterministic interactions) are specifically cached for up to 15 minutes on LSD for scenarios like this.

Think of this as a language with cache that provides a more developer friendly Wayback machine.