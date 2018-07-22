from app.app.core.pricing import get_price_rules


def test_price_rules():
    rules, bands = get_price_rules()

    assert len(rules) == 5
    assert len(bands) == 2
