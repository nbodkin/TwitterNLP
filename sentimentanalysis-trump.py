import pandas as pandas
from textblob import TextBlob
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textblob

def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    return [analysis.polarity, analysis.subjectivity]


def get_tweets():
    '''
    Main function to fetch tweets and parse them.
    '''

    # empty list to store parsed tweets
    df = pandas.read_csv("exportTweets.csv", na_values={'user_verified': False},
                         dtype={'source': str, 'text': str, 'created_at': str, 'retweet_count': str, 'favorite_count': str,'is_retweet': str})
    original_tweets = df.to_dict('records')

    # list of dictionaries formatted like fetched_tweets = [{"text":"blah blah blah", "rt": 50, "username":"'}, {"text":"blah blah blah", "rt": 50, "username":"'}, ...]
    print("hello")
    tweets = []
    # parsing tweets one by one
    for tweet in original_tweets:
        print(tweet)
        # saving sentiment of tweet
        tweet['sentiment'], tweet['subjectivity'] = get_tweet_sentiment(tweet['text'].decode('utf-8'))
        tweets.append(tweet)

    # return parsed tweets with sentiment and subjectivity
    return tweets


def main():
    tweets = get_tweets()

    print('\nexported to csv ;)')
    df = pandas.DataFrame(tweets)
    df.to_csv('output.csv')


if __name__ == "__main__":
    # calling main function
    main()
