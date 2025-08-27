from source.utils import squarer

from dotenv import load_dotenv
from openai import OpenAI

import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def connect_to_openai() -> OpenAI:
    client = OpenAI(api_key=api_key)
    return client

def main():
    print("Hello, World!")
    print(squarer(4))
    client = connect_to_openai()

if __name__ == '__main__':
    main()