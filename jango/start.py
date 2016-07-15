import ConfigParser
import jangopath
import getpass
import os

def add_name():
   print "\nJANGO - CONFIGURATION\n"
   Config = ConfigParser.ConfigParser()
   Config2 = ConfigParser.ConfigParser()
   cfgfile = open(jangopath.CONFIG_PATH, 'w')
   cfgfile2 = open(jangopath.CONTACTS_PATH, 'a')

   Config.add_section('Person')
   Config2.add_section('Person')
   name = raw_input("Enter your name : ")
   uname = raw_input("Enter your email : ")
   pswd = getpass.getpass("Enter your password : ")
   phone = raw_input("Enter your phone number(freesms8) : ")
   phonepswd = getpass.getpass("Enter your password : ")
   Config.set('Person','name',name)
   Config.set('Person','uname',uname)
   Config.set('Person','pswd',pswd)
   Config.set('Person','phone',phone)
   Config.set('Person','ppswd',phonepswd)
   Config.add_section('Location')
   loc = raw_input("Enter your current location (city, country) : ")
   Config.set('Location','name',loc)
   Config.add_section('Directory')
   music = os.getenv("HOME") + "/Music"
   Config.set('Directory','music',music)

   Config.write(cfgfile)
   Config2.write(cfgfile2)
   cfgfile.close()
   cfgfile2.close()

