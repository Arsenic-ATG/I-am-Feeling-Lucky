# lucky.py - searches google and open top results in new tabs

import webbrowser,bs4,sys,requests

# Get the address from the user
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'lxml')

# Open a browser tab for each result
link = soup.select('div#main > div > div > div > a')
no_of_tabs = min(5,len(link))

for i in range(no_of_tabs):
	webbrowser.open("https://www.google.com" + link[i].get('href'))

