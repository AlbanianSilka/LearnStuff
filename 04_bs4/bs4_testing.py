import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
search = input("Search:")
google_url = f"https://www.google.com/search?q=" + search
response = requests.get(google_url, {"User-Agent": ua.random})
soup = BeautifulSoup(response.text, "html.parser")

result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})

links = []
titles = []
for r in result_div:
    try:
        link = r.find('a', href=True)
        title = r.find('div', attrs={'class': 'vvjwJb'}).get_text()

        if title != '':
            titles.append(title)
        link_href = link.get('href')
        if "url?q=" in link_href:
            printed_link = (link.get('href').split("?q=")[1].split("&sa=U")[0])
            print(title)
            print(printed_link)
    except:
        continue
