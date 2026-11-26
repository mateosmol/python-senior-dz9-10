import requests
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

res_parse_list = []
for page in range(1, 51):
    print("\033[1A\033[2K", end="", flush=True)
    print(Fore.CYAN + Style.BRIGHT + f"reading page {page}, please wait...")
    response = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    response_parse = response.text.split("<h3>")
    for parse_elem1 in response_parse:
        parse_elem2 = parse_elem1.split('"')
        for i in range(len(parse_elem2)):
            if parse_elem2[i] == " title=":
                res_parse_list.append(parse_elem2[i + 1])

for i in res_parse_list:
    print(i)
