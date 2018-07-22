from app.app.main import app
from flask import jsonify

client = app.test_client()

test_order = """{
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
}"""



def test_rules():
    response = client.get('/pricing/rules')

    assert response.status_code == 200
    assert response.data


def test_quote():
    response = client.post('pricing/quote', data=test_order, headers={'content-type':'application/json'})

    assert response.status_code == 200
    assert response.data == b'{"Total Price": 2218, "Total VAT": 119, "Items": [{"product_id": 1, "quantity": 1, "unit price": 599, "vat pct": 0.2}, {"product_id": 2, "quantity": 5, "unit price": 250, "vat pct": 0}, {"product_id": 3, "quantity": 1, "unit price": 250, "vat pct": 0}]}\n'
