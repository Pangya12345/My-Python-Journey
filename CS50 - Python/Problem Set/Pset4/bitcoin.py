import requests
import sys 

try:
    response = requests.get("https://pro.coincap.io/dashboard")
    response.raise_for_status()
    final = response.json()
    print(final)

except requests.RequestException:
    print("Not Working")

