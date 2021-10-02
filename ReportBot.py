#!/usr/bin/env python3
import time #line:3
from colorama import Fore ,Back ,Style ,init #line:4
init (autoreset =True )#line:5
def startMessage ():#line:7
    OO0O0OO0OOO0OO0O0 =input (Fore .YELLOW +"Enter Code To Unlock The Tool : ")#line:8
    OOOO0OO000OO0OOOO ="@hackerexploits"#line:9
    if OOOO0OO000OO0OOOO !=OO0O0OO0OOO0OO0O0 :#line:10
        print (Fore .RED +'[X] Wrong Code')#line:11
        print (Fore .BLUE +''' 
   1. Go to telegram
   2. Join http://t.me/hacker_Chatroom
   3. Send #Instareport In Group
   4. You Will Get Code For Free
   5. Next time come with code and use this tool
    ''')#line:18
        startMessage ()#line:19
    else :#line:20
        print (Fore .GREEN +"Successfully Unlocked Tool!")#line:21
        pass #line:22
if __name__ =="__main__":#line:24
    startMessage ()#line:25
from libs .check_modules import check_modules #line:27
from sys import exit #line:28
from os import _exit #line:29
check_modules ()#line:31
from os import path #line:33
from libs .logo import print_logo #line:35
from libs .utils import print_success #line:36
from libs .utils import print_error #line:37
from libs .utils import ask_question #line:38
from libs .utils import print_status #line:39
from libs .attack import report_profile_attack #line:40
from libs .attack import report_video_attack #line:41
from multiprocessing import Process #line:43
def chunks (O000O0O0OO000O0OO ,OOOOO0OOO00OO00OO ):#line:45
    ""#line:46
    for OOO0OO00O000OOO0O in range (0 ,len (O000O0O0OO000O0OO ),OOOOO0OOO00OO00OO ):#line:47
        yield O000O0O0OO000O0OO [OOO0OO00O000OOO0O :OOO0OO00O000OOO0O +OOOOO0OOO00OO00OO ]#line:48
def profile_attack_process (O0OOOOO00O0OO000O ,OOOOO0000OO00OOOO ):#line:50
    if (len (OOOOO0000OO00OOOO )==0 ):#line:51
        for _OOO00O0000O000O00 in range (10 ):#line:52
            report_profile_attack (O0OOOOO00O0OO000O ,None )#line:53
        return #line:54
    for OO00OO0OOOOO0OOOO in OOOOO0000OO00OOOO :#line:56
        report_profile_attack (O0OOOOO00O0OO000O ,OO00OO0OOOOO0OOOO )#line:57
def video_attack_process (O0O00O00O00OOO00O ,O0OO000OO0000OO0O ):#line:59
    if (len (O0OO000OO0000OO0O )==0 ):#line:60
        for _OOOO0O00000OOO0O0 in range (10 ):#line:61
            report_video_attack (O0O00O00O00OOO00O ,None )#line:62
        return #line:63
    for O0O0000OOO0OOO00O in O0OO000OO0000OO0O :#line:65
        report_video_attack (O0O00O00O00OOO00O ,O0O0000OOO0OOO00O )#line:66
def video_attack (OO0O00000000OOOOO ):#line:68
    OO000OO00000OO0O0 =ask_question ("Enter the link of the video you want to report")#line:69
    print (Style .RESET_ALL )#line:70
    if (len (OO0O00000000OOOOO )==0 ):#line:71
        for OO00O000OO0O0OO00 in range (5 ):#line:72
            O0OO00O0OO00OOO0O =Process (target =video_attack_process ,args =(OO000OO00000OO0O0 ,[],))#line:73
            O0OO00O0OO00OOO0O .start ()#line:74
            print_status (str (OO00O000OO0O0OO00 +1 )+". Transaction Opened!")#line:75
            if (OO00O000OO0O0OO00 ==5 ):print ()#line:76
        return #line:77
    OO0OOOOOOO0OOO000 =list (chunks (OO0O00000000OOOOO ,10 ))#line:79
    print ("")#line:81
    print_status ("Video complaint attack is on!\n")#line:82
    OO00O000OO0O0O000 =1 #line:84
    for OOOOO0O0OOO00O000 in OO0OOOOOOO0OOO000 :#line:85
        O0OO00O0OO00OOO0O =Process (target =video_attack_process ,args =(OO000OO00000OO0O0 ,OOOOO0O0OOO00O000 ,))#line:86
        O0OO00O0OO00OOO0O .start ()#line:87
        print_status (str (OO00O000OO0O0O000 )+". Transaction Opened!")#line:88
        if (OO00O000OO0O0O000 ==5 ):print ()#line:89
        OO00O000OO0O0O000 =OO00O000OO0O0O000 +1 #line:90
