import time #line:1
import sys #line:2
import os #line:3
def load_animation ():#line:6
    OOO0OOOO0O00O0OOO ="starting your console application..."#line:7
    OOO0O0000O0OOO00O =len (OOO0OOOO0O00O0OOO )#line:8
    O0OO0OO00O0OOOOO0 ="|/-\\"#line:10
    O00OO00000O000O0O =0 #line:11
    OOO0O0O00OOO0OOO0 =0 #line:12
    OO0OOO00O00OO00O0 =0 #line:13
    while (OOO0O0O00OOO0OOO0 !=100 ):#line:15
        time .sleep (0.075 )#line:17
        O0O000O0O0O0O0OOO =list (OOO0OOOO0O00O0OOO )#line:18
        OOOOO00O0OO00OOO0 =ord (O0O000O0O0O0O0OOO [OO0OOO00O00OO00O0 ])#line:19
        OOOO0O00O00O0000O =0 #line:20
        if OOOOO00O0OO00OOO0 !=32 and OOOOO00O0OO00OOO0 !=46 :#line:21
            if OOOOO00O0OO00OOO0 >90 :#line:22
                OOOO0O00O00O0000O =OOOOO00O0OO00OOO0 -32 #line:23
            else :#line:24
                OOOO0O00O00O0000O =OOOOO00O0OO00OOO0 +32 #line:25
            O0O000O0O0O0O0OOO [OO0OOO00O00OO00O0 ]=chr (OOOO0O00O00O0000O )#line:26
        O00OOO0OO0O0O000O =''#line:27
        for OO0OO0OOOOOOO00O0 in range (OOO0O0000O0OOO00O ):#line:28
            O00OOO0OO0O0O000O =O00OOO0OO0O0O000O +O0O000O0O0O0O0OOO [OO0OO0OOOOOOO00O0 ]#line:29
        sys .stdout .write ("\r"+O00OOO0OO0O0O000O +O0OO0OO00O0OOOOO0 [O00OO00000O000O0O ])#line:30
        sys .stdout .flush ()#line:31
        OOO0OOOO0O00O0OOO =O00OOO0OO0O0O000O #line:33
        O00OO00000O000O0O =(O00OO00000O000O0O +1 )%4 #line:35
        OO0OOO00O00OO00O0 =(OO0OOO00O00OO00O0 +1 )%OOO0O0000O0OOO00O #line:36
        OOO0O0O00OOO0OOO0 =OOO0O0O00OOO0OOO0 +1 #line:37
    if os .name =="nt":#line:40
        os .system ("cls")#line:41
    else :#line:44
        os .system ("clear")#line:45
def animation_bar ():#line:48
    O000O0OOO0O00O000 =[Fore .RED +"[     =             ]",Fore .RED +"[     ==            ]",Fore .GREEN +"[     ====          ]",Fore .CYAN +"[     =====         ]",Fore .CYAN +"[     ======        ]",Fore .BLUE +"[     =======       ]",Fore .GREEN +"[     ========      ]",Fore .GREEN +"[     ===========   ]",Fore .RED +"[      ========     ]",Fore .BLUE +"[       =======     ]",Fore .BLUE +"[        ======     ]",Fore .CYAN +"[         =====     ]",Fore .RED +"[          ====     ]",Fore .RED +"[           ===     ]",Fore .RED +"[            ==     ]",Fore .CYAN +"[             =     ]",Fore .CYAN +"[                  ]"]#line:67
    O0000000000000OO0 =True #line:69
    OO00OO0O00OOOO0O0 =0 #line:70
    while O0000000000000OO0 :#line:71
            print (O000O0OOO0O00O000 [OO00OO0O00OOOO0O0 %len (O000O0OOO0O00O000 )],end ='\r')#line:72
            time .sleep (.1 )#line:73
            OO00OO0O00OOOO0O0 +=1 #line:74
            if OO00OO0O00OOOO0O0 ==10 *6 :#line:75
                break #line:76
def starting_bot ():#line:79
    O0OOOOOO000000OOO ="|/-\\"#line:81
    for O0O00OOOOOOOOO0OO in range (40 ):#line:83
            time .sleep (0.1 )#line:84
            sys .stdout .write (" Starting Bot...."+"\r"+O0OOOOOO000000OOO [O0O00OOOOOOOOO0OO %len (O0OOOOOO000000OOO )])#line:86
            sys .stdout .flush ()#line:87
def colorText (O0OO00O00000O0O00 ):#line:92
    O0O0OOOOO0000000O ={"black":"\u001b[30;1m","red":"\u001b[31;1m","green":"\u001b[32m","yellow":"\u001b[33;1m","blue":"\u001b[34;1m","magenta":"\u001b[35m","cyan":"\u001b[36m","white":"\u001b[37m","yellow-background":"\u001b[43m","black-background":"\u001b[40m","black-bright-background":"\u001b[40;1m","green-background":"\u001b[42m","reset":"\u001b[0m",}#line:108
    os .system ("cls")#line:109
    for O0000OO000OOO000O in O0O0OOOOO0000000O :#line:110
        O0OO00O00000O0O00 =O0OO00O00000O0O00 .replace ("[["+O0000OO000OOO000O +"]]",O0O0OOOOO0000000O [O0000OO000OOO000O ])#line:111
    return O0OO00O00000O0O00 #line:112
