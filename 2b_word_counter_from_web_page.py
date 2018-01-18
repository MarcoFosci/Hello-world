import requests
from bs4 import BeautifulSoup
from IPython.display import HTML, display

WIKI_URL = 'https://ia601405.us.archive.org/18/items/alicesadventures19033gut/19033.txt'
req = requests.get(WIKI_URL)
soup = BeautifulSoup(req.text, 'html5lib')
file = soup.get_text()
testo = ''.join([x for x in file if x in string.ascii_letters + ' ' + '-' ])
word_counts = {}


parole = testo.strip().split(' ')

for value in parole:
    key = value.translate(str.maketrans('','',string.punctuation)).lower()
    print(key)
    if key in word_counts.keys():
        word_counts[key] += 1
    else:
        word_counts[key] = 1

print(word_counts)  
