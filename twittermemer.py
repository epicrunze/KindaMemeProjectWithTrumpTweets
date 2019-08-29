import tweepy
consumer_key = "0ZuCEN7DYNLpsUTNELQx6TdFf"
consumer_secret = "PYMcv3IRHfk2oftMMXIFmwf2OqKNd2b8yi0nBGlEjtR6mEY8DZ"
access_token = "118683800-y4TsB3UiLtOijqXhR9rVEZq2lZk7yfQulOL8jpKh"
access_token_secret = "X9Q6CeqadRWpr34ekptCCAN7DxxtxN2cOO9Wb5vY4G5tB"

#actual code:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, id="realDonaldTrump", count=1000).items(1000):
    filename = "trumptweets.txt"
    filepath = open(filename,"a+",encoding="utf-16")
    #print(dir(status))
    if hasattr(status, 'retweeted_status'):
        continue
    filepath.write(status.text + "\n")
    filepath.close()