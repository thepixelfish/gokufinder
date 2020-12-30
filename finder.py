import requests
import bs4
import re
import cgitb
cgitb.enable()

val = input("Enter the link you'd like to use: ")

stuff = requests.get(val)

searched_word = 'volume'
searched_word2 = 'Volume'

soup = bs4.BeautifulSoup(stuff.content)
results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
results2 = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word2)), recursive=True)

print ('Found the word "{0}" {1} times\n'.format(searched_word, len(results + results2)))

