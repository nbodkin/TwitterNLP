# coding: utf-8
import re
# import tweepy
# from tweepy import OAuthHandler
from textblob import TextBlob
import pandas


def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''

    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split())


def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)

    return [analysis.polarity, analysis.subjectivity]


def get_tweets():
    '''
    Main function to fetch tweets and parse them.
    '''

    # empty list to store parsed tweets
    df = pandas.read_csv("florida-tweets.csv", encoding = 'utf-8', na_values={'user_verified':False}, dtype={'time':str, 'user_screen_name':str, 'text':str, 'tweet_type':str, 'hashtags':str, 'retweet_count':float, 'user_description':str, 'user_followers_count':float, 'user_friends_count':float, 'user_statuses_count':float, 'user_verified':str})
    #df = pandas.read_csv("trump-tweets.csv", encoding = 'utf-8', dtype={'time':str, 'user_screen_name':str, 'text':str, 'tweet_type':str, 'hashtags':str, 'retweet_count':float, 'user_description':str, 'user_followers_count':float, 'user_friends_count':float, 'user_statuses_count':float, 'user_verified':str})

    #df.fillna({'user_verified':False})
    original_tweets = df.to_dict('records')

    # list of dictionaries formatted like fetched_tweets = [{"text":"blah blah blah", "rt": 50, "username":"'}, {"text":"blah blah blah", "rt": 50, "username":"'}, ...]

    tweets = []
    #duplicate = 0
    # parsing tweets one by one
    for tweet in original_tweets:
    #    for completed in tweets:
     #       if tweet['text'] == completed['text']:
     #           duplicate = 1
     #           break

    #    if duplicate == 0:
            # saving sentiment of tweet
        tweet['text'] = clean_tweet(tweet['text'])
        tweet['sentiment'], tweet['subjectivity'] = get_tweet_sentiment(tweet['text'])
        tweets.append(tweet)
        #duplicate = 0
    for x in range(20):
        print(original_tweets[x]['text'])
    # return parsed tweets with sentiment and subjectivity
    return tweets


def main():
    # calling function to get tweets
    tweets = get_tweets()

    '''
    print ('sentiment: ', 'subjectivity:  ', 'text:')
    for tweet in tweets:
        print("  {0:.2f}       {1:.2f}        {2}".format(tweet['sentiment'], tweet['subjectivity'], tweet['text'][:100]))
    '''

    print('\nexported to csv ;)')
    df = pandas.DataFrame(tweets)
    df.to_csv('florida-output.csv', encoding='utf8')




    '''
    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) 
  
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
    '''

if __name__ == "__main__":
    # calling main function
    main()
