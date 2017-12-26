import os
from os.path import join, dirname
import twitter as Twitter
import src.pg_interface as pg
from dotenv import load_dotenv

def authenticate():
    dotenv_path = join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)
    twitter = Twitter.Api(consumer_key=os.environ.get('consumer_key'),
                          consumer_secret=os.environ.get('consumer_secret'),
                          access_token_key=os.environ.get('access_token'),
                          access_token_secret=os.environ.get('access_token_secret'))
    return twitter

def load_DB_tweets():
    return pg.SELECT("* FROM public.tweets")

def get_tweets(twitter):
    try:
        latest_tweets = twitter.GetUserTimeline(screen_name="saucy_frank", count=200, include_rts=True)
    except:
        print('Twitter Error')

    return [(t.text, t.created_at, t.id) for t in latest_tweets]

def get_new_tweets(twitter):
    new_tweets = get_tweets(twitter)
    last_db_entry = pg.SELECT("* FROM public.tweets WHERE tweet_id = \
                                (SELECT MAX(tweet_id) FROM public.tweets)")[0]

    for tIdx, tweet in enumerate(new_tweets):
        if tweet[2] == last_db_entry[2]:
            idx = tIdx

    print(idx)
    return new_tweets[:idx]

def update_pg(new_tweets):
    for tweet in new_tweets:
        pg.INSERT("INTO public.tweets (text, date, tweet_id) \
                   VALUES (%s, %s, %s)", tweet)

def load():
    twitter = authenticate()
    new_tweets = get_new_tweets(twitter)
    update_pg(new_tweets)
    tweets = new_tweets + load_DB_tweets()
    pg.CLOSE()
    return tweets
