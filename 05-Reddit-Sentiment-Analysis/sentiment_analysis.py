import praw
import openai
import os
from dotenv import load_dotenv

# Todo: refactor my self created sentiment_analysis.py to use OOP (currently all implemented in one .py file)
# Todo: add credit card to openai to avoid "openai.error.RateLimitError" error

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
reddit_client_id = os.getenv("REDDIT_CLIENT_ID")
reddit_client_secret = os.getenv("REDDIT_CLIENT_SECRET")

reddit = praw.Reddit(client_id=reddit_client_id, # the App ID retrieved from the reddit application
                     client_secret=reddit_client_secret, # the secret retrieved from the reddit application
                     user_agent="sentiment analysis test by u/Sdet-Devops"  # add your reddit name
                    )


# Of course, we want to access hot subreddits like r/wallstreetbets or r/stocks
subreddit_stocks = reddit.subreddit("stocks")

# Let's say we want to access the first 5 hot posts and three most upvoted comments:
for post in subreddit_stocks.hot(limit=5):
    print(post.title)
    submission = reddit.submission(post.id)
    c = 0
    # print top 2 comments per title comment (5 titles in all)
    for comment in submission.comments:
        comment = comment.body
        if not comment == "[deleted]": # ignore deleted comment
            print(comment)
            c+=1
        if c == 2:
            break


def get_titles_and_comments(subreddit="stocks", sub_instance="hot", limit=10, num_comments=2, skip_first=2):
    subreddit = reddit.subreddit(subreddit)
    titles_and_comments = {}
    for c, post in enumerate(getattr(subreddit, sub_instance)(limit=limit)):
        # c is counter
        if c < skip_first:
            continue

        c += (1 - skip_first)

        titles_and_comments[c] = ""

        submission = reddit.submission(post.id)
        title = post.title

        titles_and_comments[c] += "Title: " + title + "\n\n"
        titles_and_comments[c] += "Comments: \n\n"

        comment_counter = 0
        for comment in submission.comments:
            comment = comment.body
            if not comment == "[deleted]":
                titles_and_comments[c] += comment + "\n"
                comment_counter += 1
            if comment_counter == num_comments:
                break

    return titles_and_comments


titles_and_comments = get_titles_and_comments(subreddit="stocks", limit=12)
print(titles_and_comments[2])


def create_prompt(title_and_comments):
    task = ("Return the stock ticker or company in the following heading and comments and classify the sentiment. If "
            "no ticker or company is mentioned write 'No company mentioned':\n\n")
    return task + title_and_comments


prompt = create_prompt(titles_and_comments[1])
print(prompt)

for key, title_and_comments in titles_and_comments.items():
    prompt = create_prompt(title_and_comments)

    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=256,
                                        temperature=0,
                                        top_p=1.0,
                                        frequency_penalty=0.0,
                                        presence_penalty=0.0)
    print(title_and_comments)
    print("Sentiment: " + response["choices"][0]["text"])
    print("-" * 30)
