import requests

def fetch_prices():
    print("Fetching cryptocurrency prices (demo)...")
    prices = {"Bitcoin": 30000, "Ethereum": 2000}
    for coin, price in prices.items():
        print(f"{coin}: ${price}")

if __name__ == "__main__":
    fetch_prices()
