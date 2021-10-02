#!/usr/bin/env python3
from requests import Session #line:4
from sys import exit #line:5
import string #line:6
import random #line:7
import pprint #line:9
from libs .utils import print_success #line:11
from libs .utils import print_error #line:12
from libs .utils import ask_question #line:13
from libs .utils import print_status #line:14
from libs .user_agents import get_user_agent #line:15
page_headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","DNT":"1",}#line:24
report_headers ={"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3","Cache-Control":"no-cache","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded","DNT":"1","Host":"help.instagram.com","Origin":"help.instagram.com","Pragma":"no-cache","Referer":"https://help.instagram.com/contact/497253480400030","TE":"Trailers",}#line:39
def random_str (OOO0OO00OO0OO00OO ):#line:41
    O0000O0OOOO0OOOO0 =string .ascii_lowercase +string .ascii_uppercase +string .digits #line:42
    return ''.join (random .choice (O0000O0OOOO0OOOO0 )for O0O00OO0OO0OO000O in range (OOO0OO00OO0OO00OO ))#line:43
def report_profile_attack (OO000O00000OOO000 ,O0OO000OO0OO00OO0 ):#line:45
    OO0OO000000OOO0O0 =Session ()#line:46
    if (O0OO000OO0OO00OO0 !=None ):#line:48
        OO0OO000000OOO0O0 .proxies ={"https":"https://"+O0OO000OO0OO00OO0 ,"http":"https://"+O0OO000OO0OO00OO0 }#line:52
    OO0000O000OO0000O =get_user_agent ()#line:54
    page_headers ["User-Agent"]=OO0000O000OO0000O #line:56
    report_headers ["User-Agent"]=OO0000O000OO0000O #line:57
    try :#line:59
        OO0O00O0O00OOO000 =OO0OO000000OOO0O0 .get ("https://www.facebook.com/",timeout =10 )#line:60
    except :#line:61
        print_error ("Connection error occurred! (FacebookRequestsError)")#line:62
        return #line:63
    if (OO0O00O0O00OOO000 .status_code !=200 ):#line:65
        print_error ("Connection error occurred! (STATUS CODE:",OO0O00O0O00OOO000 .status_code ,")")#line:66
        return #line:67
    if ('["_js_datr","'not in OO0O00O0O00OOO000 .text ):#line:69
        print_error ("Connection error occurred! (CookieErrorJSDatr)")#line:70
        return #line:71
    try :#line:73
        O000000O0OOOO0OOO =OO0O00O0O00OOO000 .text .split ('["_js_datr","')[1 ].split ('",')[0 ]#line:74
    except :#line:75
        print_error ("Connection error occurred! (CookieParsingError)")#line:76
        return #line:77
    OO0OOO0O00OOOO0O0 ={"_js_datr":O000000O0OOOO0OOO }#line:81
    try :#line:83
        OO0O00O0O00OOO000 =OO0OO000000OOO0O0 .get ("https://help.instagram.com/contact/497253480400030",cookies =OO0OOO0O00OOOO0O0 ,headers =page_headers ,timeout =10 )#line:84
    except :#line:85
        print_error ("Connection error occurred! (InstagramRequestsError)")#line:86
        return #line:87
    if (OO0O00O0O00OOO000 .status_code !=200 ):#line:89
        print_error ("Connection error occurred! (STATUS CODE:",OO0O00O0O00OOO000 .status_code ,")")#line:90
        return #line:91
    if ("datr"not in OO0O00O0O00OOO000 .cookies .get_dict ()):#line:93
        print_error ("Connection error occurred! (CookieErrorDatr)")#line:94
        return #line:95
    if ('["LSD",[],{"token":"'not in OO0O00O0O00OOO000 .text ):#line:97
        print_error ("Connection error occurred! (CookieErrorLSD)")#line:98
        return #line:99
    if ('"__spin_r":'not in OO0O00O0O00OOO000 .text ):#line:101
        print_error ("Connection error occurred! (CookieErrorSpinR)")#line:102
        return #line:103
    if ('"__spin_b":'not in OO0O00O0O00OOO000 .text ):#line:105
        print_error ("Connection error occurred!  (CookieErrorSpinB)")#line:106
        return #line:107
    if ('"__spin_t":'not in OO0O00O0O00OOO000 .text ):#line:109
        print_error ("Connection error occurred! (CookieErrorSpinT)")#line:110
        return #line:111
    if ('"server_revision":'not in OO0O00O0O00OOO000 .text ):#line:113
        print_error ("Connection error occurred! (CookieErrorRev)")#line:114
        return #line:115
    if ('"hsi":'not in OO0O00O0O00OOO000 .text ):#line:117
        print_error ("Connection error occurred! (CookieErrorHsi)")#line:118
        return #line:119
    try :#line:121
        O0OOO000OOOO0OO0O =OO0O00O0O00OOO000 .text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]#line:122
        O000OO0O000OOO0OO =OO0O00O0O00OOO000 .text .split ('"__spin_r":')[1 ].split (',')[0 ]#line:123
        OOOO0OO0O000O00O0 =OO0O00O0O00OOO000 .text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")#line:124
        O000000O00O00O0O0 =OO0O00O0O00OOO000 .text .split ('"__spin_t":')[1 ].split (',')[0 ]#line:125
        OO00OOO0OO0OOOOO0 =OO0O00O0O00OOO000 .text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")#line:126
        O0OOO00O000O0000O =OO0O00O0O00OOO000 .text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")#line:127
        OOOOO00OO0OO0000O =OO0O00O0O00OOO000 .cookies .get_dict ()["datr"]#line:128
    except :#line:129
        print_error ("Connection error occurred! (CookieParsingError)")#line:130
        return #line:131
    O0OO0000OOOOO00OO ={"datr":OOOOO00OO0OO0000O }#line:135
    OO000000O0O000O0O ={"jazoest":"2723","lsd":O0OOO000OOOO0OO0O ,"instagram_username":OO000O00000OOO000 ,"Field241164302734019_iso2_country_code":"TR","Field241164302734019":"Türkiye","support_form_id":"497253480400030","support_form_hidden_fields":"{}","support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":O0OOO00O000O0000O ,"__s":"5gbxno:2obi73:56i3vc","__hsi":OO00OOO0OO0OOOOO0 ,"__comet_req":"0","__spin_r":O000OO0O000OOO0OO ,"__spin_b":OOOO0OO0O000O00O0 ,"__spin_t":O000000O00O00O0O0 }#line:161
    try :#line:163
        OO0O00O0O00OOO000 =OO0OO000000OOO0O0 .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =OO000000O0O000O0O ,headers =report_headers ,cookies =O0OO0000OOOOO00OO ,timeout =10 )#line:170
    except :#line:171
        print_error ("Connection error occurred! (FormRequestsError)")#line:172
        return #line:173
    if (OO0O00O0O00OOO000 .status_code !=200 ):#line:175
        print_error ("Connection error occurred! (STATUS CODE:",OO0O00O0O00OOO000 .status_code ,")")#line:176
        return #line:177
    print_success ("Successfully reported!")#line:179
