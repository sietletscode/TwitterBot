import tweepy
import time

print('this is my twitter bot')
#Sign up as developer in twitter and create application , place your keys in key1,key2 Auth1,Auth2
auth = tweepy.OAuthHandler('key1','key2')
auth.set_access_token('Auth1','Auth2')
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#navneet' in mention.full_text.lower():
            print('found tweets')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + ' '
                    +'thanks for your tweets', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
