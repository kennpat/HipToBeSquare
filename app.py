# Foursquare Project Application
# Updated 6/4/2014 - PK



#import foursquare api
import foursquare

#Grab the environment variables
import os

client_id = os.environ.get('FOURSQUARE_CLIENT_ID')
client_secret = os.environ.get('FOURSQUARE_CLIENT_SECRET')

#instantiate userless access

client = foursquare.Foursquare(client_id, client_secret)



#print client.venues.search(params={'query': 'Celtics', 'near': 'Boston, MA', 'limit': 5})

# Latitude and Longitude of Fenway Park: 42.3464 N, 71.0975 W

print client.venues.specials(params={'ll': (42.3464,71.0975), 'limit': 5})

