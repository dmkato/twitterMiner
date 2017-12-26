import os
from os.path import join, dirname
import twitter as Twitter
import pg_interface as pg
from dotenv import load_dotenv

def authenticate():
    dotenv_path = join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)
    twitter = Twitter.Api(consumer_key=os.environ.get('consumer_key'),
                          consumer_secret=os.environ.get('consumer_secret'),
                          access_token_key=os.environ.get('access_token'),
                          access_token_secret=os.environ.get('access_token_secret'))
    return twitter

def get_tweets(twitter):
    latest_tweets = []
    try:
        latest_tweets = twitter.GetUserTimeline(screen_name="saucy_frank", count=200, include_rts=True)
    except Exception as e:
        print('Error' + e.message)

    if latest_tweets:
        cleaned_tweets = [(t.text, t.created_at, t.id) for t in latest_tweets]
        return cleaned_tweets
    else:
        return None

def get_new_tweets(twitter):
    new_tweets = get_tweets(twitter)
    if not new_tweets:
        return None

    last_db_entry = pg.SELECT("* FROM public.tweets WHERE tweet_id = \
                                (SELECT MAX(tweet_id) FROM public.tweets)")[0]

    for tIdx, tweet in enumerate(new_tweets):
        if tweet[2] == last_db_entry[2]:
            idx = tIdx

    return new_tweets[:idx]

def update_pg(new_tweets):
    if not new_tweets:
        print("No new tweets")
        return
    for tweet in new_tweets:
        print(len(new_tweets), "new tweets")
        pg.INSERT("INTO public.tweets (text, date, tweet_id) \
                   VALUES (%s, %s, %s)", tweet)

def main():
    twitter = authenticate()
    new_tweets = get_new_tweets(twitter)
    update_pg(new_tweets)
    pg.CLOSE()

if __name__ == "__main__":
    main()
