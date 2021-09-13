import requests
from bs4 import BeautifulSoup as BS

f = open("subs.txt")
content = f.read()
directory = input("Enter a directory > ")
subdomains = content.splitlines()
discovered_subdomains = []
name = input("Enter The output name >")

for subdomain in subdomains:
    url  =f"http://{subdomain}{directory}"
    try:
        hdict = {"User-agent":"Googlebot"}
        resp = requests.get(url)
        text = resp.text
        soup = BS(text,'html.parser')
        target = soup.find("a",class_="btn btn-primary pull-right btn-lg")
        scode = resp.status_code
        message = resp.url
    except requests.ConnectionError:
        pass
    else:
        with open(name,'a') as file:
            if scode == "302":
                print("[+] Discovred Directory:", url," > ",scode,"\n",resp.headers['Location']," > ",message)
                if url == resp.url :
                    file.write('{0} {1} {2} {3}\n'.format(url, scode, resp.headers['Location'], message))
                    discovered_subdomains.append(url)
            elif scode == "301":
                print("[+] Discovred Directory:", url," > ",scode,"\n",resp.headers['Location']," > ",message)
                if url == resp.url :
                    file.write('{0} {1} {2} {3}\n'.format(url, scode, resp.headers['Location'], message))
                    discovered_subdomains.append(url)
            elif scode == "404":
                pass
            elif scode == "400":
                pass
            elif scode == "403":
                pass
            else:
                print("[+] Discovred Directory:", url," > ",scode," > ",message)
                if url == resp.url:
                    file.write('{0} {1} {2}\n'.format(url, scode, message))     
                    discovered_subdomains.append(url)
                    
            
        
