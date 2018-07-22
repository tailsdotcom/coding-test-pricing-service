from app.app.core.pricing import get_price_rules
from app.app.core.order_pricer import price_order


def test_price_rules():
    rules, bands = get_price_rules()

    assert len(rules) == 5
    assert len(bands) == 2


def test_order_pricer():
    rules = get_price_rules()
    order = {
        "order": {
            "id": 12345,
            "customer": {
                "name": "John",
                "customer_id": 1
            },
            "items": [
                {
                    "product_id": 1,
                    "quantity": 1
                },
                {
                    "product_id": 2,
                    "quantity": 5
                },
                {
                    "product_id": 3,
                    "quantity": 1
                }
            ]
        }
    }

    actual = price_order(order, rules)

    expected = {
        "Total Price": 2218,
        "Total VAT": 119,
        "Items": [
            {"product_id": 1, "quantity": 1, "unit price": 599, "vat pct": 0.2},
            {"product_id": 2, "quantity": 5, "unit price": 250, "vat pct": 0},
            {"product_id": 3, "quantity": 1, "unit price": 250, "vat pct": 0}
        ]
    }

    assert actual == expected
