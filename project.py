import sys
import googlemaps
from tabulate import tabulate
from time import sleep
import os
import keyboard
import re
from pyfiglet import Figlet

FONT = "big"
figlet = Figlet(font=FONT)
##figlet.setFont()
API_KEY = "AIzaSyBdEAO7YglDr_sKFGR-DHtwcow-2D8IteU"
is_yes = {"yes", "y", "si", "s", "ok"}
is_no = {"no", "n", "none"}

## Main function: Show menu, Prompt the user and show results
def main():
    while True:
        os.system("cls")
        print(f"\nWelcome to\n{figlet.renderText('Place Finder V1.0')}Please choose an option:\n")
        print("   1 - Search places\n   2 - View stored places\n   3 - Erase log\n   4 - Exit\n\nInput option number, then press Enter\n")
        op = input("--> ")
        if op == "1":
            while True:
                add = input("Address? ")
                if add == "exit":
                    sys.exit("\nBye!\n")
                dir, lat_len = format_address(add)
                resp = check_address(dir)
                if resp in is_yes:
                    break
                elif resp in is_no:
                    print("Input more details, like state or country")
                elif resp == "exit":
                    sys.exit("\nBye!\n")
                else:
                    print("Invalid response")
                
            cat = input("Category? ")
            request = map_request(lat_len, cat)
            res_list = results(request)
            print(tabulate(res_list, headers="firstrow", tablefmt="grid"))
            save_result(res_list)
            esc_and_clean()
        elif op == "2":
            save_list = print_log()
            print(tabulate(save_list, headers=["NAME","ADDRESS"], tablefmt="grid"))
            esc_and_clean()
        elif op == "3":
            erase_log()
            wait_and_clean()
        elif op == "4":
            sys.exit("\nBye!\n")
        else:
            print("Invalid option, try again")
            wait_and_clean()


## Format the entered address correctly
def format_address(d):
    try:
        maps = googlemaps.Client(key=API_KEY)
        lat_len = maps.geocode(
            address=d
        )  ##if maps don´t find the address assign an empty list
        complete_direction = maps.reverse_geocode(
            lat_len[0]["geometry"]["location"]
        )
        return complete_direction, lat_len[0]["geometry"]["location"]
    except IndexError:
        return list(), list()

## Verifying if the search was correct
def check_address(dir):
    try:
        print(
            f"Are you asking for: {dir[0]['address_components'][1]['long_name']} {dir[0]['address_components'][0]['long_name']}, {dir[0]['address_components'][2]['long_name']}, {dir[0]['address_components'][3]['long_name']}, {dir[0]['address_components'][6]['long_name']}?"
        )
        resp = input("It is ok? (Yes/No) ").strip().lower()
        return resp
    except IndexError:
        print("Address not found, try again")
        return "no"

## Requesting the google maps API
def map_request(d, c):
    maps = googlemaps.Client(key=API_KEY)
    response = maps.places(query=c, location=d, radius = 1)
    return response["results"]


## Printing the first 5 results
def results(x):
    i = 0
    table = [["N°", "NAME", "ADDRESS", "STARS"]]
    for _ in x:
        if i < 5 and _["rating"] != 0:
            table.append(
                [(i + 1), _["name"], str(_["formatted_address"]), str(_["rating"])]
            )
            i += 1
    return (table)

## If the user want, save a register
def save_result(table): 
    x = 0
    while True:
        try:
            if x == 0:
                r = input("Do you want to save any? (Yes/No)\n--> ").strip().lower()
            elif x == 1:
                r = input("Do you want to save any more? (Yes/No)\n--> ").strip().lower()
            if r in is_yes:
                while True:
                    try:
                        reg_num = input("Which one? Input the number \n--> ")
                        if reg_num.strip().lower() == "exit":
                            sys.exit("\nBye\n")
                        if reg_num == "0":
                            raise IndexError
                        with open("query_log.txt", "a") as file:
                            file.write(f"{table[int(reg_num)][1],table[int(reg_num)][2]}\n")
                            file.close()
                            print("Successfully saved")
                            x = 1
                        break
                    except (ValueError, IndexError):
                        print("\nInvalid number, try again\n")
                        pass
            elif r in is_no:
                break
            elif r.strip().lower() == "exit":
                sys.exit("\nBye!\n")
            else:
                raise ValueError
        except ValueError:
            print('\nInvalid response, use "yes/no"\n')


## Show stored results
def print_log():
    try:
        querys = []
        with open("query_log.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                reg = re.search(r"\'(.+)\'\, \'(.+)\'", line)
                querys.append([reg[1],reg[2]])
        if querys:
            return querys
        else:
            print("The log is empty")
    except FileNotFoundError:
        print("File not found. You must save a register first")


def erase_log():
    r = input("Are you sure?\nYou must enter YES to delete\n--> ")
    if r == "YES":
        file = open("query_log.txt", "w")
        file.close()
        print("Log erased")
    else:
        print("Ok, nothing was removed")


def wait_and_clean():
    sleep(1.25)
    os.system("cls")


def esc_and_clean():
    print("Press Esc to return to the menu")
    keyboard.wait("esc")
    os.system("cls")



if __name__ == "__main__":
    main()
