from colorama import Fore,Back,Style
from cores.logo import Logo
from  cores.indentify import Identify
import os,time,sys,time
from time import sleep
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
    list_len=len(final_stats_data)
    print(f'''
Your IP: {(json_data['ip'])}
Country: {(json_data["country_name"])}

''')
    front_sentences=["Cases","Today Cases","Deaths","Today Deaths","Recovered","Tests","Active"]
    for i in range(7):
        print(f'{Fore.BLUE}[+] {Fore.RED} {front_sentences[i]}: {Fore.WHITE+str(final_stats_data[i])}\n')
  
if __name__=="__main__":
    file()

