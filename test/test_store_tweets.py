import pytest
import twitter
from unittest.mock import patch
import src.store_tweets as st

def mock_api(consumer_key, consumer_secret, access_token_key, access_token_secret):
    # assert len(consumer_key) == 25
    # assert len(consumer_secret) == 50
    # assert len(access_token_key) == 50
    # assert len(access_token_secret) == 45
    return True

@patch('twitter.Api', mock_api)
def test_authenticate():
    assert st.authenticate() == True
