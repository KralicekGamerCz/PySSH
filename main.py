# PySSH
# Version 1.0.0
# ©2024 by KralicekGamer

import subprocess
import re

version = "1.0.0"

print("PythonSSH " + version)
print("""
1. Save IP
2. Load IP
3. Exit""")


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

    command = f"ssh {enter_user}@{enter_ip} -p {enter_port}"
    command_name = enter_name + ".bat"

    with open(command_name, 'w') as file:
        file.write(command)

    subprocess.run(enter_name + ".bat")


def load_ssh_connection():
    load_name = input("Name of connection: ")
    try:
        subprocess.run(load_name + ".bat")
    except FileNotFoundError:
        print("Invalid name of conection")


running_core = True


while running_core:
    first = input(">>> ")

    if first == "1":
        save_ssh_connection()

    elif first == "2":
        load_ssh_connection()

    elif first == "3":
        running_core = False

    else:
        print("Invalid operation")
