import tweepy
import os
from core.Fconf import config


try:

    with open('faya.yml', 'r') as yml:
        conf = config.twitter

    auth = tweepy.OAuthHandler(conf['OAuthHandler'][0], conf['OAuthHandler'][1])
    auth.set_access_token(conf['access_token'][0], conf['access_token'][1])
    api = tweepy.API(auth)
    follow = conf['follow']


    class MyStreamListener(tweepy.StreamListener):

        def on_status(self, status):

            # print(status)

            push = ''

            if status.user.screen_name in follow:
                push = follow[status.user.screen_name] +  ' twitter更新了 ' + status.text

            # print(push)

            if push:
                os.system(f"qq send group test群 {push}")

        def on_error(self, status_code):
            if status_code == 420:
                # returning False in on_data disconnects the stream
                os.system(f"qq send group test群 貌似twitter的streaming断了")
                return False



    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())
    myStream.userstream(encoding='utf8')
except KeyError:
    print('配置有误')

#myStream.filter(track=['apple'])

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#   print(tweet.text)


#user = api.get_user('everb1ue')
#api.user_timeline(id="everb1ue")
#print(user)


#for status in tweepy.Cursor(api.user_timeline, id="everb1ue").items(10):
    # process status here
   # print(status.text+ '\n\n')