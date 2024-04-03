# PySSH
# Version 1.1
# (C)2024 by KralicekGamer


import subprocess
import re
import shlex
import os
import urllib.request
from tkinter import messagebox

version = "1.1"
debug = False

green = "\033[32m"
yellow = "\033[93m"
red = "\033[31m"
reset = "\033[0m"


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(green + """                            
     _____     _____ _____ _____   
    |  _  |_ _|   __|   __|  |  |  
    |   __| | |__   |__   |     |  
    |__|  |_  |_____|_____|__|__|  
          |___|                    
    """"" + reset)

    print("""
    1. Open connection
    2. List conections
    3. Direct connection
    4. Add connection
    5. Delete conection
    8. Check version
    9. Exit
        """)


def open_connection():
    load_name = input("Name of connection: ")
    try:
        with open(load_name + ".ssh", 'r') as file:
            command = shlex.split(file.read())
    except FileNotFoundError:
        print(red + "[!] " + reset + "Invalid name of connection.")
        return

    if not command:
        return

    command = [part.strip("[],") for part in command]
    if debug:
        print(yellow + "[I] " + reset + " Command set:" + str(command))

    subprocess.run(command)
    welcome()


def list_connections():
    current_directory = os.getcwd()
    print()
    for file_name in os.listdir(current_directory):
        if file_name.endswith('.ssh'):
            file_name_without_extension = os.path.splitext(file_name)[0]
            print(file_name_without_extension)
    print()


def direct_connection():
    enter_ip = input("Enter IP: ")
    enter_port = input("Enter port (Default 22): ")
    enter_user = input("Enter username (Default root): ")

    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", enter_ip):
        print(red + "[!] " + reset + "Invalid IP address format")
        return
    if enter_port and not enter_port.isdigit():
        print(red + "[!] " + reset + "Invalid port number")
        return
    if not enter_port:
        enter_port = "22"
    if not enter_user:
        enter_user = "root"

    command = [
        'ssh.exe',
        '-p', enter_port,
        '-l', enter_user,
        enter_ip
    ]

    if debug:
        print(yellow + "[I] " + reset + "Command set:" + str(command))

    subprocess.run(command)
    welcome()


def add_connection():
    enter_ip = input("Enter IP: ")
    enter_port = input("Enter port (Default 22): ")
    enter_user = input("Enter username (Default root): ")
    enter_name = input("Enter name of connection: ")

    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", enter_ip):
        print(red + "[!] " + reset + "Invalid IP address format")
        return
    if enter_port and not enter_port.isdigit():
        print(red + "[!] " + reset + "Invalid port number")
        return
    if not enter_port:
        enter_port = "22"
    if not enter_user:
        enter_user = "root"

    command = [
        'ssh.exe',
        '-p', enter_port,
        '-l', enter_user,
        enter_ip
    ]

    if debug:
        print(yellow + "[I] " + reset + "Command set:" + str(command))

    command_name = enter_name + ".ssh"

    with open(command_name, 'w') as file:
        file.write(str(command))

    subprocess.run(command)
    welcome()


def delete_conection():
    enter_name = input("Enter name of connection: ")
    try:
        os.remove(enter_name + ".ssh")
    except FileNotFoundError:
        print(red + "[!] " + reset + "File not found")
        return
    welcome()


def check_version():
    def read(url):
        try:
            with urllib.request.urlopen(url) as response:
                html_content = response.read().decode('utf-8')
                text = re.sub('<[^<]+?>', '', html_content)

                return text.strip()
        except Exception as e:
            print(red + "[!] " + reset + f"Error: {e}")
            return None

    url_version = 'https://raw.githubusercontent.com/KralicekGamerCz/PySSH/main/version'
    text_web = read(url_version)

    if text_web and text_web != version:
        print("Old version: " + version)
        print("Newest version: " + text_web)
        cmd_update = input("Do you want to update? [y/n] ")
        if cmd_update == "y":
            messagebox.showinfo("Updater",
                                "Download the latest release on my github: https://github.com/KralicekGamerCz/PySSH")
            exit()

        elif cmd_update == "n":
            print("You chose not to update.")
        else:
            print(red + "[!] " + reset + "Error: Invalid input")

    else:
        print("\n" + "Stable version: " + version + "\n")


running_core = True
welcome()

while running_core:
    cmd = input(">>> ")

    if cmd == "1":
        open_connection()

    elif cmd == "2":
        list_connections()

    elif cmd == "3":
        direct_connection()

    elif cmd == "4":
        add_connection()

    elif cmd == "5":
        delete_conection()

    elif cmd == "8":
        check_version()

    elif cmd == "9":
        running_core = False

    elif cmd == "exit":
        running_core = False

    else:
        print(red + "[!] " + reset + "Invalid operation")
