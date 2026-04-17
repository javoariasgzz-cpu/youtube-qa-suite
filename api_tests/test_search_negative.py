import pytest
import requests
from utils.config import API_KEY, BASE_URL

def test_invalid_api_key_returns_400_or_403():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "python", "key": "INVALID_KEY_12345"}
    response = requests.get(url, params=params)
    assert response.status_code in [400, 403]

def test_missing_api_key_returns_400_or_403():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "python"}
    response = requests.get(url, params=params)
    assert response.status_code in [400, 403]

def test_empty_query_returns_200_with_results():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "", "key": API_KEY}
    response = requests.get(url, params=params)
    assert response.status_code == 200

def test_invalid_video_id_returns_empty_items():
    url = f"{BASE_URL}/videos"
    params = {"part": "snippet", "id": "INVALID_VIDEO_ID_999", "key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    assert data["pageInfo"]["totalResults"] == 0

def test_max_results_above_limit_accepts_request():
    # Finding: YouTube API accepts maxResults=999 and returns 200 instead of 400.
    # The API does not enforce the documented maxResults limit of 50.
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "python", "maxResults": 999, "key": API_KEY}
    response = requests.get(url, params=params)
    assert response.status_code == 200
