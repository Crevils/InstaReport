'''
Don't forget to give credits : D
Author : https://github.com/crevils
Original Repositary : https://github.com/crevils/InstaReport
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loading_screen import show_loading_screen

def report_accounts(username, accounts_file):
    options = Options()
    options.add_argument("--disable-notifications")  # Disable notifications

    # Read account credentials from file
    with open(accounts_file, "r") as file:
        accounts = [line.strip().split(":") for line in file]

    # Initialize WebDriver
    try:
        driver = webdriver.Chrome(options=options)
    except WebDriverException as e:
        print("Error: WebDriver initialization failed.")
        print(e)
        return

    # Check if the WebDriver instance is valid
    if not hasattr(driver, 'find_element'):
        print("Error: WebDriver instance is not valid.")
        return

    # Iterate through accounts
    for account in accounts:
        try:
            # Log in
            driver.get("https://www.instagram.com/accounts/login/")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
            driver.find_element("name", "username").send_keys(account[0])
            driver.find_element("name", "password").send_keys(account[1])
            
            # Find the submit button using XPath
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            show_loading_screen(10)

            # Visit target user's page
            driver.get("https://www.instagram.com/{}/".format(username))
            show_loading_screen(10)
            # Report user
            option_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//svg[@aria-label='Options']")))
            option_button.click()
            show_loading_screen(10)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Report']")))
            show_loading_screen(3)

            report_button = driver.find_element(By.XPATH, "//button[text()='Report']")
            report_button.click()
            show_loading_screen(7)
            driver.find_element(By.XPATH, "//button[text()='Report']").click()
            show_loading_screen(5)
            driver.find_element(By.XPATH, "//button[text()='It's spam']").click()
            show_loading_screen(3)

            # Close report modal
            driver.find_element(By.XPATH, "//button[text()='Close']").click()
            show_loading_screen(3)

            # Log out
            driver.find_element(By.XPATH, "//span[text()='Log Out']").click()
            show_loading_screen(3)

            driver.find_element(By.XPATH, "//button[text()='Log Out']").click()
            show_loading_screen(3)

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error occurred while processing account {account[0]}")
            print(f"Message: {e}")
            continue

    driver.quit()
