from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def visit_site(driver, name):
    """
    Navigates to a given site.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        name (str): The name of the site to visit (e.g., 'superuser').
    """
    url = f'https://{name}.com/'
    driver.get(url)
    time.sleep(2)  # Wait for the page to load


def login_stackoverflow(driver):
    """
    Logs into Stack Overflow using the provided credentials.

    Args:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
    """
    driver.get('https://stackoverflow.com/users/login')

    wait = WebDriverWait(driver, 10)

    email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))

    # Enter your credentials
    email.send_keys('${{ secrets.EMAIL }}')
    password.send_keys('${{ secrets.PASSWORD }}')
    password.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for login to complete


if __name__ == '__main__':
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
#    chrome_options.add_argument("--remote-debugging-port=0")

    # Path to ChromeDriver
    service = Service('chromedriver-linux64/chromedriver')  # Adjust the path as needed

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Log in to Stack Overflow
        login_stackoverflow(driver)

        # Visit other sites
        sites = [
            'superuser', 'serverfault', 'gaming.stackexchange', 'gamedev.stackexchange',
            'apple.stackexchange', 'security.stackexchange', 'askubuntu',
            'english.stackexchange', 'unix.stackexchange', 'raspberrypi.stackexchange',
            'diy.stackexchange', 'photo.stackexchange'
        ]

        for site in sites:
            visit_site(driver, site)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the browser
        driver.quit()
