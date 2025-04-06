import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


def check_aplaybox():
    # Get the cookie from environment variables
    cookie = os.getenv("APLAYBOX_COOKIE")
    if not cookie:
        raise ValueError("APLAYBOX_COOKIE environment variable is not set.")

    # Set up undetected ChromeDriver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = uc.Chrome(options=options, version_main=133)
    try:
        # Navigate to the target URL
        driver.get("https://www.aplaybox.com/details/model/xfyv7yIWHaxH")

        # Add the cookie to the browser
        cookie_parts = cookie.split(";")
        for part in cookie_parts:
            name, value = part.strip().split("=", 1)
            driver.add_cookie({"name": name, "value": value})

        # Refresh the page to apply the cookie
        driver.refresh()

        # Perform a check (e.g., verify page title or specific element)
        print("Page title:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    check_aplaybox()