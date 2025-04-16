# shopify graphql

This project gets the API spec for the Shopify GraphQL API using [LSD](https://lsd.so)

## Contents

* [Setup](#setup)
* [Running](#running)
* [LSD Cache](#lsd-cache)

## Setup

Set the `LSD_USER` and `LSD_API_KEY` environment variables using [your authenticated credentials](https://lsd.so/profile)

## Running

Use [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
$ uv run main.py
```

## LSD Cache

When running this python project, it involves querying the same page more than once for different groups of elements (such as in [here]() or [here]()). To prevent overloading Shopify's servers, pages in distinct states (whether statically off a public URL or following a sequence of deterministic interactions are specifically cached on LSD for scenarios like this.