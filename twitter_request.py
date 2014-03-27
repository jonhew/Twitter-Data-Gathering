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

search = api.GetSearch(term='#hail', lang='en', result_type='recent', count=100, max_id='')
outfile = open("outfile", "wb" )
writer = csv.writer(outfile)

for t in search:
    print t.user.screen_name + ' (' + t.created_at + ')'
    #Add the .encode to force encoding
    print t.text.encode('utf-8')
    print ''
    writer.writerow([t.user.screen_name,t.created_at,t.text.encode('utf-8')])
outfile.close()

