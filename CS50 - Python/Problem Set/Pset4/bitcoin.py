import sys
import requests

# API key and URL configuration for CoinCap
api_key = "ca12e9fcfda5ceb55017429f2b9551be916f440a6e7557eb1b9d24330369fe94"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

try:
    # Send a GET request to the CoinCap API
    response = requests.get(url)
    
    # Parse the JSON response from the API
    data = response.json()
    
    # Extract the current Bitcoin price in USD and convert it to a float
    bitcoin_price = float(data["data"]["priceUsd"])


    # Check if the user forgot to provide a command-line argument
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")

    # Check if the provided argument is alphabetic
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")

    # If an argument is provided and not strictly alphabetical, calculate the value
    else:
        # Convert the command-line argument to a float
        coin = float(sys.argv[1])
        
        # Calculate the total value of the specified amount of Bitcoin
        result = bitcoin_price * coin
        
        # Print the final result formatted as currency with 4 decimal places
        print(f"${result:,.4f}")



except requests.RequestException:
    # Quietly ignore any network or request-related errors
    pass