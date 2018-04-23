import requests as req 
from bs4 import BeautifulSoup
r = req.get("http://" + 'www.amrita.edu')
data = r.text
soup = BeautifulSoup(data)
#Using the find_all method, gives us a whole list of elements with the tag "a".
for link in soup.find_all('a'):
 print(link.get('href'))