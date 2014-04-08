import urllib
import twitter
import json
import csv


#add your twitter api keys below
api = twitter.Api(
 consumer_key='***',
 consumer_secret='***',
 access_token_key='***',
 access_token_secret='***'
 )
 
file = raw_input("Please enter name of file: ")
outfile = open(file + ".csv", "wb" )
writer = csv.writer(outfile)
i = ''
p = 0
#max sets total number of tweets returned
max = 100
print "in progress...",
writer.writerow(["Screen Name","Created At","# Retweets","# Favorites","Tweet"])

while p<max:
    #change parameters of get search to determine results
    search = api.GetSearch(term='#gameofthrones', lang='en', count='100', result_type='popular', max_id=i)
    i = search[0].id

    for t in search:
        #remove duplicate retweets
        if "RT" not in t.text:
            writer.writerow([t.user.screen_name,t.created_at,t.retweet_count,t.favorite_count,t.text.encode('utf-8')])
        if(t.id < i): i = t.id
    print p,
    p = p+1
print "DONE!"
outfile.close()

