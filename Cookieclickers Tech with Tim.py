from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/') #open link

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

#select english
language = driver.find_element(By.XPATH, "//*[contains(text(),'English')]")
language.click()

#set up IDs
cookie_id = "bigCookie"
cookies_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = 'product'

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, cookie_id)) #wait for the cookie
)

# Main game loop with error handling
try:
    while True:
        try:
            # Get cookie and click it
            cookie = driver.find_element(By.ID, cookie_id)
            cookie.click()
            
            # Get cookie count
            try:
                cookies_text = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
                cookies_count = int(cookies_text.replace(',',''))
            except (ValueError, IndexError, StaleElementReferenceException):
                # Skip this iteration if we can't get cookie count
                continue
            
            # Buy upgrades
            for i in range(4):
                try:
                    product_price_element = driver.find_element(By.ID, product_price_prefix + str(i))
                    product_price_text = product_price_element.text.replace(',','')
                    
                    if not product_price_text.isdigit():
                        continue
                    
                    product_price = int(product_price_text)
                    
                    if cookies_count >= product_price:
                        product = driver.find_element(By.ID, product_prefix + str(i))
                        product.click()
                        print(f"Bought product {i}")
                        break
                        
                except (StaleElementReferenceException, NoSuchElementException):
                    # Skip this product if element is stale
                    continue
        
        except Exception as e:
            # Handle any other exceptions
            print(f"Error: {e}")
            time.sleep(0.1)  # Small delay
            
except KeyboardInterrupt:
    # Allow user to exit with Ctrl+C
    print("Bot stopped by user")
finally:
    # Cleanup
    driver.quit()