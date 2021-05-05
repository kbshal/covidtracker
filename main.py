from colorama import Fore,Back,Style
import requests
from cores.logo import Logo
from  cores.indentify import Identify
import os,time,sys,time
from time import sleep
_checkInternet=requests.get("https://google.com")
'''if _chekInternet.status_code==200:
    pass
else:
    print(f"{Fore.RED}{Style.BRIGHT}Please connect to internet ")
    exit()
'''
try:
    internet=requests.get("https://google.com")
except ConnectionError:
    print("Network is unreacheable ")
try:
    def file():
        os.system("clear")
        def popup_message():
            message = "In this difficult times please wear mask and stay healty 😷 \n " 
            for letter in message:
                sleep(0.1) # In seconds
                sys.stdout.write(Fore.YELLOW+letter)
                sys.stdout.flush()
            time.sleep(4)    
            print(Fore.GREEN+"Please wait while running daemon")
            time.sleep(3)
        
        popup_message()    
        os.system('clear')
        banner=Logo()
        banner.logo()
        time.sleep(2)
        identify=Identify()
        final_stats_data=[]
        stats_results=identify.covid_stats()
    
        for stats_number in stats_results:
            final_stats_data.append(stats_number)
         
        json_data=identify.raw_data()
        print(f'''
Your IP: {(json_data['ip'])}
Country: {(json_data["country_name"])}
         
''')       
        front_words=["Cases","Today Cases","Deaths","Today Deaths","Recovered","Tests","Active"]
        for i in range(7):
            print(f'{Fore.BLUE}[+] {Fore.RED} {front_words[i]}: {Style.BRIGHT}{Fore.WHITE+str(final_stats_data[i])}\n')
                                                                
    if __name__=="__main__":
        file()
except Exception:
    pass
