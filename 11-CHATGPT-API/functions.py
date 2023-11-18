import openai
import os
import tiktoken
from dotenv import load_dotenv
import openai

"""
# History ChatBot Tutor
**WARNING: Remember that models are prone to hallucination! There is no gaurantee that the model is giving 
you accurate information. Alright, let's get on with building this tutor bot**
"""

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class CreateBot:

    def __init__(self, system_prompt):
        """
        system_prompt: [str] Describes context for Chat Assistant
        """
        self.system = system_prompt
        self.messages = [{"role": "system", "content": system_prompt}]

    def chat(self):
        """
        Tracks dialogue history and takes in user input
        """
        print('To end conversation, type END')
        question = ''
        while question != 'END':
            # Get User Question
            question = input("")

            # Add to messages/dialogue history
            self.messages.append({'role': 'user', 'content': question})

            # Send to ChatGPT and get response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages)

            # Get content of assistant reply
            content = response['choices'][0]['message']['content']
            print('\n')
            print(content)
            print('\n')
            # Add assistant reply for dialogue history
            self.messages.append({'role': 'assistant', 'content': content})


"""
Token Length Check¶
One last note, we currently didn't add a check for very long conversations, you could do a token count check, 
and if it went over you could start removing older messages, for example:
"""


def num_tokens_from_string(string, encoding_name):
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


if __name__ == "__main__":
    history_tutor = CreateBot(system_prompt="You are an expert in US History")
    history_tutor.chat()

    full_content = ''
    for item in history_tutor.messages:
        full_content += item['content']

    num_tokens_from_string(full_content, encoding_name='cl100k_base')

    # Don't pop index 0, because that is the system role!
    history_tutor.messages.pop(1)
