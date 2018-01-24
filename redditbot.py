import praw
import config
import time

def bot_login():
    r = praw.Reddit(username =  config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Nicebot 1.0")
    return r
def run_bot(r):

    for comment in r.subreddit('all').comments(limit=500):
        if (comment.body in (["word"])  and comment.id not in comments_replied
        and not comment.author == r.user.me()):
            print("string found")
            comment.reply("Reply")

            comments_replied.append(comment.id)
    print("sleeping")
    print (comments_replied)
    time.sleep(10)
        

    
comments_replied = []
r = bot_login()

while True:


    run_bot(r)
