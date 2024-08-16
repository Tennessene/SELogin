from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def visit_url(url, sleep_time):
    """
    Navigates to a given url.

    Args:
        url (str): The url of the site to visit (e.g., 'https://stackexchange.com/').
        sleep_time (int): The time in seconds to sleep before moving on.
    """
    print(f'Visiting {url}')
    driver.get(url)
    time.sleep(sleep_time) # Wait for the page to load

def visit_site(name):
    """
    Navigates to a given site.

    Args:
        name (str): The name of the site to visit (e.g., 'superuser').
    """
    url = f'https://{name}.com/'
    visit_url(url, 2)

    # Visit meta site
    if ".stackexchange" in name:
        namearray = name.split('.')
        basename = namearray[0]
        url = f'https://{basename}.meta.stackexchange.com/'
    else:
        url = f'https://meta.{name}.com/'

    visit_url(url, 2)


def login_stackexchange():

    # Logs into Stack Exchange using the provided credentials.

    name = 'stackexchange'
    url = f'https://{name}.com/users/login'
    visit_url(url, 0)

    wait = WebDriverWait(driver, 10)

    email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    password = wait.until(EC.element_to_be_clickable((By.ID, "password")))

    # Enter your credentials
    email.send_keys('${{ secrets.EMAIL }}')
    password.send_keys('${{ secrets.PASSWORD }}')
    password.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for login to complete

    # Visit meta site
    url = f'https://meta.{name}.com/'
    visit_url(url, 2)


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
        # Log in to Stack Exchange
        login_stackexchange()

        # Visit other sites
        sites = [
            'stackoverflow', 'superuser', 'serverfault', 'gaming.stackexchange', 'gamedev.stackexchange',
            'apple.stackexchange', 'security.stackexchange', 'askubuntu',
            'english.stackexchange', 'unix.stackexchange', 'raspberrypi.stackexchange',
            'diy.stackexchange', 'photo.stackexchange'
        ]

        for site in sites:
            visit_site(site)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the browser
        driver.quit()
