import requests
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

books_list = []
print(Fore.RED + Style.BRIGHT + "It would be too long to process all pages.")
page = int(input("Enter the page number of books, information of which you want to see: "))
print(Fore.CYAN + Style.BRIGHT + f"reading page {page}, please wait...")

response = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
response.raise_for_status()
response_parse = response.text.split("<h3>")
book_links = []
for parse_elem1 in response_parse:
    parse_elem2 = parse_elem1.split('"')
    for i in range(len(parse_elem2)):
        if parse_elem2[i] == " title=":
            book_links.append(parse_elem2[i - 1])
            break
for book_link in book_links:
    book_url = "https://books.toscrape.com/catalogue/" + book_link
    book_response = requests.get(book_url)
    book_response.raise_for_status()
    book_html = book_response.text
    # Назва книги
    title = book_html.split('<h1>')[1].split('</h1>')[0]
    # Ціна
    price = book_html.split('<p class="price_color">')[1].split('</p>')[0]
    # Рейтинг
    rating_part = book_html.split('<p class="star-rating ')[1]
    rating = rating_part.split('"')[0]
    # Інформація з таблиці
    table = book_html.split('<table class="table table-striped">')[1]
    table_rows = table.split('<tr>')
    book_info = {}
    for row in table_rows:
        if '<th>' in row and '<td>' in row:
            key = row.split('<th>')[1].split('</th>')[0]
            value = row.split('<td>')[1].split('</td>')[0]
            book_info[key] = value
    books_list.append({"Title": title, "Price": price, "Rating": rating, **book_info})

print(Fore.YELLOW + Style.BRIGHT + f"\nAll books of page {page}:\n")

for book in books_list:
    print("-" * 50)
    for key, value in book.items():
        print(f"{key}: {value}")