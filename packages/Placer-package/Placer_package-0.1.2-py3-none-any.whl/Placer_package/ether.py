# Welcome to ether
# How to use:
# 1 import ether into your python file
# 2 use the ether.log() to insert 
# Done!

from os.path import isfile, dirname
from os import makedirs
from typing import Tuple


log_file = 'logs/ether_log.txt'


def check_existing_log() -> bool:
    return isfile(log_file)


# ----- Functions to create log -----
def init_create_file():
    with open(log_file, "w") as f:
        f.write("[Etherlogs]" + "\n")
        f.write("Current numer of events:" + "\n")
        f.write("0" + "\n")

def init_create_folder():
    try:
        path = dirname(log_file)
        makedirs(path)
    except FileExistsError:
        print("Unable to create etherlog, path already exists")


# ----- Functions to update the header -----
def read_event_number() -> Tuple[list, str]:
    with open(log_file, 'r') as file:
        file_content = file.readlines()

    past_event_number = int(file_content[2])
    new_event_number = str(past_event_number + 1)
    
    return file_content, new_event_number

def update_event_number(file_content: list, event_number: str):
    file_content[2] = event_number + "\n"

    with open(log_file, 'w', encoding='utf-8') as file:
        file.writelines(file_content)


# ----- Functions to add the event -----
def add_event_number(event_number: str):
     with open(log_file, "a") as f:
        f.write("\n\n" + "Event number " + event_number + ":\n")


# ----- Main functions -----
def create_log():
    ether_initiated: bool = check_existing_log()

    if not ether_initiated:
        init_create_folder()
        init_create_file()
    
    file_content, event_number = read_event_number()
    update_event_number(file_content, event_number)
    add_event_number(event_number)


def log(event):
    with open(log_file, "a") as f:
        f.write(str(event) + "\n")

# _0884
