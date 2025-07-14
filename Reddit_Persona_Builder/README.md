# Reddit User Persona Builder

This project fetches Reddit user posts and comments, then generates a user persona using OpenAI's GPT models. It outputs the persona along with citations from the user's Reddit activity.

---

## Features

- Scrapes Reddit posts and comments for any public user profile
- Uses OpenAI GPT-3.5 Turbo to analyze content and build a detailed user persona
- Saves persona output in a text file with references to original posts/comments

---

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/reddit-persona-builder.git
   cd reddit-persona-builder


2. Create and activate a Python virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt


4. Create a .env file in the project root with your API credentials:

env
Copy
Edit
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=persona-script by u/your_reddit_username
OPENAI_API_KEY=your_openai_api_key


5. Usage
Run the script with a Reddit user profile URL:

bash
Copy
Edit
python main.py https://www.reddit.com/user/kojied/
The user persona will be saved in the sample_output/ folder as <username>_persona.txt.

6. Important Notes
OpenAI API Quota and Billing:
The script uses OpenAI's GPT API, which requires a valid API key. Free tier limits are very restrictive, and you may encounter quota exceeded errors without adding billing information to your OpenAI account.
To fully use the persona generation feature, set up a paid billing plan on OpenAI and use an API key from that account.

7. Mock Mode for Testing:
To avoid API quota issues during development or demo, you can replace the generate_persona function in persona_generator.py with a mock function that returns fixed sample text. This allows you to test the scraping and output generation without making API calls.

