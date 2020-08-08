# lucky.py - searches google and open top results in new tabs

import webbrowser,bs4,sys,requests

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"html.parser")

# Open a browser tab for each result
link = soup.select('.LC20lb DKV0Md a')

#print(link)
no_of_tabs = min(5,len(link))

for i in range(no_of_tabs):
	webbrowser.open("https://www.google.com" + link[i].get('href'))