import tweepy
from textblob import TextBlob

consumer_key="r0ubp1aWrhdK7lChTjMvKuCSA"
consumer_secret="4a2Unpghyar3Kb700VJfPNQIooBgoj4hkaijbM9DuKWkbAIMLP"

access_token="1035307842-HKak8OQd0UXsp7rEyPJSTFW5ymJ7FxceXBF3i83"
access_token_secret="rArTWqYX64GKGjYQIjphiVMbNeOSnKYntDOmpLUNN25QU"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search(q='cokie', count=10000,since = "2016-10-13", until="2018-04-13")

with open ("f.txt","w") as fout:
	for tweet in public_tweets:
   		fout.write(tweet.text.encode('utf-8')+"\n")
   		analysis=TextBlob(tweet.text)
   		fout.write(str(analysis.sentiment).encode('utf-8')+"\n")