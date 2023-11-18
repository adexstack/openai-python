
import os
import openai
from dotenv import load_dotenv
#os.environ["OPENAI_API_KEY"] = ""
#print(os.environ.get("OPENAI_API_KEY"))

# optimizing code by having the api key in .env for security purpose
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# CONNECT TO API KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Hello!"},
    # We'll add the reply back in!
    {
      "content": "Hello there! How can I assist you today?",
      "role": "assistant"
    },
    # Now we add our response:
    {"role": "user", "content": "I am good, briefly, what is the definition of AI?"},
  ]
)

print(completion.choices[0].message)

print("-----------------------------------------------------------------------------")
# Get just the output string
print(completion.choices[0].message['content'])

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
      # Edit the system
      {"role":'system','content':'You are very tired and only want to answer questions about bedtime.'},
    {"role": "user", "content": "What is AI?"},
  ],
)

print(completion.choices[0].message)


