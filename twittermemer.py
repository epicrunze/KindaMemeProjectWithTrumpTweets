import tweepy


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
