import tweepy
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from twitterauth import *
import json



auth  = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


class MyListener(StreamListener):
	
	def on_data(self, data):
		try:
			with open('coutinho.json', 'a') as f:
				f.write(data)
				tweet = json.loads(data)

				print('%s \n \n' % tweet['text'])
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))

	def on_error(self, status):
		print(status)
		return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#coutinho'])
