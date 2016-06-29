from twitter import Twitter, OAuth, TwitterStream

oauth = OAuth(access_token_key, access_token_secret, api_key, api_secret)
twitter = Twitter(auth=oauth)


twitter_stream= TwitterStream(auth=oauth)
iterator = twitter_stream.statuses.filter(track= "Brexit", language= "en")
count= 0
for tweet in iterator:
    print tweet['text']
    count+=1
    if count== 50:
        break
