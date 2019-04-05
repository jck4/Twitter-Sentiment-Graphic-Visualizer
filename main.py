from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as Sentiment
import json
import time

#consumer key, consumer secret, access token, access secret.
ckey="a"
csecret="a"
atoken="a"
asecret="a"

class listener(StreamListener):

    def on_data(self, data):

        data = json.loads(data)

        tweet = data['text']
        analyzer = Sentiment()
        vs = analyzer.polarity_scores(tweet)
        compound = str(vs['compound'])
        out = open("twitter-Sentiment.txt","a")
        out.write(compound + '\n')
        time.sleep(2)
        out.close()

        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])
