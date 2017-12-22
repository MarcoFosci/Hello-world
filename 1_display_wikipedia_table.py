import requests
from bs4 import BeautifulSoup
from IPython.display import HTML, display

WIKI_URL = 'https://en.wikipedia.org/wiki/List_of_ongoing_armed_conflicts'
req = requests.get(WIKI_URL)
soup = BeautifulSoup(req.text, 'html5lib')

# Wikipedia use two CSS selectors for larger tables – sortable and plainrowheaders
table_classes = {'class': ['sortable', 'plainrowheaders']} 
table = soup.find_all('table', table_classes)

# I want to display the first table of the web page then I use table[0]
display(HTML(str(table[0]))) 
