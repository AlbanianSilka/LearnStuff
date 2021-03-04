import requests
from bs4 import BeautifulSoup
search = input("Search:")
results = 10
page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
soup = BeautifulSoup(page.content, "html5lib")
links = soup.findAll("a")
heading_object=soup.find_all( 'h3' )
for info in heading_object:
    print(info.getText())
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        print (link.get('href').split("?q=")[1].split("&sa=U")[0])