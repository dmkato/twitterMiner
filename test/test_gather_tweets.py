import src.gather_tweets as gather_tweets
import pytest

def test_authenticate():
    test_twitter = gather_tweets.authenticate()
    info = test_twitter.VerifyCredentials()
    assert info.screen_name == "dmkato"

def test_load_DB_tweets():
    rows = gather_tweets.load_DB_tweets()

def test_load():
    tweets = gather_tweets.load()
    print(tweets)
