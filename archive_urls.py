import requests as req
c = input('Enter the host > ')
url = "http://web.archive.org/cdx/search/cdx?url="+c+"*&output=txt"
a = req.get(url)
b = a.text
f = open("Urls.txt", "a")
f.write(b)
f.close()
