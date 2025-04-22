from setuptools import setup

setup(
    name="shopagent",
    version="1.0.1",
    packages=['shopagent', 'shopagent.api', 'shopagent.code_gen', 'shopagent.constants', 'shopagent.lsd', 'shopagent.models', 'shopagent.nav'],
    data_files=[('data', ['data/shopify_api.json'])]
)
