'''
Don't forget to give credits : D
Author : https://github.com/crevils
Original Repositary : https://github.com/crevils/InstaReport
'''

import argparse
from report_accounts import report_accounts
from loading_screen import show_loading_screen
from Banner import show_banner

def get_options():
    parser = argparse.ArgumentParser(description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--username", type=str, default="", help="Username to report.")
    parser.add_argument("-f", "--file", type=str, default="acc.txt", help="Accounts list (Defaults to acc.txt in program directory).")
    return parser.parse_args()

def main():
    args = get_options()
    username = args.username
    accounts_file = args.file
    show_banner()
    show_loading_screen(3)
    if username == "":
        username = input("Username: ")

    show_loading_screen(3)
    report_accounts(username, accounts_file)

if __name__ == "__main__":
    main()
