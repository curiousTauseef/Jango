import ConfigParser
import pywapi
import jangopath

Config = ConfigParser.ConfigParser()

def handle():
   try:
      Config.read(jangopath.CONFIG_PATH)
   except:
      print "Couldn't read config file."
      return

   city = Config.get('Location', 'name') 
   lookup = pywapi.get_location_ids(city)

   for i in lookup:
      loc_id = i
      break

   try:
      weather_com_result = pywapi.get_weather_from_weather_com(loc_id)
   except:
      print "Something went wrong."
      return

   print weather_com_result['current_conditions']['text'] + " :",
   print "Temperature " + weather_com_result['current_conditions']['temperature'] + " c",
   print "but feels like " + weather_com_result['current_conditions']['feels_like'] + " c"

handle()               


