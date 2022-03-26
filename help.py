import webbrowser
import os
from colorama import Fore, Back, Style

from libs.utils import clearConsole
from libs.logo import print_logo

def help_msg():
    print(Style.RESET_ALL)
    que = print('''
${Fore.GREEN}============================== HELP  ==============================

    [1] Connection Error
    [2] Not banning account
    [3] More help
    [4] Exit
    ''')
    que_ans = input("Please select :- ")
    if (int(que_ans)==1):
        clearConsole()
        print('''

        [ ✔️ ] Connection error! (CookieErrorJSDatr)         = Cookies error
        [ ✔️ ] Connection error! STATUS CODE: !200           = Poor Internet
        [ ✔️ ] Connection error! (FacebookRequestsError)     = Poor proxies or not using proxies
        [ ✔️ ] Connection error! (CookieErrorLSD)            = '["LSD",[],{"token":"' not in response
        [ ✔️ ] Connection error! (CookieErrorRev)            = Server Revision
        [ ✔️ ] Connection error occurred (FormRequestsError) = Error while loading report page
        ''')
        help_msg()
    elif (int(que_ans) == 2):
        clearConsole()
        print('''
        
        Reasons why victim's account is not getting banned

        [ 1️⃣ ] The fact is that the account could be deleted by Instagram because of three or four 
        reports from various accounts due to the reason given for reporting the account. 
        All Instagram accounts reported in violation of the Community Guidelines or Terms of Use 
        will be deleted. Only accounts that meet one or both guidelines will be removed.

        [ 2️⃣ ] You don't have good proxies. You need to buy paid proxy or crack some good qualities.
        To buy proxies go to https://t.me/CrevilBot and ask proxy.

        [ ✔️ ] You can always buy premium version of this tool with more features like
        1. Paid proxy available with tool
        2. Ban confirm (more powerful)
        3. For more information contact me on telegram
         
        ''')
        help_msg()
    elif(int(que_ans)==3):
        clearConsole()
        print('''
        
        For more help you can directly contact me on https://t.me/CrevilBot
        Or you can report bugs at https://t.me/Hacker_Chatroom

        [ ✔️ ] You can always buy premium version of this tool with more features like
        1. Paid proxy available with tool
        2. Ban confirm (more powerful)
        3. For more information contact me on telegram
         
        ''')
        help_msg()
        webbrowser.open('http://t.me/Hacker_Chatroom')
    elif(int(que_ans)==4):
        clearConsole()
        os.system('python ReportBot.py' if os.name == 'nt' else 'bash run.sh')