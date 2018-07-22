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
    result = response.data

    assert result


def test_quote():
    response = client.post('pricing/quote', data=test_order, headers={'content-type':'application/json'})

    assert response.data == b'"hello world"\n'
