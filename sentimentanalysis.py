# coding: utf-8
import re 
#import tweepy 
#from tweepy import OAuthHandler 
from textblob import TextBlob 
import pandas
import csv


class TwitterClient(object): 

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", tweet).split()) 
  
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        '''
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

        '''
        return [analysis.polarity, analysis.subjectivity]

  
    def get_tweets(self): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = pandas.read_csv("a.csv", header = None, delimiter="\t", quoting=csv.QUOTE_NONE, encoding='utf-8')
        print(tweets.loc[: , "text"])

  





        fetched_tweets = ["I can’t believe you had the balls to tweet this. #LiarInChief #ImpeachTrumpNow", "Secure our nations boarder!!!", "We all are waiting for you to go to jail", "The first contracts to support the construction of President Donald Trump's border wall are expected to be awarded this week using Pentagon funds", "Check this out - TRUTH!", "“What’s completely unacceptable is for Congesswoman Omar to target Jews, in this case Stephen Miller.” Jeff Ballabon, B2 Strategic, CEO.  @Varneyco", "On National Former Prisoner of War Recognition Day, we honor the Americans captured and imprisoned by foreign powers while carrying out their duties to defend this great Nation...", "The Mainstream Media has never been more inaccurate or corrupt than it is today. It only seems to get worse. So much Fake News!", "The Democrats will never be satisfied, no matter what they get, how much they get, or how many pages they get. It will never end, but that’s the way life goes!"]


        # parsing tweets one by one 
        for tweet in fetched_tweets: 
            # empty dictionary to store required params of a tweet 
            parsed_tweet = {} 
  
            # saving text of tweet 
            parsed_tweet['text'] = tweet #tweet.text 
            # saving sentiment of tweet 
            parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet) 

  
            # appending parsed tweet to tweets list 
            if tweet.retweet_count > 0: 
                # if tweet has retweets, ensure that it is appended only once 
                if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
            else: 
                tweets.append(parsed_tweet) 
  				

            # return parsed tweets 
            return tweets 
  
  
def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets() 

    print ('polarity:  ', 'subjectivity:  ', 'text:')
    for tweet in tweets:
    	print("  {0:.2f}       {1:.2f}        {2}".format(tweet['sentiment'][0], tweet['sentiment'][1], tweet['text'][:100]))

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