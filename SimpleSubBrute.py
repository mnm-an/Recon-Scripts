import requests
from tqdm import tqdm , trange
import time

f = open("subs.txt")
name = input("Name of file > ")
content = f.read()
subdomains = content.splitlines()
domain = input("Enter the domain > ")
discovered_subdomains = []
x = len(subdomains)

for subdomain in subdomains:
        url  =f"http://{subdomain}.{domain}"
        try:
            hdict = {"User-agent":"Googlebot"}
            resp = requests.get(url, headers=hdict)
            scode = resp.status_code
        except requests.ConnectionError:
            pass
        else:
            with open(name,'a') as file:
                if scode == "302":
                    print("[+] Discovred subdomain:", url," > ",scode,"\n",resp.headers['Location'])
                    discovered_subdomains.append(url)
                    file.write('{0} {1} {2} {3}\n'.format(url, scode, resp.headers['Location']))
                elif scode == "301":
                    print("[+] Discovred subdomain:", url," > ",scode,"\n",resp.headers['Location'])
                    file.write('{0} {1} {2} {3}\n'.format(url, scode, resp.headers['Location']))
                elif scode == "404":
                    print("[+] Discovred subdomain:", url," > ",scode)
                elif scode == "400":
                    print("[+] Discovred subdomain:", url," > ",scode)
                else:
                    print("[+] Discovred subdomain:", url," > ",scode)
                    discovered_subdomains.append(url)
                    file.write('{0} {1} \n'.format(url, scode))   
            
                    
            
        
