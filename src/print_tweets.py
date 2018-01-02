import pg_interface as pg

def get_tweets():
    return pg.SELECT('* FROM public.tweets ORDER BY tweet_id ASC')

def print_tweets(tweets):
    idx = 0
    for tweet in tweets:
        print(str(idx) + ' | ', str(tweet['date']) + " | " + tweet['text'])
        idx += 1

def main():
    tweets = get_tweets()
    print_tweets(tweets)

if __name__ == '__main__':
    main()
