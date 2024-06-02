#!/usr/bin/env python3

import os
import sys
import argparse
import subprocess
import threading

machine_name = ""
difficulty = ""
os_name = ""
platform = ""
path_to_folder=""

def create_folder(path):
    global path_to_folder
    try:
        expanded_path = os.path.expanduser(path)
        os.makedirs(expanded_path, exist_ok=True) 
        print(f"Directory '{path}' created successfully")
        path_to_folder = path
    except OSError as error:
        print(f"Error creating directory '{path}': {error}")


def pars():
    global machine_name, difficulty, os_name, platform
    parser = argparse.ArgumentParser()

    parser.add_argument('-n',type=str,help='set name of machine')
    parser.add_argument('-d',type=str,help='set difficulty')
    parser.add_argument('-os',type=str,help='set OS')
    parser.add_argument('-platform',type=str,help='set platform (HTB or THM)')

    args=parser.parse_args()

    machine_name = (args.n if args.n else "").strip("\n")
    difficulty = (args.d if args.d else "").strip("\n")
    os_name = (args.os if args.os else "").strip("\n")
    platform = (args.platform if args.platform else "HTB").strip("\n")

def fill_folder():
    global machine_name,difficulty,os_name,platform,path_to_folder

    #outputNMAP.txt
    expanded_path = os.path.expanduser(path_to_folder)
    file_path = os.path.join(expanded_path, "outputNMAP.txt")
    try:
        with open(file_path,'w') as file:
            file.write("")
    except OSError as error:
        print(f"Error creating file '{file_path}': {error}")

    #WriteUp.md
    file_path = os.path.join(expanded_path, "WriteUp.md")
    try:
        with open(file_path,'w') as file:
            file.write(f"""# {platform} {machine_name}
## Difficulty: {difficulty}
## OS: {os_name}

## Enumeration:

## Foothold:

## We got the user flag!

## Privilege Escalation:

## We got the root flag!
""")
            print("Files created successfully")
    except OSError as error:
        print(f"Error creating file '{file_path}': {error}")

def move_to_dir():
    global path_to_folder
    os.system(f"ls {path_to_folder}")

pars()
#print(machine_name)
#print(platform)
create_folder(f"~/Documents/{platform}/{machine_name}")
fill_folder()

move_to_dir()