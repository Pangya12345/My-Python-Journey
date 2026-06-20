import sys
import requests
api_key = "ca12e9fcfda5ceb55017429f2b9551be916f440a6e7557eb1b9d24330369fe94"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
try:
    response = requests.get(url)
    data = response.json()
    
except requests.RequestException:
    print()


