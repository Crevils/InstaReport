#!/usr/bin/env python3
import requests #line:2
from colorama import *#line:3
import os #line:4
from os import _exit #line:5
from colorama import Fore ,Back ,Style #line:6
import time #line:7
import random #line:8
from libs .animation import colorText #line:9
init (convert =True )#line:10
os .system ('cls'if os .name =='nt'else 'clear')#line:11
rhttps =requests .get ('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=7000&country=ALL&anonymity=elite&ssl=no')#line:12
rhttp =requests .get ('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=ALL&anonymity=elite&ssl=no')#line:13
rs4 =requests .get ('https://www.proxy-list.download/api/v1/get?type=socks4')#line:14
rs5 =requests .get ('https://www.proxy-list.download/api/v1/get?type=socks5')#line:15
https =[]#line:16
https =rhttps .text #line:17
https =https .split ()#line:18
http =[]#line:19
http =rhttp .text #line:20
http =http .split ()#line:21
socks4 =[]#line:22
socks4 =rs4 .text #line:23
socks4 =socks4 .split ()#line:24
socks5 =[]#line:25
socks5 =rs5 .text #line:26
socks5 =socks5 .split ()#line:27
number =random .randint (25 ,50 )#line:28
def find_proxies ():#line:29
    print (colorText ('''
[[red]] _______  [[blue]] _______  [[magenta]]  ______  [[cyan]] __    __ [[yellow]] __      __ [[red]] ________ [[reset]]
[[red]]|       \ [[blue]]|       \ [[magenta]] /      \ [[cyan]]|  \  |  \[[yellow]]|  \    /  \[[red]]|        \[[reset]] 
[[red]]| $$$$$$$\[[blue]]| $$$$$$$\[[magenta]]|  $$$$$$\[[cyan]]| $$  | $$[[yellow]] \$$\  /  $$[[red]] \$$$$$$$$[[reset]]
[[red]]| $$__/ $$[[blue]]| $$__| $$[[magenta]]| $$  | $$[[cyan]] \$$\/  $$[[yellow]]  \$$\/  $$ [[red]]    /  $$ [[reset]]
[[red]]| $$    $$[[blue]]| $$    $$[[magenta]]| $$  | $$[[cyan]]  >$$  $$ [[yellow]]   \$$  $$  [[red]]   /  $$  [[reset]]
[[red]]| $$$$$$$ [[blue]]| $$$$$$$\[[magenta]]| $$  | $$[[cyan]] /  $$$$\ [[yellow]]    \$$$$   [[red]]  /  $$   [[reset]]
[[red]]| $$      [[blue]]| $$  | $$[[magenta]]| $$__/ $$[[cyan]]|  $$ \$$\[[yellow]]    | $$    [[red]] /  $$___ [[reset]]
[[red]]| $$      [[blue]]| $$  | $$[[magenta]] \$$    $$[[cyan]]| $$  | $$[[yellow]]    | $$    [[red]]|  $$    \[[reset]] 
[[red]] \$$      [[blue]] \$$   \$$[[magenta]]  \$$$$$$ [[cyan]] \$$   \$$[[yellow]]     \$$    [[red]] \$$$$$$$$[[reset]]
[[black-bright-background]][[red]]Note - Use At Your Own Risk. The Developer Of This Software Will Not 
        Be Hold Liable For Any Bad Activities You Do![[reset]]

                    [[black]]Codded By Crevil[[reset]]

                [[red]]Github :- [[blue]]@Crevils[[reset]]
                [[red]]Youtube :- [[blue]]@Crevil[[reset]]
                [[red]]Telegram :- [[blue]]@HackerExploits[[reset]] 


[[red]][ 1 ][[reset]] [[green]]HTTPS[[reset]]
[[red]][ 2 ][[reset]] [[green]]HTTP[[reset]]
[[red]][ 3 ][[reset]] [[green]]SOCKS4[[reset]]
[[red]][ 4 ][[reset]] [[green]]SOCKS5[[reset]] 
'''))#line:54
    print (Fore .RESET +' ')#line:55
    O000OOOOOO0O0O0OO =input (Fore .LIGHTWHITE_EX +"Choose Type of Proxy : ")#line:56
    if (O000OOOOOO0O0O0OO =="1"):#line:57
        for OO00OOO000OO0O000 in range (number ):#line:58
            OOOO0OO00O0000OO0 =https [OO00OOO000OO0O000 ]#line:59
            print (Fore .LIGHTWHITE_EX +"[ "+Fore .LIGHTGREEN_EX +"Success -> HTTPS"+Fore .LIGHTWHITE_EX +" ] "+Fore .LIGHTGREEN_EX +OOOO0OO00O0000OO0 )#line:60
            O0OO0000000O0OO00 =open ("https.txt","a")#line:61
            O0OO0000000O0OO00 .write ('\n'+https [OO00OOO000OO0O000 ])#line:62
            time .sleep (0.1 )#line:63
        return OOOO0OO00O0000OO0 #line:64
    elif (O000OOOOOO0O0O0OO =="2"):#line:65
        for O000OOOOOO0O0O0OO in range (number ):#line:66
            OOOO0OO00O0000OO0 =http [O000OOOOOO0O0O0OO ]#line:67
            print (Fore .LIGHTWHITE_EX +"[ "+Fore .LIGHTGREEN_EX +"Success -> HTTP"+Fore .LIGHTWHITE_EX +" ] "+Fore .LIGHTGREEN_EX +OOOO0OO00O0000OO0 )#line:68
            OOOOOOO00000O0OO0 =open ("http.txt","a")#line:69
            OOOOOOO00000O0OO0 .write ('\n'+http [O000OOOOOO0O0O0OO ])#line:70
            time .sleep (0.1 )#line:71
        return OOOO0OO00O0000OO0 #line:72
    elif (O000OOOOOO0O0O0OO =="3"):#line:73
        for OO0000O000OO00O00 in range (number ):#line:74
            OOOO0OO00O0000OO0 =socks4 [OO0000O000OO00O00 ]#line:75
            print (Fore .LIGHTWHITE_EX +"[ "+Fore .LIGHTGREEN_EX +"Success -> SOCKS4"+Fore .LIGHTWHITE_EX +" ] "+Fore .LIGHTGREEN_EX +OOOO0OO00O0000OO0 )#line:76
            O0O000OO00O000000 =open ("socks4.txt","a")#line:77
            O0O000OO00O000000 .write ('\n'+socks4 [OO0000O000OO00O00 ])#line:78
            time .sleep (0.1 )#line:79
        return OOOO0OO00O0000OO0 #line:80
    elif (O000OOOOOO0O0O0OO =="4"):#line:81
        for OOOO00OO0OO0OO00O in range (number ):#line:82
            OOOO0OO00O0000OO0 =socks5 [OOOO00OO0OO0OO00O ]#line:83
            print (Fore .LIGHTWHITE_EX +"[ "+Fore .LIGHTGREEN_EX +"Success -> SOCKS5"+Fore .LIGHTWHITE_EX +" ] "+Fore .LIGHTGREEN_EX +OOOO0OO00O0000OO0 )#line:84
            O0OOO00O00O0OOO00 =open ("socks5.txt","a")#line:85
            O0OOO00O00O0OOO00 .write ('\n'+socks5 [OOOO00OO0OO0OO00O ])#line:86
            time .sleep (0.1 )#line:87
        return OOOO0OO00O0000OO0 #line:88
    else :#line:89
        print (f"No Option Found Named -> '{O000OOOOOO0O0O0OO}' ")#line:90
if __name__ =="__main__":#line:91
    try :#line:92
        find_proxies ()#line:93
        print ("All Proxy's Successfully Generated And Saved To File! Now use them to mass report")#line:94
    except KeyboardInterrupt :#line:95
        print ("\n\n"+Fore .RED +"[*] Program is closing!")#line:96
        print (Style .RESET_ALL )#line:97
        _exit (0 )#line:98
