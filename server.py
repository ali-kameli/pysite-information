import builtwith
import sys
import os
from colorama import Fore, init
init()

if len(sys.argv) == 2:
    os.system('cls' or 'clear')
    print(f'{Fore.BLUE} Site Information:\n{Fore.RESET}')
    site = sys.argv[1]
    result = builtwith.builtwith(site)

    for num in result:
        print(f"{Fore.GREEN}[+] {num}:   {result[num]}{Fore.RESET}")
else:
    print(f'{Fore.RED}Invalid Argument !{Fore.RESET}')
