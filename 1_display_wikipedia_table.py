import requests
from bs4 import BeautifulSoup
from IPython.display import HTML, display

WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts'
req = requests.get(WIKI_URL)
soup = BeautifulSoup(req.text, 'html5lib')
table_classes = {'class': ['sortable', 'plainrowheaders']}
table = soup.find_all('table', table_classes)
display(HTML(str(table[0]))) # table[0] just to take the first table on the webpage 
