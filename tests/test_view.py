def test_view_home(client):
    assert client.get('/').status_code == 200

def test_view_login(client):
    assert client.get('/login').status_code == 200

def test_view_signup(client):
    assert client.get('/signup').status_code == 200



