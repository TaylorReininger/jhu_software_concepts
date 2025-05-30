from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import urlopen
import json




# Test scraping anything from the web


url = "https://www.thegradcafe.com/result/"
entry_num = '986062'


page = urlopen(url+entry_num)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")


print(soup.title.string)


department_html = soup.find_all('dt')

print(department_html)

department = [i.get_text() for i in department_html]
print(department)




department_html = soup.find_all('dd')

print(department_html)

department = [i.get_text() for i in department_html]
print(department)