def profile_attack (OO00O0OOO00OOO0O0 ):#line:92
    OOOO0O00000OOO00O =ask_question ("Enter the username of the person you want to report")#line:93
    print (Style .RESET_ALL )#line:94
    if (len (OO00O0OOO00OOO0O0 )==0 ):#line:95
        for O00O00O00000OO0OO in range (5 ):#line:96
            O00000O000OOOOOO0 =Process (target =profile_attack_process ,args =(OOOO0O00000OOO00O ,[],))#line:97
            O00000O000OOOOOO0 .start ()#line:98
            print_status (str (O00O00O00000OO0OO +1 )+". Transaction Opened!")#line:99
        return #line:100
    OO00OOO0OO00OOOOO =list (chunks (OO00O0OOO00OOO0O0 ,10 ))#line:102
    print ("")#line:104
    print_status ("Profile complaint attack is starting!\n")#line:105
    O0OOOO0O00OOOOO0O =1 #line:107
    for OOOO0O00O0000OO00 in OO00OOO0OO00OOOOO :#line:108
        O00000O000OOOOOO0 =Process (target =profile_attack_process ,args =(OOOO0O00000OOO00O ,OOOO0O00O0000OO00 ,))#line:109
        O00000O000OOOOOO0 .start ()#line:110
        print_status (str (O0OOOO0O00OOOOO0O )+". Transaction Opened!")#line:111
        if (O0OOOO0O00OOOOO0O ==5 ):print ()#line:112
        O0OOOO0O00OOOOO0O =O0OOOO0O00OOOOO0O +1 #line:113
def main ():#line:115
    print_success ("Modules loaded!\n")#line:116
    O0OOO0O00OOO00O0O =ask_question ("Would you like to use a proxy? [Y / N]")#line:118
    O00O0OO00OOO0OO00 =[]#line:120
    if (O0OOO0O00OOO00O0O =="Y"or O0OOO0O00OOO00O0O =="y"):#line:122
        O0OOO0O00OOO00O0O =ask_question ("Would you like to collect your proxies from the internet? [Y / N]")#line:123
        if (O0OOO0O00OOO00O0O =="Y"or O0OOO0O00OOO00O0O =="y"):#line:125
            print_status ("PLEASE USE VPN AS YOU ARE USING THIS TOOL ON ANDROID")#line:126
        elif (O0OOO0O00OOO00O0O =="N"or O0OOO0O00OOO00O0O =="n"):#line:127
            print_status ("PLEASE USE VPN AS YOU ARE USING THIS TOOL ON ANDROID")#line:128
            pass #line:129
    elif (O0OOO0O00OOO00O0O =="N"or O0OOO0O00OOO00O0O =="n"):#line:130
        pass #line:131
    else :#line:132
        print_error ("Answer not understood, exiting!")#line:133
        exit ()#line:134
    print ("")#line:138
    print_status ("1 - Report Profile.")#line:139
    print_status ("2 - Report a video.")#line:140
    OOO0O0000OOO0O0OO =ask_question ("Please select the complaint method")#line:141
    print ("")#line:142
    if (OOO0O0000OOO0O0OO .isdigit ()==False ):#line:144
        print_error ("The answer is not understood.")#line:145
        exit (0 )#line:146
    if (int (OOO0O0000OOO0O0OO )>2 or int (OOO0O0000OOO0O0OO )==0 ):#line:148
        print_error ("The answer is not understood.")#line:149
        exit (0 )#line:150
    if (int (OOO0O0000OOO0O0OO )==1 ):#line:152
        profile_attack (O00O0OO00OOO0OO00 )#line:153
    elif (int (OOO0O0000OOO0O0OO )==2 ):#line:154
        video_attack (O00O0OO00OOO0OO00 )#line:155
if __name__ =="__main__":#line:157
    print_logo ()#line:158
    try :#line:159
        main ()#line:160
        print (Style .RESET_ALL )#line:161
    except KeyboardInterrupt :#line:162
        print ("\n\n"+Fore .RED +"[*] Program is closing!")#line:163
        print (Style .RESET_ALL )#line:164
        _exit (0 )