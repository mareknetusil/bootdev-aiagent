import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

import prompts
from functions.call_function import available_functions, call_function


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")


def main() -> None:
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("OPENROUTER_API_KEY is unset")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    prompt = args.user_prompt
    messages = [
        {"role": "system", "content": prompts.system_prompt},
        {"role": "user", "content": prompt},
    ]

    for _ in range(20):
        response = _prompt_llm(client, messages, args.verbose)
        message = response.choices[0].message
        messages.append(message)
        if not message.tool_calls:
            print(message.content)
            break

        for tool_call in message.tool_calls:
            result = call_function(tool_call, args.verbose)
            if result["content"] == "":
                raise Exception(f"Empty response from a tool: {tool_call}!")
            if args.verbose:
                print(f"-> {result['content']}")
            messages.append(result)
    else:
        exit(1)


def _prompt_llm(client: OpenAI, messages: list[dict], verbose: bool = False) -> object:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if response.usage is None:
        raise RuntimeError("invalid response from openrouter")

    return response



if __name__ == "__main__":
    main()
