# PySSH
# Version 1.0.0
# (C)2024 by KralicekGamer

import subprocess
import re
import shlex
import os

version = "1.0.1"


def connection():
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

    subprocess.run(command)


def save_ssh_connection():
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

    command_name = enter_name + ".ssh"

    with open(command_name, 'w') as file:
        file.write(str(command))

    subprocess.run(command)


def load_ssh_connection():
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

    subprocess.run(command)


running_core = True


while running_core:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("PythonSSH " + version)
    print("""
    1. Connect IP
    2. Load IP
    3. Save IP
    4. Exit
    """)
    first = input(">>> ")

    if first == "1":
        connection()

    elif first == "2":
        load_ssh_connection()

    elif first == "3":
        save_ssh_connection()

    elif first == "4":
        running_core = False

    else:
        print("Invalid operation")
