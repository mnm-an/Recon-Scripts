import requests
import json

domain = input("Enter a domain > ")
apikey = "Enter your apikey"

url = 'https://www.virustotal.com/vtapi/v2/domain/report'
params = {'apikey':apikey,'domain':domain}
try:
    response = requests.get(url, params=params)
    jdata = response.json()
    domains = sorted(jdata['subdomains'])
except(KeyError):
    print("No domains found for %s" % domain)
    exit(0)
except(requests.ConnectionError):
    print("Could not connect to www.virtustotal.com", file=sys.stderr)
    exit(1)

for domain in domains:
    f = open("domains.txt", "a")
    f.write(domain+"\n")

f.close()
