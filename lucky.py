# lucky.py - searches google and open top results in new tabs

import webbrowser,bs4,sys,requests

#res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
res = requests.get('https://google.com/search?q=google')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,'lxml')
# print(soup)
# Open a browser tab for each result
#link = soup.select('.r a')
link = soup.select('div#main > div > div > div > a')
print(link)
no_of_tabs = min(5,len(link))

for i in range(no_of_tabs):
	webbrowser.open("https://www.google.com" + link[i].get('href'))

