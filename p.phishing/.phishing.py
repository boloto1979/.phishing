import os
from colorama import Fore
import webbrowser
import shutil

def title():
    logo = (
        "                "+Fore.LIGHTCYAN_EX   +"             _     _     _     _                  "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"            | |   (_)   | |   (_)                 "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"       _ __ | |__  _ ___| |__  _ _ __   __ _      "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"      | '_ \| '_ \| / __| '_ \| | '_ \ / _` |     "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"     _| |_) | | | | \__ \ | | | | | | | (_| |     "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"    (_) .__/|_| |_|_|___/_| |_|_|_| |_|\__, |     "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"      | |                               __/ |     "+Fore.LIGHTCYAN_EX  +"\n"
        "                "+Fore.LIGHTCYAN_EX   +"      |_|                              |___/      "+Fore.LIGHTCYAN_EX  +"\n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                            "+Fore.LIGHTCYAN_EX +"       |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               Welcome to .Phishing.       "+Fore.LIGHTCYAN_EX  +"        |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"          To see the Commands, type [help].   "+Fore.LIGHTCYAN_EX +"     |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                 Use Responsibly!           "+Fore.LIGHTCYAN_EX +"       |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                            "+Fore.LIGHTCYAN_EX +"       |\n"
        "             "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + logo)

def show_help():
    help = (
        "\n"
        "             "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                          "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               [1] Site List              "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               [2] Github Repository      "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               [help] Show commands       "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               [clear] Clear the screen   "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"               [exit] Close Program       "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                          "+Fore.LIGHTCYAN_EX +"         |\n"
        "             "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + help)

def site_list():
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    site_folder = os.path.join(current_script_dir, "site")
    site = (
        "             "+Fore.LIGHTCYAN_EX   +"                      _____ _ _               "+Fore.LIGHTCYAN_EX  +"\n"
        "             "+Fore.LIGHTCYAN_EX   +"                     / ____(_) |              "+Fore.LIGHTCYAN_EX  +"\n"
        "             "+Fore.LIGHTCYAN_EX   +"                     | (___  _| |_ ___ ___    "+Fore.LIGHTCYAN_EX  +"\n"
        "             "+Fore.LIGHTCYAN_EX   +"                      \___ \| | __/ _ \ __|   "+Fore.LIGHTCYAN_EX  +"\n"
        "             "+Fore.LIGHTCYAN_EX   +"                      ____) | | |_  __\__ \   "+Fore.LIGHTCYAN_EX  +"\n"
        "             "+Fore.LIGHTCYAN_EX   +"                     |_____/|_|\__\___|___/   "+Fore.LIGHTCYAN_EX  +"\n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX   +"                       Use Responsibly!           "+Fore.LIGHTCYAN_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  __________________  __________________  __________________     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  |                |  |                |  |                |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [01] Facebook  |  | [11] Site List |  | [21] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [02] Site List |  | [12] Site List |  | [22] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [03] Site List |  | [13] Site List |  | [23] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [04] Site List |  | [14] Site List |  | [24] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [05] Site List |  | [15] Site List |  | [25] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [06] Site List |  | [16] Site List |  | [26] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [07] Site List |  | [17] Site List |  | [27] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [08] Site List |  | [18] Site List |  | [28] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [09] Site List |  | [19] Site List |  | [29] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [10] Site List |  | [20] Site List |  | [30] Site List |     "+Fore.LIGHTWHITE_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  |________________|  |________________|  |________________|     "+Fore.LIGHTWHITE_EX +"         \n"
        "\n"
        "               "+Fore.LIGHTCYAN_EX   +"                      Next Page [Next]           "+Fore.LIGHTCYAN_EX +"         \n" 

        "\n"
    )
    print(Fore.LIGHTCYAN_EX + site)
    while True:
        choice = input("Enter your choice [01-30]: ").strip().lower()

        if choice == "next":
            pass
        elif choice == "exit":
            break
        else:
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= 30:
                    file_name = f"{choice_num:02d}"
                    file_found = False

                    for file in os.listdir(site_folder):
                        if file.startswith(file_name) and os.path.isfile(os.path.join(site_folder, file)):
                            source_file_path = os.path.join(site_folder, file)

                            destination_folder = input("Enter the destination folder path: ").strip()
                            destination_file_path = os.path.join(destination_folder, file)

                            shutil.copyfile(source_file_path, destination_file_path)
                            print(f"File '{file}' downloaded to your computer.")
                            file_found = True
                            break
                    
                    if not file_found:
                        print(f"Error: File with the number '{file_name}' not found in the 'sites' folder.")
                else:
                    print("Error: Invalid choice. Please enter a number between 01 and 30.")
            except ValueError:
                print("Error: Invalid input. Please enter a number between 01 and 30.")

def open_github_repository():
    url = "https://github.com/phishing-project/.phishing"
    webbrowser.open(url)

def main():
    title()
    while True:
        user_input = input("~/.phishing $ ").strip().lower()

        if user_input == "help":
            show_help()
        if user_input == "1":
            site_list()
        elif user_input == "2":
            open_github_repository()
        elif user_input == "clear":
            if os.name == 'nt':  # Windows
                os.system('cls')
            else:  # Unix (Linux/Mac)
                os.system('clear')
            title()
        elif user_input == "exit":
            print("Exiting .Phishing.")
            break

if __name__ == "__main__":
    main()