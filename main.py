from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

def visit_url(url):
    """
    Navigates to a given url.

    Args:
        url (str): The url of the site to visit (e.g., "https://stackexchange.com/").
        sleep_time (int): The time in seconds to sleep before moving on.
    """
    print(f"Visiting {url}")
    driver.get(url)

    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )


def visit_site(name):
    """
    Navigates to a given site.

    Args:
        name (str): The name of the site to visit (e.g., 'superuser').
    """
    url = f"https://{name}.com/users/current"
    visit_url(url)
    accept_cookies()

    # Visit meta site
    if '.stackexchange' in name:
        namearray = name.split('.')
        basename = namearray[0]
        url = f"https://{basename}.meta.stackexchange.com/users/current"
    else:
        url = f"https://meta.{name}.com/users/current"

    visit_url(url)
    accept_cookies()

def accept_cookies():
    isPresent = len(driver.find_elements(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')) > 0
    if isPresent:

        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        )
        print(f"Clicking on accept cookie button: {cookie_button.text}")
        cookie_button.click()
    else:
        print("Cookies have already been accepted or are not availible")


def login_stackexchange():

    # Logs into Stack Exchange using the provided credentials.

    name = 'stackexchange'
    url = f"https://{name}.com/users/login/"
    visit_url(url)

    wait = WebDriverWait(driver, 10)

    email = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
    password = wait.until(EC.element_to_be_clickable((By.ID, 'password')))

    # Enter your credentials
    emailStr = os.getenv('EMAIL')
    passwordStr = os.getenv('PASSWORD')
    email.send_keys(emailStr)
    password.send_keys(passwordStr)
    password.send_keys(Keys.RETURN)

    time.sleep(4) # Wait for login to complete

    accept_cookies()

    url = f"https://{name}.com/users/15915140/anston-sorensen"
    visit_url(url)

    driver.save_screenshot("stackexchange.png")

    # Visit meta site
    url = f"https://meta.{name}.com/users/current"
    visit_url(url)
    accept_cookies()


if __name__ == '__main__':
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")

    # Path to ChromeDriver
    service = Service("chromedriver-linux64/chromedriver")  # Adjust the path as needed

    # Initialize the WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Log in to Stack Exchange
        login_stackexchange()

        # Visit other sites
        sites = os.getenv('SITES')
        sitesf = sites.split(', ')

        for site in sitesf:
            visit_site(site)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the browser
        driver.close()
        driver.quit()
