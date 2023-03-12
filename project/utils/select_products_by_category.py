def select_products_by_category(products: list, category: str) -> list:
    filtered_products: list = []
    for product in products:
        if product.category == category:
            filtered_products.append(product)
    return filtered_products
