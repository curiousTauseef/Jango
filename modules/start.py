import ConfigParser
import jangopath

def add_name():
   print "\nJANGO - CONFIGURATION\n"
   Config = ConfigParser.ConfigParser()
   cfgfile = open(jangopath.CONFIG_PATH, 'w')
   Config.add_section('Person')
   name = raw_input("Enter your name : ")
   Config.set('Person','name',name)
   Config.add_section('Location')
   loc = raw_input("Enter your current location (city, country) : ")
   Config.set('Location','name',loc)
   Config.write(cfgfile)
   cfgfile.close()
   print "\n"
