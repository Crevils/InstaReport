# coding=utf-8
#!/usr/bin/env python3

from colorama import Fore, Back, Style
from os import path
import re
import random
from requests import get
from sys import exit
        
def print_success(message, *argv):
    print(Fore.GREEN + "[ OK ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_error(message, *argv):
    print(Fore.RED + "[ ERR ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def print_status(message, *argv):
    print(Fore.BLUE + "[ * ] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end=" ")
    for arg in argv:
        print(arg, end=" ")
    print("")

def ask_question(message, *argv):
    message = Fore.BLUE + "[ ? ] " + Style.RESET_ALL + Style.BRIGHT + message
    for arg in argv:
        message = message + " " + arg
    print(message, end="")
    ret = input(": ")
    return ret

def parse_proxy_file(fpath):
    if (path.exists(fpath) == False):
        print("")
        print_error("Proxy file not found! (I wonder if you're taking the wrong path?)")
        print_error("Exiting From Program")
        exit(0)
    
    proxies = []
    with open(fpath, "r") as proxy_file:
        for line in proxy_file.readlines():
            line = line.replace(" ", "")
            line = line.replace("\r", "")
            line = line.replace("\n", "")
            
            if (line ==  ""):
                continue
            
            proxies.append(line)
    
    if (len(proxies) > 50):
        proxies = random.choices(proxies, 50)
        
    print("")
    print_success(str(len(proxies)) + " Proxies have been installed!")

    return proxies


