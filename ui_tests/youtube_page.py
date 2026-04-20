from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YouTubePage:
    URL = "https://www.youtube.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_box = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "search_query"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    def get_results(self):
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-video-renderer"))
        )
        return self.driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")

    def get_first_result_title(self):
        results = self.get_results()
        if results:
            title = results[0].find_element(By.CSS_SELECTOR, "#video-title")
            return title.text
        return None

    def click_first_result(self):
        results = self.get_results()
        if results:
            title = results[0].find_element(By.CSS_SELECTOR, "#video-title")
            title.click()

    def is_video_player_loaded(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "video.html5-main-video"))
            )
            return True
        except:
            return False
