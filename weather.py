import urllib2
import json

WUNDERGROUND_URL = "http://api.wunderground.com/api/{api_key}/geolookup/conditions/q/{state}/{city}.json"

class CityWeather(object):

    def __init__(self, api_key, city, state):
        self.api_key = api_key
        self.city = city
        self.state = state
        self.weather = {}        

    def get_city_weather(self):
        url = WUNDERGROUND_URL.format(api_key=self.api_key, state=self.state, city=self.city)
        print 'Requesting url:::',url

        try:        
            f = urllib2.urlopen(url) 
            response = f.read()
            d = json.loads(response)
            self.weather = d.get('current_observation')            
        except urllib2.URLError, err:
            print 'ERROR in url:::',err
        except Exception, err:
            print 'ERROR:::',err
        finally:
            f.close()

    def __str__(self):
        if self.weather:
            return "Location: {0}\
            \nTemparature: {1}\
            \nFeeld Like: {2}\
            \nWeather: {3}\
            \nHumidity: {4}\
            \nWind: {5}".format(self.weather['display_location']['full'], \
                        self.weather['temperature_string'], self.weather['feelslike_string'], 
                        self.weather['weather'], self.weather['relative_humidity'], self.weather['wind_string'])
        else:
            return "Could not find Current Observation for given city, please check speeling for command line options."
            
            
            
