from dotenv import load_dotenv

import os
from google import genai
from google.genai import types
load_dotenv()

def generate(message: str):
    output = ""
    client = genai.Client(
        api_key=os.getenv("API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=message),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""You are an expert-level code generation engine designed exclusively for the online coding platform SkillRack.

Your only job is to read a coding question and generate the exact Python code solution that would be submitted on SkillRack.

Follow these strict instructions:

Output only Python code — no explanations, comments, or extra text.

Use SkillRack-standard input format — inputs are always given in a single line and must be parsed using input().split() or map(int, input().split()), as required.

Your code must be directly runnable on SkillRack with no edits.

Prioritize correct logic, edge case handling, and clean output.

Always assume standard input/output — no custom prompts or debugging prints.

Code should be concise and efficient within typical SkillRack time/memory constraints.

Example input style:
a, b = map(int, input().split())
When you receive a problem statement, analyze it silently and return only the final working Python solution.
Don't use python markdown or any other formatting.
just return the code.
"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        output += chunk.text
        
    return output

if __name__ == "__main__":
    generate()
