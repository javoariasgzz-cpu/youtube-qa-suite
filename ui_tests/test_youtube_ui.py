import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ui_tests.youtube_page import YouTubePage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    d = webdriver.Chrome(service=service, options=options)
    d.implicitly_wait(10)
    yield d
    d.quit()

def test_youtube_opens(driver):
    page = YouTubePage(driver)
    page.open()
    assert "YouTube" in driver.title

def test_search_returns_results(driver):
    page = YouTubePage(driver)
    page.open()
    page.search("python selenium tutorial")
    results = page.get_results()
    assert len(results) > 0

def test_first_result_has_title(driver):
    page = YouTubePage(driver)
    page.open()
    page.search("QA automation")
    title = page.get_first_result_title()
    assert title is not None
    assert len(title) > 0

def test_click_opens_video(driver):
    page = YouTubePage(driver)
    page.open()
    page.search("python testing")
    page.click_first_result()
    assert "watch" in driver.current_url

def test_video_player_loads(driver):
    page = YouTubePage(driver)
    page.open()
    page.search("selenium webdriver tutorial")
    page.click_first_result()
    assert page.is_video_player_loaded()
