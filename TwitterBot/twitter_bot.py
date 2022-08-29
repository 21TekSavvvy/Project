import tweepy
## import Tkinter

# consumer_key = 'MCfxywPXiRrsVzkM1CWcfwPJf'
# consumer_secret = '9TxKnKxMQ58L8n7OnKEFvG5oL51EMdFcUcG0tnkGsPiQb8tx5N'
# access_token = '2521908055-4pviPjIZO60Mnkpo0iyHpFaGQh1FjwsNzKsbGnD'
# access_token_secret = 'vCTyPQeuwUQmDXdfAtgD14RoWEoBHGqRA07YbwlK7GAug'
#client_id = T18xS3FzdUFfRFgwSk9oa0lUS3k6MTpjaQ
# client_secret = o9VpEd0PMvfr46s5EecW6CyDEXwUy8VE7p-w5KPWMLGZMFZAl_

auth = tweepy.OAuth2UserHandler(client_id = '18xS3FzdUFfRFgwSk9oa0lUS3k6MTpjaQ', redirect_uri = 'https://twitter.com/jj2166', scope =["tweet.read", "tweet.write", "tweet.moderate.write", "users.read", "follows.read","follow.write", "offline.access", "space.read", "mute.read","mute.write", "like.read", "like.write"], client_secret = 'o9VpEd0PMvfr46s5EecW6CyDEXwUy8VE7p-w5KPWMLGZMFZAl_')

#auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token,access_token_secret)

print(auth.get_authorization_url())
access_token = '2521908055-4pviPjIZO60Mnkpo0iyHpFaGQh1FjwsNzKsbGnD'
client = tweepy.Client(access_token)
api = tweepy.API(auth)
#
for follower in api.get_followers():
    print(follower)



# for followers in tweepy.Cursor(api.get_followers()).items():
#     followers.follow()
#
# print("Followed everyone that is following " )
