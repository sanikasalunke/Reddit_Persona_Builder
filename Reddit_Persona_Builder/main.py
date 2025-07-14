# main.py

import sys
import os
from RedditScraper import extract_username_from_url, fetch_user_activity
from PersonaGenerator import generate_persona

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url>")
        return

    profile_url = sys.argv[1]
    username = extract_username_from_url(profile_url)
    print(f"\nFetching Reddit data for: {username}")

    posts, comments = fetch_user_activity(username)

    if not posts and not comments:
        print("No posts or comments found. The user may not exist or have public content.")
        return

    print(f"Generating persona using LLM for {username}...")
    persona_text = generate_persona(posts, comments)

    output_dir = "sample_output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{username}_persona.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona_text)

    print(f"\nPersona saved to: {output_path}")

if __name__ == "__main__":
    main()
