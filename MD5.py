import os
import sys
import time
import hashlib
from colorama import Fore,init,Style

banners=f"""{Fore.GREEN+Style.BRIGHT}
   Cyber Hunter Kurdish {Fore.WHITE}{Style.BRIGHT}            
 https://t.me/cyberhunter_official   
 {Fore.YELLOW}{Style.BRIGHT}                             
██▄  ▄██ ▄▄▄▄  ███▀▀▀   ██  ██  ▄▄▄   ▄▄▄▄ ▄▄ ▄▄ 
██ ▀▀ ██ ██▀██ ▀▀███▄   ██████ ██▀██ ███▄▄ ██▄██ 
██    ██ ████▀ ▄▄▄██▀   ██  ██ ██▀██ ▄▄██▀ ██ ██  {Fore.RED} {Style.BRIGHT}   
█████▄ ▄▄▄▄  ▄▄ ▄▄ ▄▄▄▄▄▄ ▄▄▄▄▄                  
██▄▄██ ██▄█▄ ██ ██   ██   ██▄▄                   
██▄▄█▀ ██ ██ ▀███▀   ██   ██▄▄▄                {Fore.WHITE}{Style.BRIGHT}"""

ErrMSG=(f"""
{banners}

    -- Smart Tool, For BruteForce Attack MD5 Hashes Decrypt....!
{Fore.RED}{Style.BRIGHT}ERROR-HUMAN{Fore.WHITE}: python MD5.py missing a options!

[+] -- Options-[ {Fore.CYAN}--MD5 {Fore.WHITE}<Your Hash MD5> {Fore.CYAN}--WordList {Fore.WHITE}<Your WordList>  ]

[+] -- Run: python MD5.py --MD5 <Your Hash> --WordList <Your WordList>
""")

W = Fore.WHITE+Style.BRIGHT
G = Fore.GREEN+Style.BRIGHT
R = Fore.RED+Style.BRIGHT
Y = Fore.YELLOW+Style.BRIGHT

Argv1 = "--MD5"
Argv2 = "--WordList"
MSG = f"{W}[{G}Received{W}] +Num {G} Hashed {W} | {G} Word"
MSG1 =  f"{W}[{G}Received{W}] +Num {R} Hashed {W} | {R} Word"
MSG2 = f"{W}[{Y}Not Received{W}] +Num {Y} Hashed {W} | {Y} Word"

def Start_Attack_BruteForce(hashlib_md5,wordlist_brute):
   try:
     wordlist= open(wordlist_brute,'r').read().splitlines()
   except:
      print(Fore.RED+Style.BRIGHT+"ERROR-HUMAN"+Fore.WHITE+Style.BRIGHT+": WordList NotFound...!")
      exit()
      return
   print(banners)
   print(f"""
   {Fore.WHITE}{Style.BRIGHT}
   Received All WordList:{Fore.GREEN}{Style.BRIGHT} {str(len(wordlist))}""")
   time.sleep(3)
   print(Fore.GREEN+Style.BRIGHT+"   [+] - Starting Attack.....")
   time.sleep(3)
   print(Fore.WHITE+Style.BRIGHT+"-"*40)
   num=0
   for words in wordlist:
     num+=1
     num3=str(num)
     try: 
        first_encode = words.encode("UTF-8")
        two_hash = hashlib.md5(first_encode)
        hash_md5 = two_hash.hexdigest()
        if hashlib_md5 == hash_md5:
          mess = MSG.replace("Num",num3).replace("Hashed",hash_md5).replace("Word",words)
          print(mess)
          break
        else:
           mess = MSG1.replace("Num",num3).replace("Hashed",hash_md5).replace("Word",words)
           print(mess)
           continue
     except Exception as e:
        mess = MSG2.replace("Num",num3).replace("Hashed","Error Hashing it...!").replace("Word",words)
        print(mess)
        pass
   print()
   print(Fore.WHITE+Style.BRIGHT+"-"*40)
   print(Fore.WHITE+Style.BRIGHT+"Join My Channel --> https://t.me/cyberhunter_official")
   exit()
   return
          
def main():
   CyberHunterKurdish = (sys.argv) # CyberHunterKudish
   if Argv1 not in CyberHunterKurdish or Argv2 not in CyberHunterKurdish:
      print(ErrMSG)
      exit()
   else:
     try:
       hashlib_md5 = sys.argv[2]
       wordlist_brute = sys.argv[4]
     except:
       print(ErrMSG)
       exit()
   Start_Attack_BruteForce(hashlib_md5,wordlist_brute)

if __name__ == '__main__':
   main()




