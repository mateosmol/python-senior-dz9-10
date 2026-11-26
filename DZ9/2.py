import requests
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

res_parse_list = []
for page in range(1, 51):
    print("\033[1A\033[2K", end="", flush=True)
    print(Fore.CYAN + Style.BRIGHT + f"reading page {page}, please wait...")
    response = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html')
    response_parse = response.text.split('<p class="price_color">')
    for parse_elem1 in response_parse[1:]:
        parse_elem2 = parse_elem1.split("</p>")
        res_parse_list.append(parse_elem2[0])

for i in res_parse_list:
    print(i[1:-1])
