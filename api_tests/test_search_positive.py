import pytest
import requests
from utils.config import API_KEY, BASE_URL

def test_search_returns_200():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "python testing", "maxResults": 5, "key": API_KEY}
    response = requests.get(url, params=params)
    assert response.status_code == 200

def test_search_returns_items():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "selenium", "maxResults": 3, "key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0

def test_search_result_has_title():
    url = f"{BASE_URL}/search"
    params = {"part": "snippet", "q": "QA automation", "maxResults": 1, "key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    assert "title" in data["items"][0]["snippet"]

def test_video_details_returns_200():
    url = f"{BASE_URL}/videos"
    params = {"part": "snippet", "id": "dQw4w9WgXcQ", "key": API_KEY}
    response = requests.get(url, params=params)
    assert response.status_code == 200

def test_video_details_has_channel():
    url = f"{BASE_URL}/videos"
    params = {"part": "snippet", "id": "dQw4w9WgXcQ", "key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    assert "channelTitle" in data["items"][0]["snippet"]
