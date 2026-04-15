import requests
from utils.config import API_KEY, BASE_URL

def test_api_connection():
    url = f"{BASE_URL}/search"
    params = {
        "part": "snippet",
        "q": "python testing",
        "maxResults": 1,
        "key": API_KEY
    }
    response = requests.get(url, params=params)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

test_api_connection()
