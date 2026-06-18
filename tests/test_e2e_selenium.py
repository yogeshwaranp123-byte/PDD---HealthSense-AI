import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def run_tests():
    # Target URL can be set via env var, e.g. for Vercel deployment, or fallback to github.io
    target_url = os.environ.get("TARGET_URL", "https://yogeshwaranp123-byte.github.io/PDD-web-application-/")
    print(f"Target URL for Selenium tests: {target_url}")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    # Bypass CORS, Mixed Content, and Private Network Access checks in Chrome
    options.add_argument("--disable-web-security")
    options.add_argument("--allow-running-insecure-content")
    
    # Disable modern SameSite cookie restrictions so we can test secure public frontends with local HTTP backends
    options.add_argument("--disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure,BlockInsecurePrivateNetworkRequests")
    
    # Enable console log capture
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})

    print("Initializing Chrome WebDriver...")
    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"Standard Selenium 4 driver initialization failed: {e}")
        print("Attempting fallback using webdriver-manager...")
        try:
            from webdriver_manager.chrome import ChromeDriverManager
            from selenium.webdriver.chrome.service import Service
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as fallback_error:
            print(f"Fallback initialization failed: {fallback_error}")
            print("Please ensure Google Chrome is installed on the system.")
            sys.exit(1)
    
    try:
        # 1. Load Landing Page
        print("Loading Landing Page...")
        driver.get(target_url)
        wait = WebDriverWait(driver, 15)
        
        # Verify page loads
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print(f"Page title: {driver.title}")
        
        # 2. Test navigation to Login Page
        print("Navigating to Login Page...")
        sign_in_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign In') or contains(text(), 'SIGN IN')]")))
        sign_in_link.click()
        
        # Wait until login form is visible
        print("Waiting for Login Page to load...")
        wait.until(EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Welcome back')]")))
        print(f"Current URL: {driver.current_url}")
        
        # 3. Test Invalid Login
        print("Testing login with invalid credentials...")
        email_input = driver.find_element(By.XPATH, "//input[@type='email']")
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        email_input.send_keys("invalid_user@example.com")
        password_input.send_keys("WrongPassword123")
        submit_btn.click()
        
        # Verify error message shows up
        print("Waiting for login response/error...")
        try:
            error_banner = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'failed') or contains(text(), 'error') or contains(text(), 'Invalid') or contains(@style, 'danger')]")))
            print(f"Success: Found expected login error banner.")
        except Exception:
            print("Warning: Expected error banner not found.")
            
        # 4. Navigate to Register Page using the link in the login form footer
        print("Navigating to Register Page via footer link...")
        create_account_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Create one')]")))
        create_account_link.click()
        
        # Wait until register form is visible
        print("Waiting for Register Page to load...")
        name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Dr. Jane Smith']")))
        email_reg_input = driver.find_element(By.XPATH, "//input[@type='email']")
        pass_reg_input = driver.find_element(By.XPATH, "//input[@type='password']")
        submit_reg_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # 5. Test Register Page form interaction
        print("Testing Register Page form interaction...")
        name_input.send_keys("Test Doctor")
        email_reg_input.send_keys("testdoctor@healthsense.ai")
        pass_reg_input.send_keys("123")
        
        disabled_attr = submit_reg_btn.get_attribute("disabled")
        print(f"Is register submit button disabled for password length < 6? {disabled_attr}")
        assert disabled_attr == "true" or disabled_attr is not None
        
        pass_reg_input.clear()
        pass_reg_input.send_keys("Password123!")
        
        disabled_attr = submit_reg_btn.get_attribute("disabled")
        print(f"Is register submit button disabled for valid password? {disabled_attr}")
        assert disabled_attr is None or disabled_attr == "false"
        
        # 6. Navigate back to Login Page using footer link
        print("Navigating back to Login Page via footer link...")
        sign_in_footer_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign in')]")))
        sign_in_footer_link.click()
        
        # 7. Test Demo Bypass Login (Empty fields, click Continue)
        print("Testing Demo Bypass Login...")
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        
        # Clear fields
        email_input.send_keys(Keys.CONTROL + "a")
        email_input.send_keys(Keys.BACKSPACE)
        password_input.send_keys(Keys.CONTROL + "a")
        password_input.send_keys(Keys.BACKSPACE)
        
        submit_btn.click()
        
        print("Waiting for dashboard redirect...")
        try:
            wait.until(EC.url_contains("/dashboard"))
            print(f"Successfully redirected! Current URL: {driver.current_url}")
            dashboard_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Dashboard') or contains(text(), 'Welcome')]")))
            print(f"Dashboard verification element text: '{dashboard_element.text[:40]}...'")
            print("Selenium test execution finished successfully!")
        except TimeoutException as te:
            print("Timeout waiting for dashboard redirect! Capturing browser console logs:")
            for entry in driver.get_log('browser'):
                print(f"[Browser Console] {entry}")
            raise te
        
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()
