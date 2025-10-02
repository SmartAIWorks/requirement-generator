import os, json

from openai import OpenAI
from app.config import settings

from app.models.story import Story


client = OpenAI(api_key=settings.OPENAI_API_KEY)

PROMPT = """
You are a user-story generator. Given the requirements below, return ONLY a JSON array of stories.
Each story must contain: title, description, acceptance_criteria (array), story_points (int|null), labels (array), epic (string|null).

Response Output Constraint:
 - Return valid and parsable JSON only and do not include other text not part of JSON object.
 - Output JSON array ONLY.
 - Do not include any explanations, comments, or markdown fences lile ```json or ```
Requirements:
{requirements}

"""

def _call_llm(prompt: str) -> str:
    res = client.chat.completions.create(model="gpt-4o-mini", 
        messages=[{"role": "user", "content": prompt}])

    print('res >>>', res.choices[0].message.content)
    return res.choices[0].message.content


def generate_stories(requirement_txt: str) -> list[Story]:
    prompt = PROMPT.format(requirements = requirement_txt)

    print(prompt)

    raw_response = _call_llm(prompt)

    try:
        parsed = json.loads(raw_response)
        stories = []
        for story in parsed:
            s = Story.parse_obj(story)
            stories.append(s)
        
        return stories
    except Exception as e:
        raise Exception(f"Error parsing stories: {e}")





