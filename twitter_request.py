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
search = api.GetSearch(term='#hail', lang='en', result_type='recent', count=100, max_id='')

for t in search:
    #Add the .encode to force encoding
    writer.writerow([t.user.screen_name,t.created_at,t.text.encode('utf-8')])
print "DONE!"
outfile.close()

