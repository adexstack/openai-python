import os
import openai
from dotenv import load_dotenv

# Getting the api key in .env for security purpose
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# CONNECT TO API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

"""https://pieriantraining.com/chatgpt-api-python-guide/?utm_campaign=2023-06-01&utm_term=9685726&utm_content
=educational&utm_source=email-sendgrid&utm_medium=903744
Let’s look at an example script project that will automatically add back in the reply to the list, then let 
the user continue the conversation, essentially our own Python version of the official ChatGPT website:"""

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Enter question or Type 'quit' to end chat : ")
messages = []
user_input = ''
while user_input != 'quit':
    # Get user input
    user_input = input('')
    # Add to messages list
    messages.append({'role': 'user', 'content': user_input})
    # Send to ChatGPT API
    completion = openai.ChatCompletion.create(
        max_tokens=3500,
        model="gpt-3.5-turbo",
        messages=messages)
    # Grab Assistant Messages and append to messages list
    reply = completion.choices[0].message
    messages.append(reply)
    # Print out reply for user to respond to:
    print(reply['content'])
    # Then we keep this loop going until user says quit
