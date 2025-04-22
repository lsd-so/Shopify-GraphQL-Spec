import json
import os.path

from ollama import chat
from whoosh import index
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

from shopagent.constants import OLLAMA_MODEL
from shopagent.models import ShopifyAPI


def establish_agent_gen_prompt():
    return {
        'role': 'user',
        'content': """You are a mid-level software engineer who writes "Shopify agents" in Ruby using the Shopify GraphQL API.

Based on the provided request, use the [search_shopify_graphql] tool to obtain information about the relevant GraphQL functionalities to use. When you're ready to write the agent, use the [define_agent] tool to do so."""
    }


def format_user_request_into_prompt(user_request):
    # If does not already end with punctuation
    if user_request[-1] not in [".", "?", "!"]:
        user_request += "."

    return {
        'role': 'user',
        'content': f"Request: {user_request}",
    }


search_shopify_graphql_tool = {
    'type': 'function',
    'function': {
        'name': 'search_shopify_graphql',
        'description': 'Given a query, search through the Shopify GraphQL spec for one of "MUTATION", "QUERY", or "OBJECT". May be helpful for getting information if something is not already known beforehand',
        'parameters': {
            'type': 'object',
            'required': ['query', 'search_type'],
            'properties': {
                'query': {
                    'type': 'string',
                    'description': 'The query to search the Shopify GraphQL spec with',
                },
                'search_type': {
                    'type': 'string',
                    'enum': ['MUTATION', 'QUERY', 'OBJECT'],
                },
            }
        }
    },
}


def search_shopify_graphql(query, search_type):
    with open("shopify_api.json", "r") as shopify_api_file:
        data = json.load(shopify_api_file)
        api_information = ShopifyAPI(**data)

        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")

        schema = Schema(
            name=TEXT(stored=True),
            description=TEXT(analyzer=StemmingAnalyzer()),
            fields_and_connections=TEXT(stored=True),
            arguments=TEXT(stored=True),
            returns=TEXT(stored=True),
            code_examples=TEXT(stored=True),
        )

        ix = index.create_in("indexdir", schema)
        writer = ix.writer()
        for category in api_information.categories:
            if search_type == "MUTATION":
                for mutation in category.mutations:
                    writer.add_document(
                        name=mutation.name,
                        description=mutation.description,
                        arguments=f"[{', '.join(['<' + arg.name + ': ' + arg.type + ' (required)' if arg.required else '' + '>' for arg in mutation.arguments])}]",
                        returns=f"[{', '.join(['<' + ret.name + ': ' + ret.type for ret in mutation.returns])}]",
                        code_examples='\n\n'.join(example.description + ':\n' + example.code for example in mutation.examples),
                    )
            elif search_type == "QUERY":
                for query in category.queries:
                    writer.add_document(
                        name=query.name,
                        description=query.description,
                        arguments=f"[{', '.join(['<' + arg.name + ': ' + arg.type + ' (required)' if arg.required else '' + '>' for arg in query.arguments])}]",
                        returns=f"[{', '.join(['<' + ret.name + ': ' + ret.type for ret in query.returns])}]",
                        code_examples='\n\n'.join(example.description + ':\n' + example.code for example in query.examples),
                    )
            else:
                for obj in category.objects:
                    writer.add_document(
                        name=obj.name,
                        description=obj.description,
                        fields_and_connections=f"[{', '.join(['<' + field.name + ': ' + field.type + '>' for field in obj.fields_and_connections])}]",
                        code_examples='\n\n'.join(example.description + ':\n' + example.code for example in obj.examples),
                    )

        qp = QueryParser("description", schema=ix.schema)
        q = qp.parse(query)

        with ix.searcher() as searcher:
            results = searcher.search(q, limit=10)
            return str([r for r in list(results)])


define_agent_tool = {
    'type': 'function',
    'function': {
        'name': 'define_agent',
        'description': 'Given a string containing a ruby program that defines a "Shopify agent", write to the file "agent.rb"',
        'parameters': {
            'type': 'object',
            'required': ['ruby_code'],
            'properties': {
                'query': {
                    'type': 'string',
                    'description': 'The query to search the Shopify GraphQL spec with',
                },
                'search_type': {
                    'type': 'string',
                    'enum': ['MUTATION', 'QUERY', 'OBJECT'],
                },
            }
        }
    },
}


def define_agent(ruby_code=''):
    if len(ruby_code) == 0:
        return "Cannot define an empty agent"

    with open("agent.rb", "w") as agent_file:
        agent_file.write(ruby_code)
        return "Defined! No more need to call tools"


def generate_agent(user_request):
    last_tool_calls = [[]]
    messages = [establish_agent_gen_prompt(), format_user_request_into_prompt(user_request)]
    available_functions = {
        'search_shopify_graphql': search_shopify_graphql,
        'define_agent': define_agent,
    }
    available_functions_schemas = {
        'search_shopify_graphql': search_shopify_graphql_tool,
        'define_agent': define_agent_tool,
    }

    defined_agent = False
    while not defined_agent:
        if len(messages) > 24:
            messages = [establish_agent_gen_prompt(), format_user_request_into_prompt(user_request)]

        response = chat(
            OLLAMA_MODEL,
            messages=messages,
            tools=[search_shopify_graphql_tool, define_agent_tool],
        )

        if response.message.tool_calls:
            print("Calling a tool...")
            # There may be multiple tool calls in the response
            for tool in response.message.tool_calls:
                # Ensure the function is available, and then call it
                if function_to_call := available_functions.get(tool.function.name):
                    try:
                        output = function_to_call(**tool.function.arguments)
                        if tool.function.name == "define_agent" and output != "Cannot define an empty agent":
                            defined_agent = True
                    except Exception as e:
                        output = f"You called the tool incorrectly, here's the error:\n{str(e)}\n\nThe expected parameters are [{', '.join(k for k in available_functions_schemas[tool.function.name]['function']['parameters']['properties'])}]"
                    last_tool_calls += [[]]

                # Only needed to chat with the model using the tool call results
                if response.message.tool_calls:
                    # Add the function response to messages for the model to use
                    messages.append(response.message)
                    messages.append({'role': 'tool', 'content': str(output), 'name': tool.function.name})
        elif "```ruby" in response.message.content and not defined_agent:
            ruby_code = response.message.content[response.message.content.index("```ruby")+7:]
            ruby_code = ruby_code[:ruby_code.index("```")]
            if len(ruby_code) > 0:
                define_agent(ruby_code)
                defined_agent = True
        elif "```" in response.message.content and not defined_agent:
            messages.append(response.message)
            messages.append({"role": "user", "content": "Use the [define_agent] tool instead of providing code"})
            last_tool_calls += [[]]


def gen_agent():
    user_request = input("What would you like your agent to do? ")
    generate_agent(user_request)
