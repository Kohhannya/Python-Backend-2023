def select_products_by_category(products, category):
    filtered_products = []
    for product in products:
        if product.category == category:
            filtered_products.append(product)
    return filtered_products
