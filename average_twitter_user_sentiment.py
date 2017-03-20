import twitter
import requests

con_secret = 'VKwjWAXnuX2wywUZYVsknC0oY'
con_secret_key = 'UAeNa2QE4Nk8yuDdtvv2ykH6aLF1lat9yx1r824XUgrlx6nPwp'
token = '2428617499-muXCuNlhiquXythOH9s8mXo4PBp8ZjiZCyX3Ly8'
token_key = '78YMqJiibi8ooNTmDfyDDwZ7hjfT05EqSV07QgxLzVD4f'
t=twitter.Twitter(auth=twitter.OAuth(token, token_key, con_secret, con_secret_key))
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