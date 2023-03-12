def extract_prices(products):
    prices = []
    for product in products:
        prices.append(product.price)
    return prices
