from app.app.main import app


def test_demo():
    client = app.test_client()
    response = client.get('/pricing/rules')
    result = response.data
    print(result)
    assert result
