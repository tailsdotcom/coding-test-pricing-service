def price_item(order_item, price_list, vat_band):
    id = order_item['product_id']
    unit_price = price_list[id]['price']
    vat = vat_band[price_list[id]['vat_band']]

    return {
        'product_id': id,
        'quantity': order_item['quantity'],
        'unit price': unit_price,
        'vat pct': vat
    }


def price_order(order, rules):
    """
    - the total price for the order
    - the total VAT for the order
    - price and VAT for each item in the order
    """
    price_list, vat_bands = rules
    total_price = 0
    total_vat = 0
    itemised_price = []
    for i in order['order']['items']:
        p = price_item(i, price_list, vat_bands)
        item_vat = p['unit price'] * p['quantity'] * p['vat pct']
        item_total = p['unit price'] * p['quantity'] * (1 + p['vat pct'])
        total_price += item_total
        total_vat += item_vat
        itemised_price.append(p)

    return {
        'Total Price': int(total_price),
        'Total VAT': int(total_vat),
        'Items': itemised_price
    }
