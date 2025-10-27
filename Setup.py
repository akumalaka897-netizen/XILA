import sys
import os
import random

G = '\033[0;33m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m'# BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI

def clear():
    os.system("cls" if os.name == "nt" else "clear")

if sys.platform.startswith("win"):
    "WINDOWS"
    print(f"\n{M}[{P}+{M}] {M}[{P}+{M}] {B}Installing the python modules required for the DarkStar Tool:")
    print(f"{M}[{P}+{M}] {B}Upgrade pip")
    os.system("pip3 install --upgrade pip")
    os.system("pip3 install --upgrade pip setuptools wheel")
    clear()
    print(f"{M}[{P}+{M}] {B}Installing names")
    os.system("pip3 install names")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing dnspython")
    os.system("pip3 install dnspython")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing unidecode")
    os.system("pip3 install unidecode")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing aiohttp")
    os.system("pip3 install aiohttp")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing rich")
    os.system("pip3 install rich")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing colorama")
    os.system("pip3 install colorama")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing requests")
    os.system("pip3 install requests")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing holehe")
    os.system("pip3 install holehe")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing psutil")
    os.system("pip3 install psutil")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing bs4")
    os.system("pip3 install bs4")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing itertools")
    os.system("pip3 install itertools")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing phonenumbers")
    os.system("pip3 install phonenumbers")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing pystyle")
    os.system("pip3 install pystyle")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing pytube")
    os.system("pip3 install pytube")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing stdiomask")
    os.system("pip3 install stdiomask")
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing google")
    os.system('pip3 install google')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing wget")
    os.system('pip3 install wget')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing requests")
    os.system('pip3 install requests')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing sockets")
    os.system('pip3 install sockets')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing ipaddres")
    os.system('pip3 install ipaddress')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing pyexiftool")
    os.system('pip3 install pyexiftool')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing beautifulsoup4")
    os.system('pip3 install beautifulsoup4')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing faker")
    os.system('pip3 install faker')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing urllib3")
    os.system('pip3 install urllib3')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing regex")
    os.system('pip3 install regex')
    clear()
    
    print(f"{M}[{P}+{M}] {B}Installing argparse")
    os.system('pip3 install argparse')
    clear()
    print(f"{M}[{P}+{M}] {B}Installing importlib")
    os.system('pip3 install importlib')    
    clear()
    print(f"{M}[{P}+{M}] {B}Installing scapy")
    os.system('pip3 install scapy')
    clear() 
    print(f"{M}[{P}+{M}] {B}Installing whois")
    os.system('pip3 install whois')
    clear()
    print(f"{M}[{P}+{M}] {B}Installing openssl")
    os.system('pip3 install pyopenssl')
    clear()
    print(f"{M}[{P}+{M}] {B}Installing fuzzywuzzy")
    os.system('pip3 install fuzzywuzzy')
    clear()
    print(f"{M}[{P}+{M}] {B}Installing tld")
    os.system('pip3 install tld')
    clear()
    print(f"{M}[{P}+{M}] {B}Installing googlesearch")
    os.system('pip3 install googlesearch')
    clear()
    
    print(f"{H}Finish.")
    os.system("python3 DarkStar.py")

