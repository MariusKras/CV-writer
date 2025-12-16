import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_reply(messages: list[dict]) -> str:
    result = client.responses.create(
        model="gpt-5-mini",
        input=messages,
        reasoning={"effort": "minimal"},
        text={"verbosity": "low"}
    )
    return result.output_text.strip()

if __name__ == "__main__":
    system_prompt = load_text("config/system_prompt.txt")
    personal_info = load_text("data/personal_info.txt")

    messages = [
        {"role": "systemddddddd", "content": system_prompt},
        {"role": "user", "content": f"My info:\n{personal_info}"}
    ]

    while True:
        user_input = input("\nUser message:\n").strip()

        messages.append({"role": "user", "content": user_input})

        reply = generate_reply(messages)
        print(f"\nAssistant message:\n{reply}")

        messages.append({"role": "assistant", "content": reply})
