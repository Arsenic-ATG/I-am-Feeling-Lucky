#! Python4
# lucky.py - searches google and open top results in new tabs

import webbrowser,bs4,sys

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# TODO: Retrieve top search result links.
# 
# TODO: Open a browser tab for each result