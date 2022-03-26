#!/usr/bin/env python3
from requests import Session #line:2
from sys import exit #line:3
import string #line:4
import random #line:5
import pprint #line:6
from libs .utils import print_success #line:7
from libs .utils import print_error #line:8
from libs .utils import print_status #line:9
from libs .utils import parse_proxy_file #line:10
from libs .user_agents import get_user_agent #line:11
page_headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","DNT":"1",}#line:12
report_headers ={"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","DNT":"1","Host":"help.instagram.com","Origin":"help.instagram.com","Pragma":"no-cache","Referer":"https://help.instagram.com/contact/497253480400030","TE":"Trailers",}#line:13
def random_str (O0O0000000000OOOO ):#line:14
    O00O0OO0O0O0OOOOO =string .ascii_lowercase +string .ascii_uppercase +string .digits #line:15
    return ''.join (random .choice (O00O0OO0O0O0OOOOO )for O0OOO00OO0O0OO00O in range (O0O0000000000OOOO ))#line:16
def report_profile_attack (OOOO00O0O0O0OOOOO ,O00O000OOO000O0OO ):#line:17
    OOOOOOO0OO00000OO =Session ()#line:18
    if (O00O000OOO000O0OO !=None ):#line:19
        OOOOOOO0OO00000OO .proxies ={"https":"https://"+O00O000OOO000O0OO ,"http":"https://"+O00O000OOO000O0OO }#line:20
    O00O0000OO0OOOO00 =get_user_agent ()#line:21
    page_headers ["User-Agent"]=O00O0000OO0OOOO00 #line:22
    report_headers ["User-Agent"]=O00O0000OO0OOOO00 #line:23
    try :#line:24
        O00O0000OOO0O00OO =OOOOOOO0OO00000OO .get ("https://www.facebook.com/",timeout =10 )#line:25
    except :#line:26
        print_error ("Connection error! (FacebookRequestsError)")#line:27
        return #line:28
    if (O00O0000OOO0O00OO .status_code !=200 ):#line:29
        print_error ("Connection error! (STATUS CODE:",O00O0000OOO0O00OO .status_code ,")")#line:30
        return #line:31
    if ('["_js_datr","'not in O00O0000OOO0O00OO .text ):#line:32
        print_error ("Connection error! (CookieErrorJSDatr)")#line:33
        return #line:34
    try :#line:35
        OO000O0O00O000O00 =O00O0000OOO0O00OO .text .split ('["_js_datr","')[1 ].split ('",')[0 ]#line:36
    except :#line:37
        print_error ("Connection error! (CookieParsingError)")#line:38
        return #line:39
    O0000OO0OOO000O0O ={"_js_datr":OO000O0O00O000O00 }#line:40
    try :#line:41
        O00O0000OOO0O00OO =OOOOOOO0OO00000OO .get ("https://help.instagram.com/contact/497253480400030",cookies =O0000OO0OOO000O0O ,headers =page_headers ,timeout =10 )#line:42
    except :#line:43
        print_error ("Connection error! (InstagramRequestsError)")#line:44
        return #line:45
    if (O00O0000OOO0O00OO .status_code !=200 ):#line:46
        print_error ("Connection error! (STATUS CODE:",O00O0000OOO0O00OO .status_code ,")")#line:47
        return #line:48
    if ("datr"not in O00O0000OOO0O00OO .cookies .get_dict ()):#line:49
        print_error ("Connection error! (CookieErrorDatr)")#line:50
        return #line:51
    if ('["LSD",[],{"token":"'not in O00O0000OOO0O00OO .text ):#line:52
        print_error ("Connection error! (CookieErrorLSD)")#line:53
        return #line:54
    if ('"__spin_r":'not in O00O0000OOO0O00OO .text ):#line:55
        print_error ("Connection error! (CookieErrorSpinR)")#line:56
        return #line:57
    if ('"__spin_b":'not in O00O0000OOO0O00OO .text ):#line:58
        print_error ("Connection error! (CookieErrorSpinB)")#line:59
        return #line:60
    if ('"__spin_t":'not in O00O0000OOO0O00OO .text ):#line:61
        print_error ("Connection error! (CookieErrorSpinT)")#line:62
        return #line:63
    if ('"server_revision":'not in O00O0000OOO0O00OO .text ):#line:64
        print_error ("Connection error! (CookieErrorRev)")#line:65
        return #line:66
    if ('"hsi":'not in O00O0000OOO0O00OO .text ):#line:67
        print_error ("Connection error! (CookieErrorHsi)")#line:68
        return #line:69
    try :#line:70
        OOOOOO000OOOO0O00 =O00O0000OOO0O00OO .text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]#line:71
        OO00O0O0O00OOOOO0 =O00O0000OOO0O00OO .text .split ('"__spin_r":')[1 ].split (',')[0 ]#line:72
        OO00OO000OO000OO0 =O00O0000OOO0O00OO .text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")#line:73
        O00O0O0O0O00O0O00 =O00O0000OOO0O00OO .text .split ('"__spin_t":')[1 ].split (',')[0 ]#line:74
        OO0O0OO00OOOOOO0O =O00O0000OOO0O00OO .text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")#line:75
        O000OO0OOO00000OO =O00O0000OOO0O00OO .text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")#line:76
        O0O0OOOOOO00O00OO =O00O0000OOO0O00OO .cookies .get_dict ()["datr"]#line:77
    except :#line:78
        print_error ("Connection error! (CookieParsingError)")#line:79
        return #line:80
    OOOO0O00O0O0OO000 ={"datr":O0O0OOOOOO00O00OO }#line:81
    O0O00OOO0000O0O00 ={"jazoest":"2723","lsd":OOOOOO000OOOO0O00 ,"instagram_username":OOOO00O0O0O0OOOOO ,"Field241164302734019_iso2_country_code":"TR","Field241164302734019":"Türkiye","support_form_id":"497253480400030","support_form_hidden_fields":"{}","support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":O000OO0OOO00000OO ,"__s":"5gbxno:2obi73:56i3vc","__hsi":OO0O0OO00OOOOOO0O ,"__comet_req":"0","__spin_r":OO00O0O0O00OOOOO0 ,"__spin_b":OO00OO000OO000OO0 ,"__spin_t":O00O0O0O0O00O0O00 }#line:82
    try :#line:83
        O00O0000OOO0O00OO =OOOOOOO0OO00000OO .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =O0O00OOO0000O0O00 ,headers =report_headers ,cookies =OOOO0O00O0O0OO000 ,timeout =10 )#line:84
    except :#line:85
        print_error ("Connection error occurred (FormRequestsError)")#line:86
        return #line:87
    if (O00O0000OOO0O00OO .status_code !=200 ):#line:88
        print_error ("Connection error occurred (STATUS CODE:",O00O0000OOO0O00OO .status_code ,")")#line:89
        return #line:90
    print_success ("Successfully reported!")#line:91
