from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def perform_smoke_test():
    # Specify the path to your ChromeDriver executable
    driver_path = '/path/to/chromedriver'
    
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Navigate to the login page
        driver.get('https://example.com/login')

        # Locate the username and password input fields and the login button
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

        # Enter valid credentials
        username_input.send_keys('your_username')
        password_input.send_keys('your_password')

        # Click the login button
        login_button.click()

        # Verify if the login was successful by checking for elements on the post-login page
        assert driver.find_element(By.XPATH, '//h1[text()="Welcome"]')

        print("Smoke test passed: Login functionality is working correctly!")

    except Exception as e:
        print(f"Smoke test failed: {str(e)}")

    finally:
        # Close the browser window
        driver.quit()