elif sys.platform.startswith("linux"):
    "LINUX"
    print(f"\n{M}[{P}01{M}] {B}Termux\n{M}[{P}02{M}] {B}Kali Linux")
    p = input(f"\n{M}[{P}+{M}] {B}Pilih :{P} ")
    if p in["01","1"]:
        print(f"\n{K}Installing the python modules required for the DarkStar Tool:{B}")
        
        os.system('pkg update && apt upgrade')
        
        print(f"{M}[{P}+{M}] {B}Installing golang")
        os.system('pkg install golang')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing nodejs")
        os.system('pkg install nodejs-lts')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing perl")
        os.system('pkg install perl')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing git")
        os.system('pkg install git')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing neofetch")
        os.system('pkg install neofetch')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing wget")
        os.system('pkg install wget')
        clear()
      
        print(f"{M}[{P}+{M}] {B}Installing names")
        os.system("pip3 install names")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing aiohttp")
        os.system("pip3 install aiohttp")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing rich")
        os.system("pip3 install rich")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing colorama")
        os.system("pip3 install colorama")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing requests")
        os.system("pip3 install requests")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing holehe")
        os.system("pip3 install holehe")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing psutil")
        os.system("pip3 install psutil")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing bs4")
        os.system("pip3 install bs4")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing phonenumbers")
        os.system("pip3 install phonenumbers")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pystyle")
        os.system("pip3 install pystyle")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pytube")
        os.system("pip3 install pytube")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing stdiomask")
        os.system("pip3 install stdiomask")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing colorama")
        os.system('pip3 install colorama')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing wget")
        os.system('pip3 install wget')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing requests")
        os.system('pip3 install requests')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing sockets")
        os.system('pip3 install sockets')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing ipaddres")
        os.system('pip3 install ipaddress')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pyexiftool")
        os.system('pip3 install pyexiftool')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing beautifulsoup4")
        os.system('pip3 install beautifulsoup4')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing faker")
        os.system('pip3 install faker')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing urllib3")
        os.system('pip3 install urllib3')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing regex")
        os.system('pip3 install regex')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing argparse")
        os.system('pip3 install argparse')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing importlib")
        os.system('pip3 install importlib')    
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing scapy")
        os.system('pip3 install scapy')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing whois")
        os.system('pip3 install whois')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing openssl")
        os.system('pip3 install pyopenssl')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing fuzzywuzzy")
        os.system('pip3 install fuzzywuzzy')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing tld")
        os.system('pip3 install tld')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing googlesearch")
        os.system('pip3 install googlesearch')
        clear()
        
        print(f"{H}Finish.")
        os.system("rm -rf Setup.py")
        os.system("python3 DarkStar.py")
 
    
    elif p in["02","2"]:
        print(f"\n{M}[{P}+{M}] {B}Installing the python modules required for the DarkStar Tool:{N}")
        os.system('apt update && apt upgrade')
        
        clear()
        print(f"{M}[{P}+{M}] {B}Installing names")
        os.system("apt install python3-names")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing aiohttp")
        os.system("apt install python3-aiohttp")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing rich")
        os.system("apt install python3-rich")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing colorama")
        os.system("apt install python3-colorama")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing requests")
        os.system("apt install python3-requests")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing holehe")
        os.system("apt install python3-holehe")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing psutil")
        os.system("apt install python3-psutil")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing bs4")
        os.system("apt install python3-bs4")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing webbroswer")
        os.system("apt install python3-webbrowser")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing itertools")
        os.system("apt install itertools")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing phonenumbers")
        os.system("apt install python3-phonenumbers")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pystyle")
        os.system("apt install python3-pystyle")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pytube")
        os.system("apt install python3-pytube")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing httpx")
        os.system("apt install python3-httpx")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing stdiomask")
        os.system("apt install python3-stdiomask")
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing google")
        os.system('apt install python3-google')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing colorama")
        os.system('apt install python3-colorama')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing wget")
        os.system('apt install python3-wget')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing requests")
        os.system('apt install python3-requests')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing sockets")
        os.system('apt install python3-sockets')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pythonping")
        os.system('apt install python3-pythonping')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing ipaddres")
        os.system('apt install python3-ipaddress')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing pyexiftool")
        os.system('apt install python3-pyexiftool')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing beautifulsoup4")
        os.system('apt install python3-beautifulsoup4')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing faker")
        os.system('apt install python3-faker')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing urllib3")
        os.system('apt install python3-urllib3')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing regex")
        os.system('apt install python3-regex')
        clear()
        
        print(f"{M}[{P}+{M}] {B}Installing argparse")
        os.system('apt install python3-argparse')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing importlib")
        os.system('apt install python3-importlib')    
        clear()
        print(f"{M}[{P}+{M}] {B}Installing scapy")
        os.system('apt install python3-scapy')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing whois")
        os.system('apt install python3-whois')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing tld")
        os.system('apt install python3-tld')    
        clear()
        print(f"{M}[{P}+{M}] {B}Installing openssl")
        os.system('apt install python3-pyopenssl')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing fuzzywuzzy")
        os.system('apt install python3-fuzzywuzzy')
        clear()
        print(f"{M}[{P}+{M}] {B}Installing googlesearch")
        os.system('apt install python3-googlesearch')
        clear()
        
        print(f"{H}Finish.")
        os.system("python3 DarkStar.py")
    else:
        print(f"{M}Input Yang Anda Masukkan Salah!!")
        exit()
