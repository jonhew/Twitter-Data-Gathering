import urllib
import twitter
import json
import csv



api = twitter.Api(
 consumer_key='wplDp3kXN99bNPifkz9Qkg',
 consumer_secret='tp9LNWDriPqFM5EFNr1WE1cYbrwBHyvUDXghQtsnI0',
 access_token_key='699133-4xxJIkcC3qN3N8d7OQ8XI3J7ejsglrCvNlHs3jP9bWv',
 access_token_secret='lewo5SjitNlgDugggHCnDdpxjaGjXkhrWCJcYZ2Zc2dMB'
 )
file = raw_input("Please enter name of file: ")
outfile = open(file + ".csv", "wb" )
writer = csv.writer(outfile)
i = ''
p = 0
#max sets total number of tweets returned
max = 100
while p<max:
    search = api.GetSearch(term='umich', lang='en', count='100', result_type='recent', max_id=i)
    i = search[0].id
    for t in search:
        #Add the .encode to force encoding
        writer.writerow([t.user.screen_name,t.created_at,t.retweet_count,t.id,t.text.encode('utf-8')])
        if(t.id < i): i = t.id
    p = p+1


print "DONE!"
outfile.close()

