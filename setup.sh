  #!/bin/bash

# colour 
Black="\033[1;30m"       # Black
Red="\033[1;31m"         # Red
Green="\033[1;32m"       # Green
Yellow="\033[1;33m"      # Yellow
Blue="\033[1;34m"        # Blue
Purple="\033[1;35m"      # Purple
Cyan="\033[1;36m"        # Cyan
White="\033[1;37m"       # White

clear
echo -e "$Purple Created By \e[1;34m"
       figlet Insta Report | lolcat
sleep 2.0
    echo -e " \e[96m  
                                     ████████ \e[0m"
echo "                                 ████████████████
                                   █─▄▀█──█▀▄─█
                                  ▐▌──────────▐▌"
echo -e    "\e[0m                                  █▌\e[91m▀▄──▄▄──▄▀\e[0m▐█"
echo -e    "\e[0m                                 ▐██──\e[91m▀▀\e[91m──▀▀──\e[0m██" 
echo "                                ▄████▄──▐▌──▄████▄"
echo -e    "\e[91m"  
echo " "  
figlet -f Bloody Insta-Hack | lolcat

    echo " "
    echo -e "$Red                                 ⫸ Coded by$Yellow Crevil$Red ⫷\033[0m"
    echo -e "$Red                               ⫸$Purple t.me/HackerExploits$Red ⫷\033[0m"
echo " "
echo -e " $Green     |---------------------------------------------------------------------------------|"
echo -e " $Green     ||----------------------------$Cyan [features] $Green----------------------------||"
echo -e " $Green     ||                                                                               ||"
echo -e " $Green     ||             $Purple==>$Yellow[1️⃣] Start Report Bot$Green                      ||"
echo -e " $Green     ||             $Purple==>️$Yellow[2️⃣] Help$Green                                  ||"
echo -e " $Green     ||             $Purple==>$Yellow[3️⃣] About$Green                                 ||"
echo -e " $Green     ||             $Purple==>$Yellow[4️⃣] Update scrip$Green                          ||"
echo -e " $Green     ||             $Purple==>$Yellow[5️⃣] exit$Green                                  ||"
echo -e " $Green     ||                                                                               ||"                                                                                       
echo -e " $Green     ||---------------------------$Cyan [select option] $Green------------------------||"
echo -e " $Green     |---------------------------------------------------------------------------------|"
echo " "
echo " "

    read ch
   if [ $ch -eq 1 ];then
        cd $HOME
        cd InstaReport
        python ReportBot.py

        exit
    elif [ $ch -eq 2 ];then
        cd $HOME
        cd InstaReport
        python help.py

        exit
    elif [ $ch -eq 3 ];then
        cd $HOME
        cd InstaReport
        python about.py

        exit

    elif [ $ch -eq 4 ];then
        echo -e "\e[1;34m Downloading Latest Files..."
        cd $HOME
        rm -rf InstaReport
        git clone https://github.com/Crevils/InstaReport
        cd InstaReport
        bash setup.sh
     
        exit
    elif [ $ch -eq 5 ];then
        echo -e 
        cd $HOME

        exit
        
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
