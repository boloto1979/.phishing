import os
from colorama import Fore
import webbrowser

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux/Mac)
        os.system('clear')

def title():
    logo = (
        "         "+Fore.LIGHTCYAN_EX   +"              _     _     _     _             \n"
        "         "+Fore.LIGHTCYAN_EX   +"             | |   (_)   | |   (_)            \n"
        "         "+Fore.LIGHTCYAN_EX   +"        _ __ | |__  _ ___| |__  _ _ __   __ _ \n"
        "         "+Fore.LIGHTCYAN_EX   +"       | '_ \| '_ \| / __| '_ \| | '_ \ / _` |\n"
        "         "+Fore.LIGHTCYAN_EX   +"      _| |_) | | | | \__ \ | | | | | | | (_| |\n"
        "         "+Fore.LIGHTCYAN_EX   +"     (_) .__/|_| |_|_|___/_| |_|_|_| |_|\__, |\n"
        "         "+Fore.LIGHTCYAN_EX   +"       | |                               __/ |\n"
        "         "+Fore.LIGHTCYAN_EX   +"       |_|                "+Fore.LIGHTRED_EX   +"Version : 1.0 "+Fore.LIGHTCYAN_EX   +"|___/ \n"
        "\n"
        "       "+Fore.LIGHTCYAN_EX+"         ["+Fore.LIGHTWHITE_EX+"-"+Fore.LIGHTCYAN_EX+"] Tool Created by .phishing-project\n"
        "       "+Fore.LIGHTRED_EX+"           ["+Fore.LIGHTWHITE_EX+"::"+Fore.LIGHTRED_EX+"] "+Fore.LIGHTWHITE_EX+"Select a Site to Attack "+Fore.LIGHTRED_EX+"["+Fore.LIGHTWHITE_EX+"::"+Fore.LIGHTRED_EX+"]\n"
        "\n"
        "       "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "       "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[01] "+Fore.LIGHTWHITE_EX+"Facebook   "+Fore.LIGHTRED_EX+"[10] "+Fore.LIGHTWHITE_EX+"Linkedin   "+Fore.LIGHTRED_EX+"[19] "+Fore.LIGHTWHITE_EX+"Wordpress   "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[02] "+Fore.LIGHTWHITE_EX+"Instagram  "+Fore.LIGHTRED_EX+"[11] "+Fore.LIGHTWHITE_EX+"Twitch     "+Fore.LIGHTRED_EX+"[20] "+Fore.LIGHTWHITE_EX+"Playstation "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[03] "+Fore.LIGHTWHITE_EX+"Google     "+Fore.LIGHTRED_EX+"[12] "+Fore.LIGHTWHITE_EX+"Pinterest                   "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[04] "+Fore.LIGHTWHITE_EX+"Microsoft  "+Fore.LIGHTRED_EX+"[13] "+Fore.LIGHTWHITE_EX+"Ebay       "+Fore.LIGHTRED_EX+"[exit] "+Fore.LIGHTWHITE_EX+"Exit      "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[05] "+Fore.LIGHTWHITE_EX+"Netflix    "+Fore.LIGHTRED_EX+"[14] "+Fore.LIGHTWHITE_EX+"Dropbox    "+Fore.LIGHTRED_EX+"[help] "+Fore.LIGHTWHITE_EX+"Help      "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[06] "+Fore.LIGHTWHITE_EX+"Paypal     "+Fore.LIGHTRED_EX+"[15] "+Fore.LIGHTWHITE_EX+"Spotify                     "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[07] "+Fore.LIGHTWHITE_EX+"Steam      "+Fore.LIGHTRED_EX+"[16] "+Fore.LIGHTWHITE_EX+"Reddit                      "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[08] "+Fore.LIGHTWHITE_EX+"Twitter    "+Fore.LIGHTRED_EX+"[17] "+Fore.LIGHTWHITE_EX+"Adobe                       "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|   "+Fore.LIGHTRED_EX+"[09] "+Fore.LIGHTWHITE_EX+"Github     "+Fore.LIGHTRED_EX+"[18] "+Fore.LIGHTWHITE_EX+"Snapchat                    "+Fore.LIGHTCYAN_EX+"|\n"
        "       "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "       "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + logo)

def show_help():
    url = "https://github.com/phishing-project/.phishing"
    webbrowser.open(url)

def main():
    title()
    while True:
        user_input = input("~/.phishing $ ").strip().lower()

        if user_input == "help":
            show_help()
        elif user_input == "exit":
            print("Exiting .Phishing.")
            break
        elif user_input == "clear":
            clear_screen()
            title()

if __name__ == "__main__":
    main()