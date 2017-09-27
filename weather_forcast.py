#!/usr/local/bin/python
from optparse import OptionParser

from weather import CityWeather



if __name__ == '__main__':    
    parser = OptionParser()

    parser.add_option('-k', "--key",
                          dest="api_key",
                          help='Wunderground API KEY',
                          default='740ce852e68a576f')

    parser.add_option('-c', "--city",
                          dest="city",
                          help='City Name',
                          default='Philadelphia')

    parser.add_option('-s', "--state",
                          dest="state",
                          help='State Code',
                          default='PA')

    (options, args) = parser.parse_args()
    cw = CityWeather(options.api_key, options.city, options.state)
    cw.get_city_weather()
    print cw
    