def report_video_attack (O0O0O0OOO0O00OOO0 ,OO0O00O0O000OOO0O ):#line:181
    O0OO0O0O00O0O00OO =Session ()#line:182
    if (OO0O00O0O000OOO0O !=None ):#line:183
        O0OO0O0O00O0O00OO .proxies ={"https":"https://"+OO0O00O0O000OOO0O ,"http":"https://"+OO0O00O0O000OOO0O }#line:187
    O00000000OO00OOO0 =get_user_agent ()#line:189
    page_headers ["User-Agent"]=O00000000OO00OOO0 #line:191
    report_headers ["User-Agent"]=O00000000OO00OOO0 #line:192
    try :#line:194
        O000OOOOOO0OO0O0O =O0OO0O0O00O0O00OO .get ("https://www.facebook.com/",timeout =10 )#line:195
    except Exception as OO000O0OO00OOO0O0 :#line:196
        print_error ("Connection error occurred! (FacebookRequestsError)",OO000O0OO00OOO0O0 )#line:197
        return #line:198
    if (O000OOOOOO0OO0O0O .status_code !=200 ):#line:200
        print_error ("Connection error occurred! (STATUS CODE:",O000OOOOOO0OO0O0O .status_code ,")")#line:201
        return #line:202
    if ('["_js_datr","'not in O000OOOOOO0OO0O0O .text ):#line:204
        print_error ("Connection error occurred! (CookieErrorJSDatr)")#line:205
        return #line:206
    try :#line:208
        O000O000OOOO00O0O =O000OOOOOO0OO0O0O .text .split ('["_js_datr","')[1 ].split ('",')[0 ]#line:209
    except :#line:210
        print_error ("Connection error occurred! (CookieParsingError)")#line:211
        return #line:212
    O0OO0000O00OOO0O0 ={"_js_datr":O000O000OOOO00O0O }#line:216
    try :#line:218
        O000OOOOOO0OO0O0O =O0OO0O0O00O0O00OO .get ("https://help.instagram.com/contact/497253480400030",cookies =O0OO0000O00OOO0O0 ,headers =page_headers ,timeout =10 )#line:219
    except :#line:220
        print_error ("Connection error occurred! (InstagramRequestsError)")#line:221
        return #line:222
    if (O000OOOOOO0OO0O0O .status_code !=200 ):#line:224
        print_error ("Connection error occurred! (STATUS CODE:",O000OOOOOO0OO0O0O .status_code ,")")#line:225
        return #line:226
    if ("datr"not in O000OOOOOO0OO0O0O .cookies .get_dict ()):#line:228
        print_error ("Connection error occurred! (CookieErrorDatr)")#line:229
        return #line:230
    if ('["LSD",[],{"token":"'not in O000OOOOOO0OO0O0O .text ):#line:232
        print_error ("Connection error occurred! (CookieErrorLSD)")#line:233
        return #line:234
    if ('"__spin_r":'not in O000OOOOOO0OO0O0O .text ):#line:236
        print_error ("Connection error occurred! (CookieErrorSpinR)")#line:237
        return #line:238
    if ('"__spin_b":'not in O000OOOOOO0OO0O0O .text ):#line:240
        print_error ("Connection error occurred! (CookieErrorSpinB)")#line:241
        return #line:242
    if ('"__spin_t":'not in O000OOOOOO0OO0O0O .text ):#line:244
        print_error ("Connection error occurred! (CookieErrorSpinT)")#line:245
        return #line:246
    if ('"server_revision":'not in O000OOOOOO0OO0O0O .text ):#line:248
        print_error ("Connection error occurred! (CookieErrorRev)")#line:249
        return #line:250
    if ('"hsi":'not in O000OOOOOO0OO0O0O .text ):#line:252
        print_error ("Connection error occurred! (CookieErrorHsi)")#line:253
        return #line:254
    try :#line:256
        O0OO00000O000O0O0 =O000OOOOOO0OO0O0O .text .split ('["LSD",[],{"token":"')[1 ].split ('"},')[0 ]#line:257
        O00OOO0O00000O00O =O000OOOOOO0OO0O0O .text .split ('"__spin_r":')[1 ].split (',')[0 ]#line:258
        OO000OO0OO0O0000O =O000OOOOOO0OO0O0O .text .split ('"__spin_b":')[1 ].split (',')[0 ].replace ('"',"")#line:259
        O0O00O0OO0OO00O00 =O000OOOOOO0OO0O0O .text .split ('"__spin_t":')[1 ].split (',')[0 ]#line:260
        O0000OOO0OOO000O0 =O000OOOOOO0OO0O0O .text .split ('"hsi":')[1 ].split (',')[0 ].replace ('"',"")#line:261
        O00O0OO0O00OOO000 =O000OOOOOO0OO0O0O .text .split ('"server_revision":')[1 ].split (',')[0 ].replace ('"',"")#line:262
        O0OOOOOO0O00000O0 =O000OOOOOO0OO0O0O .cookies .get_dict ()["datr"]#line:263
    except :#line:264
        print_error ("Connection error occurred! (CookieParsingError)")#line:265
        return #line:266
    OOO0OOOOOOOOOO0OO ={"datr":O0OOOOOO0O00000O0 }#line:270
    OO00000OO00O0O0OO ={"jazoest":"2723","lsd":O0OO00000O000O0O0 ,"sneakyhidden":"","Field419623844841592":O0O0O0OOO0O00OOO0 ,"Field1476905342523314_iso2_country_code":"TR","Field1476905342523314":"Türkiye","support_form_id":"440963189380968","support_form_hidden_fields":'{"423417021136459":false,"419623844841592":false,"754839691215928":false,"1476905342523314":false,"284770995012493":true,"237926093076239":false}',"support_form_fact_false_fields":"[]","__user":"0","__a":"1","__dyn":"7xe6Fo4SQ1PyUhxOnFwn84a2i5U4e1Fx-ey8kxx0LxW0DUeUhw5cx60Vo1upE4W0OE2WxO0SobEa81Vrzo5-0jx0Fwww6DwtU6e","__csr":"","__req":"d","__beoa":"0","__pc":"PHASED:DEFAULT","dpr":"1","__rev":O00O0OO0O00OOO000 ,"__s":"5gbxno:2obi73:56i3vc","__hsi":O0000OOO0OOO000O0 ,"__comet_req":"0","__spin_r":O00OOO0O00000O00O ,"__spin_b":OO000OO0OO0O0000O ,"__spin_t":O0O00O0OO0OO00O00 }#line:297
    try :#line:299
        O000OOOOOO0OO0O0O =O0OO0O0O00O0O00OO .post ("https://help.instagram.com/ajax/help/contact/submit/page",data =OO00000OO00O0O0OO ,headers =report_headers ,cookies =OOO0OOOOOOOOOO0OO ,timeout =10 )#line:306
    except :#line:307
        print_error ("Connection error occurred!! (FormRequestsError)")#line:308
        return #line:309
    if (O000OOOOOO0OO0O0O .status_code !=200 ):#line:311
        print_error ("Connection error occurred!! (STATUS CODE:",O000OOOOOO0OO0O0O .status_code ,")")#line:312
        return #line:313
    print_success ("Successfully reported!")#line:315
