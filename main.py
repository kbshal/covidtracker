from colorama import Fore,Back,Style
from cores.logo import Logo
from  cores.indentify import Identify
import os,time,sys,time


def popup_message():
    print()
os.system('clear')
banner=Logo()
banner.logo()
identify=Identify()
json_data=identify.raw_data()
print(f'''
Your IP: {(json_data['ip'])}
Country: {(json_data['country_name'])}

''')

time.sleep(1.5)
