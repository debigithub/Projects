import requests, bs4, re, time

pagedata = requests.get("https://www.bbc.co.uk/")
cleanpagedata = bs4.BeautifulSoup(pagedata.text, 'html.parser')

#data = json.load(urllib2.urlopen('https://www.bbc.co.uk'))

for p in cleanpagedata.select('section'):
    print(p.text+'\n')


#print(str(cleanpagedata))