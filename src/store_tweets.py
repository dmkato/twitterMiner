import os
from os.path import join, dirname
import twitter as Twitter
from src.pg_interface import PG
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

def get_new_tweets(twitter, pg):
    new_tweets = get_tweets(twitter)
    if not new_tweets:
        return None

    last_db_entry = pg.SELECT("* FROM public.tweets WHERE tweet_id = \
                                (SELECT MAX(tweet_id) FROM public.tweets)")[0]

    for tIdx, tweet in enumerate(new_tweets):
        if tweet[2] == last_db_entry[2]:
            idx = tIdx

    return new_tweets[:idx]

def update_pg(new_tweets, pg):
    if not new_tweets:
        print("No new tweets")
        return
    for tweet in new_tweets:
        pg.INSERT("INTO public.tweets (text, date, tweet_id) \
                   VALUES (%s, %s, %s)", tweet)
    print(len(new_tweets), "new tweets")

def main():
    pg = PG()
    twitter = authenticate()
    new_tweets = get_new_tweets(twitter, pg)
    print(new_tweets)
    update_pg(new_tweets, pg)
    pg.close()

if __name__ == "__main__":
    main()
