import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_bullets(system_prompt: str, personal_info: str, job_description: str) -> str:
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"My info:\n{personal_info}\n\nJob description:\n{job_description}"}
        ],
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    system_prompt = load_text("config/system_prompt.txt")
    personal_info = load_text("data/personal_info.txt")

    job_description = input("Paste the job description:\n")

    print("\nGenerating bullet points...\n")
    result = generate_bullets(system_prompt, personal_info, job_description)
    print(result)
