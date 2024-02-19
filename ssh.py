# PySSH
# Version 1.0.2
# (C)2024 by KralicekGamer


import subprocess
import re
import shlex
import os
import urllib.request
import webbrowser
from tkinter import messagebox

version = "1.0.2"
debug = False

green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"


def open_connection():
    load_name = input("Name of connection: ")
    try:
        with open(load_name + ".ssh", 'r') as file:
            command = shlex.split(file.read())
    except FileNotFoundError:
        print("Invalid name of connection.")
        return

    if not command:
        return

    command = [part.strip("[],") for part in command]
    if debug:
        print("Command set:" + str(command))

    subprocess.run(command)


def direct_connection():
    enter_ip = input("Enter IP: ")
    enter_port = input("Enter port (Default 22): ")
    enter_user = input("Enter username (Default root): ")

    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", enter_ip):
        print("Invalid IP address format")
        return
    if enter_port and not enter_port.isdigit():
        print("Invalid port number")
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
        print("Command set:" + str(command))

    subprocess.run(command)


def add_connection():
    enter_ip = input("Enter IP: ")
    enter_port = input("Enter port (Default 22): ")
    enter_user = input("Enter username (Default root): ")
    enter_name = input("Enter name of connection: ")

    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", enter_ip):
        print("Invalid IP address format")
        return
    if enter_port and not enter_port.isdigit():
        print("Invalid port number")
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
        print("Command set:" + str(command))

    command_name = enter_name + ".ssh"

    with open(command_name, 'w') as file:
        file.write(str(command))

    subprocess.run(command)


def delete_conection():
    enter_name = input("Enter name of connection: ")
    try:
        os.remove(enter_name + ".ssh")
    except FileNotFoundError:
        print("File not found")
        return


def check_version():
    def read(url):
        try:
            with urllib.request.urlopen(url) as response:
                html_content = response.read().decode('utf-8')
                text = re.sub('<[^<]+?>', '', html_content)

                return text
        except Exception as e:
            print(f"Error: {e}")
            return None

    url_version = 'https://raw.githubusercontent.com/KralicekGamerCz/PySSH/main/version'
    text_web = read(url_version)

    if text_web != version:
        print("Old version: " + version)
        print("Newest version: " + text_web)
        cmd_update = input("Do you want do update? [y/n] ")
        if cmd_update == "y":
            webbrowser.open("https://github.com/KralicekGamerCz/PySSH")
            messagebox.showinfo("Updater", "Download lasted relese on this website please.")
            exit()

        elif cmd_update == "n":
            print()
        else:
            print("Error")

    else:
        print("Stable version: " + version)


running_core = True


while running_core:
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
2. Direct connection
3. Add connection
4. Delete conection
8. Check version
9. Exit
    """)
    cmd = input(">>> ")

    if cmd == "1":
        open_connection()

    elif cmd == "2":
        direct_connection()

    elif cmd == "3":
        add_connection()

    elif cmd == "4":
        delete_conection()

    elif cmd == "8":
        check_version()

    elif cmd == "9":
        running_core = False

    elif cmd == "exit":
        running_core = False

    else:
        print(red + "Invalid operation" + reset)
