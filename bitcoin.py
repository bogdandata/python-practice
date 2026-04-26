import requests
import sys

API_KEY = "0280dcd144ffef501b33f9c0afd141271844434c3f56fdccf70a4f99199cb63b"

def main():
    if len(sys.argv) != 2:
        print("Usage: bitcoin.py <amount>")
        sys.exit(1)
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Invalid amount")
        sys.exit(1)
    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
        response.raise_for_status()
        data = response.json()
        price = float(data["data"]["priceUsd"])
        print(f"${price * n:,.4f}")
    except requests.RequestException:
    
        print("Error fetching data")
        sys.exit(1)
    except KeyError:
        print("Invalid date")
        sys.exit(1)

if __name__ == "__main__":
    main()