def report_video_attack (O0O0OO00OOOO00O00 ,O00O0OOOOOO0O0O0O ):#line:92
    O000OOOO0O000O0OO =Session ()#line:93
    if (O00O0OOOOOO0O0O0O !=None ):#line:94
        O000OOOO0O000O0OO .proxies ={"https":"https://"+O00O0OOOOOO0O0O0O ,"http":"https://"+O00O0OOOOOO0O0O0O }#line:95
    O000OO00OOOO0OO0O =get_user_agent ()#line:96
    page_headers ["User-Agent"]=O000OO00OOOO0OO0O #line:97
    report_headers ["User-Agent"]=O000OO00OOOO0OO0O #line:98
    try :#line:99
        OOO0OO0O0OOOO00O0 =O000OOOO0O000O0OO .get ("https://www.facebook.com/",timeout =10 )#line:100
    except Exception as O00OO0OO000OOO0O0 :#line:101
        print_error ("Connection error! (FacebookRequestsError)",O00OO0OO000OOO0O0 )#line:102
        return #line:103
    if (OOO0OO0O0OOOO00O0 .status_code !=200 ):#line:104
        print_error ("Connection error! (STATUS CODE:",OOO0OO0O0OOOO00O0 .status_code ,")")#line:105
        return #line:106
    if ('["_js_datr","'not in OOO0OO0O0OOOO00O0 .text ):#line:107
        print_error ("Connection error! (CookieErrorJSDatr)")#line:108
        return #line:109
    try :#line:110
        OOOO0000OO0O0O0O0 =OOO0OO0O0OOOO00O0 .text .split ('["_js_datr","')[1 ].split ('",')[0 ]#line:111
    except :#line:112
        print_error ("Connection error! (CookieParsingError)")#line:113
        return #line:114
    OO0O00OOOO00O00O0 ={"_js_datr":OOOO0000OO0O0O0O0 }#line:115
    try :#line:116
        OOO0OO0O0OOOO00O0 =O000OOOO0O000O0OO .get ("https://help.instagram.com/contact/497253480400030",cookies =OO0O00OOOO00O00O0 ,headers =page_headers ,timeout =10 )#line:117
    except :#line:118
        print_error ("Connection error! (InstagramRequestsError)")#line:119
        return #line:120
    if (OOO0OO0O0OOOO00O0 .status_code !=200 ):#line:121
        print_error ("Connection error! (STATUS CODE:",OOO0OO0O0OOOO00O0 .status_code ,")")#line:122
        return #line:123
    if ("datr"not in OOO0OO0O0OOOO00O0 .cookies .get_dict ()):#line:124
        print_error ("Connection error! (CookieErrorDatr)")#line:125
        return #line:126
    if ('["LSD",[],{"token":"'not in OOO0OO0O0OOOO00O0 .text ):#line:127
        print_error ("Connection error! (CookieErrorLSD)")#line:128
        return #line:129
    if ('"__spin_r":'not in OOO0OO0O0OOOO00O0 .text ):#line:130
        print_error ("Connection error! (CookieErrorSpinR)")#line:131
        return #line:132
    if ('"__spin_b":'not in OOO0OO0O0OOOO00O0 .text ):#line:133
        print_error ("Connection error! (CookieErrorSpinB)")#line:134
        return #line:135
    if ('"__spin_t":'not in OOO0OO0O0OOOO00O0 .text ):#line:136
        print_error ("Connection error! (CookieErrorSpinT)")#line:137
        return #line:138
    if ('"server_revision":'not in OOO0OO0O0OOOO00O0 .text ):#line:139
        print_error ("Connection error! (CookieErrorRev)")#line:140
        return #line:141
    if ('"hsi":'not in OOO0OO0O0OOOO00O0 .text ):#line:142
        print_error ("Connection error! (CookieErrorHsi)")#line:143
        return #line:144
    try :#line:145
        O0O0000OO0OO0OO0O =OOO0OO0O0OOOO00O0 .text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]#line:146
        OO0000O000OOO00OO =OOO0OO0O0OOOO00O0 .text .split ('"__spin_r":')[1 ].split (',')[0 ]#line:147
        OO0O0OOOOO00OOOO0 =OOO0OO0O0OOOO00O0 .text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")#line:148
        OOO0O0OO0OO0OO00O =OOO0OO0O0OOOO00O0 .text .split ('"__spin_t":')[1 ].split (',')[0 ]#line:149
        OOO0OO00OO0OO0000 =OOO0OO0O0OOOO00O0 .text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")#line:150
        OO0O0O0OOO0000O0O =OOO0OO0O0OOOO00O0 .text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")#line:151
        OOOO0000O000O00OO =OOO0OO0O0OOOO00O0 .cookies .get_dict ()["datr"]#line:152
    except :#line:153
        print_error ("Connection error! (CookieParsingError)")#line:154
        return #line:155
    OO0OOO00O000OOO0O ={"datr":OOOO0000O000O00OO }#line:156
    O0O00OOOO00O00OOO ={"jazoest":"2723","lsd":O0O0000OO0OO0OO0O ,"sneakyhidden":"","Field419623844841592":O0O0OO00OOOO00O00 ,"Field1476905342523314_iso2_country_code":"TR","Field1476905342523314":"Türkiye","support_form_id":"440963189380968","support_form_hidden_fields":'{"423417021136459":false,"419623844841592":false,"754839691215928":false,"1476905342523314":false,"284770995012493":true,"237926093076239":false}',"support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":OO0O0O0OOO0000O0O ,"__s":"5gbxno:2obi73:56i3vc","__hsi":OOO0OO00OO0OO0000 ,"__comet_req":"0","__spin_r":OO0000O000OOO00OO ,"__spin_b":OO0O0OOOOO00OOOO0 ,"__spin_t":OOO0O0OO0OO0OO00O }#line:157
    try :#line:158
        OOO0OO0O0OOOO00O0 =O000OOOO0O000O0OO .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =O0O00OOOO00O00OOO ,headers =report_headers ,cookies =OO0OOO00O000OOO0O ,timeout =10 )#line:159
    except :#line:160
        print_error ("Connection error! (FormRequestsError)")#line:161
        return #line:162
    if (OOO0OO0O0OOOO00O0 .status_code !=200 ):#line:163
        print_error ("Connection error! (STATUS CODE:",OOO0OO0O0OOOO00O0 .status_code ,")")#line:164
        return #line:165
    print_success ("Successfully reported!")