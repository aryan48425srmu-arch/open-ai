import os

from openai import OpenAI


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {"role": "user", "content": "Write a short welcome message for a new OpenAI starter project."}
        ],
    )

    print(response.output_text)


if __name__ == "__main__":
    main()
