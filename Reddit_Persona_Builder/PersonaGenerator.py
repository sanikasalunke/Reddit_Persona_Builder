# persona_generator.py

import openai
import os
from dotenv import load_dotenv

# Load your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  # You’ll set this key in .env

def truncate_text(text, max_chars):
    """Helper to truncate text for token safety."""
    return text[:max_chars] + "..." if len(text) > max_chars else text

def build_prompt(posts, comments):
    """
    Constructs a prompt to send to the LLM.
    Includes both posts and comments with instructions.
    """
    sample_posts = "\n\n".join(
        f"Title: {p['title']}\nText: {truncate_text(p['selftext'], 300)}\nSubreddit: {p['subreddit']}" for p in posts[:5]
    )
    sample_comments = "\n\n".join(
        f"Comment: {truncate_text(c['body'], 300)}\nSubreddit: {c['subreddit']}" for c in comments[:5]
    )

    prompt = f"""
You are an AI that analyzes a Reddit user's activity and builds a user persona.

Based on the Reddit posts and comments below, extract the following traits:
- Likely interests
- Writing style
- Personality traits
- Possible location (if any hint)
- Subreddits they frequent
- Any profession or domain hints
- Beliefs, values, or tone

For **each trait**, cite the supporting **post or comment** briefly.

---

Posts:
{sample_posts}

---

Comments:
{sample_comments}

Return the result in a human-readable format.
    """
    return prompt

'''Uncomment the below function to use OpenAI's API for generating the persona.
 Before running replace your OpenAi API Key in the .env file'''

# def generate_persona(posts, comments):
#     """
#     Calls OpenAI's API with the built prompt and returns the persona.
#     """
#     try:
#         prompt = build_prompt(posts, comments)
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7,
#             max_tokens=800
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         print(f"OpenAI API error: {e}")
#         return "Failed to generate persona."



def generate_persona(posts, comments):
    # Mock response for testing without OpenAI calls
    return """
User Persona:
- Interests: Technology, gaming, and programming.
- Writing style: Informal, concise.
- Personality traits: Curious, humorous.
- Location hints: Possibly from the US (based on some post topics).
- Profession clues: Likely a software developer or student.
- Citations: Based on recent posts and comments.
"""
