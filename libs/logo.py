# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo =  """

██╗███╗░░██╗░██████╗████████╗░█████╗░    ██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
██║██╔██╗██║╚█████╗░░░░██║░░░███████║    ██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║    ██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║    ██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝    ╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░      
                                                                   
                                                                   """


def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)                                                  
    print(Fore.RED + "                                                      Youtube" + Fore.CYAN + " - Crevil ")
    print(Fore.RED + "                                                      BY     " + Fore.CYAN + " - @CREVIL")
    print(Fore.RED + "                                                      Telegram"+ Fore.CYAN + " - t.me/CrevilNetwork ")
    print(Fore.GREEN + "      Crevil Project: https://t.me/crevilProject"+ Style.RESET_ALL + Style.BRIGHT)
