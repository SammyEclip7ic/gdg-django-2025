prices = [120, 45, 300, 85, 150]
new_prices = []

def get_expensive_products(prices):
    for price in prices:
        if price > 100:
            new_prices.append(price)
    
    print(new_prices)


if __name__ == "__main__":
    get_expensive_products(prices)
