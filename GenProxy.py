import json
import argparse
import requests

banner = """
 _____         _____                 
|   __|___ ___|  _  |___ ___ _ _ _ _ 
|  |  | -_|   |   __|  _| . |_'_| | |
|_____|___|_|_|__|  |_| |___|_,_|_  |
                                |___|
"""

print(banner)
parser = argparse.ArgumentParser(description='GenProxy - Yet another tool to generate free random proxies')
parser.add_argument('-t', '--type', type=str, choices=['HTTP', 'HTTPS', 'SOCKS4', 'SOCKS5'], default='HTTP', help='Type of proxy')
parser.add_argument('-c', '--country', type=str, help='Country code for proxy')
parser.add_argument('-n', '--number', type=int, default=5, help='Number of proxies to generate max[100]')
parser.add_argument('-o', '--output', type=str, help='Output file to save proxies')
parser.add_argument('-tr', '--tier', type=str, choices=['random', 'tier1', 'tier2'], default='random', help='Tier for proxy')
args = parser.parse_args()

if not args.country:
    parser.print_help()
    exit()

urls = {
"random": "https://proxypage1.p.rapidapi.com/v1/tier1random",
"tier1": "https://proxypage1.p.rapidapi.com/v1/tier1",
"tier2": "https://proxypage1.p.rapidapi.com/v1/tier2"
}

headers = {
"Content-Type": "application/x-www-form-urlencoded",
"X-RapidAPI-Key": "3398693b48msh311dd6a4dbdd27bp19903ajsn7fcf6c888dda",
"X-RapidAPI-Host": "proxypage1.p.rapidapi.com"
}

proxies = []

print("Generating proxies...")
for i in range(args.number):
    querystring = {"type": args.type, "country": args.country}
    response = requests.request("GET", urls[args.tier], headers=headers, params=querystring)
    data = json.loads(response.text)
    proxies.append(data[0]["ip"] + ":" + str(data[0]["port"]))

if args.output:
    with open(args.output, "w") as file:
        for proxy in proxies:
            file.write(proxy + "\n")
    print("Proxies written to " + args.output)
else:
    for proxy in proxies:
        print(proxy)
