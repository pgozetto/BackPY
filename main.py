# Dependencies
from datetime import date
from shutil import copyfile, copytree
from time import sleep as wait
from colorama import Fore

# Variables
bk_date = str(date.today()) # Date of the backup (YYYY-MM-DD)

# Functions
def IsFile():
    path_input: str = str(input(" > Input PATH: "))
    file_name: str = str(input(" > Input File name & format: "))
    file_total: str = path_input + "\\" + file_name
    path_output: str = str(input(" > Output PATH: ")) + "\\" + bk_date + file_name
    print(path_output)
    copyfile(file_total, path_output)
def IsDirectory():
    path_input: str = str(input(" > Input PATH: "))
    file_name: str = str(input(" > Input directory (new) name: "))
    path_output: str = str(input(" > Output PATH: ")) + "\\" + bk_date + file_name
    print(path_output)
    copytree(path_input, path_output)
def CustomText(string: str):
    wait(0.5)
    size: int = len(string) + 4
    print(Fore.MAGENTA + "-"*size + Fore.RESET)
    print(Fore.YELLOW + f"  {string}" + Fore.RESET)
    print(Fore.MAGENTA + "-"*size + Fore.RESET)

# Isolate GUI Function
def GUI(optionslist:list):
    """
    :param optionslist: A String List to show in the menu
    :varia select: The User's Choice
    :return: None

    OBS: TO CHANGE THE OPTIONS IN CODE, YOU NEED TO CHANGE THE "else" function
    """
    while True:
        for indice, options in enumerate(optionslist):
            print(f"{indice} - {options}")
        print(Fore.BLUE + "Made by: @pgozetto [Pedro Gozetto]" + Fore.RESET)
        wait(0.25)
        try:
            select = int(input(("\n CHOOSE A OPTION: ")))
        except:
            print(Fore.RED + " Error<You MUST use Int values, please, try again>" + Fore.RESET)
        else:
            if select > 3:
                print(Fore.RED + " Error<You MUST input the possible options, please, try again>" + Fore.RESET)
            if select == 3:
                print(Fore.RED + " THX For Using the App, Bye" + Fore.RESET)
                break
            if select == 0:
                IsFile()
            if select == 1:
                IsDirectory()
            if select == 2:
                print(Fore.BLUE + "Made by: @pgozetto [Pedro Gozetto]" + Fore.RESET)
                print(Fore.BLUE + "GitHub: https://github.com/pgozetto" + Fore.RESET)
                print(Fore.BLUE + "Instagram: https://www.instagram.com/pedrogozetto/" + Fore.RESET)
                print(Fore.BLUE + "X/Twitter: https://x.com/PedroGozetto" + Fore.RESET)

                
def __main__():
    CustomText("BackPython")
    GUI(["BackUp a File", "BackUp a Directory", "See Info","Exit The Application"])

if __name__ == "__main__":
    __main__()

