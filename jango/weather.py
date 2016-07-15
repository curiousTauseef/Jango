import ConfigParser
import pyowm
import jangopath

Config = ConfigParser.ConfigParser()

f = open(jangopath.HOME_DIR + '/ans.txt','w')

def handle():
   try:
      Config.read(jangopath.CONFIG_PATH)
   except:
      print "Couldn't read config file."
      return

   city = Config.get('Location', 'name') 

   owm = pyowm.OWM('f47660233e14a180642092b3914a2cb1')

   observation = owm.weather_at_place(city)
   w = observation.get_weather()
   f.write("Current Temperature is : " + str(int(w.get_temperature('celsius')['temp'])) + str(" Degree Celsius\n\n") )
   f.write(" , Humidity " + str(w.get_humidity()) + "%")
   print "Current Temperature is : " + str(w.get_temperature('celsius')['temp']) + str(" Degree Celsius")
   print "Humidity " + str(w.get_humidity()) + "%"
   f.close()

handle()               


