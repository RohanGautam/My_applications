'''This program fetches the first 20 tweets of a user and calculated weather
the average sentiment(calculated using HP heaven on demand's sentiment analysis API) is positive or negative'''
import twitter
import requests
#ENTER YOUR TWITTER API DETAILS BELOW:
#if you don't have this stuff, create an app at apps.twitter.com/apps and copy-paste required information
con_secret = ''
con_secret_key = ''
token = ''
token_key = ''
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
#program works better if you follow me on twitter  at @RohanGautam13 
x=t.statuses.user_timeline(screen_name="@RohanGautam13",count=20, include_rts=False)

apiurl='https://api.havenondemand.com/1/api/sync/analyzesentiment/v2'
apikey='?apikey='+'da14f365-731c-4950-81fe-5e924fcbf050'
total=0

for i in x:
    text='&text='+i['text']
    finalcall=apiurl+apikey+text
    ro=requests.get(finalcall)
    js=ro.json()
    #import pprint    (if you want to see the json that the api returns)
    #pprint.pprint(js)
    total+=js['sentiment_analysis'][0]['aggregate']['score']

if total>0.0:print 'Average user sentiment is positive'
elif total<0.0:print 'Average user sentiment is negative'
else:print 'Average user sentiment is neutral'
