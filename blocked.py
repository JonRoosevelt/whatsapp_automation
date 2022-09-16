import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('./chromedriver')

def remove_blocked(quantity: int) -> None:
    print(f'Removing {quantity} blocked contacts')
    for _ in list(range(0, quantity)):
        x = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='chat-controls'][role='button']")))
        x.click()
        time.sleep(1)
        ok = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='popup-controls-ok'][role='button']")))
        ok.click()
        time.sleep(1)

def run() -> None:
    try:
        driver.get('https://web.whatsapp.com/')
        print('Scan QR code, and then press Enter')
        input('Press to continue...')
        menu_bar_menu_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='menu-bar-menu']")))
        menu_bar_menu_button.click()
        chat_list_dropdown = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[data-testid='chatlist-dropdown-item-settings']")))
        chat_list_dropdown.click()
        privacy = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='settings-drawer-item-privacy'][role='button']")))
        privacy.click()
        time.sleep(1)
        left_drawer = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='drawer-left']")))
        blocked_contacts = left_drawer.find_elements(By.CSS_SELECTOR, "div[role='button']")[-1]
        quantity = blocked_contacts.text.split('\n')[1] 
        if quantity.isnumeric():
            blocked_contacts.click()
            remove_blocked(int(quantity))
        else:
            print('No blocked contacts')
    except Exception as e:
        print('Error:', e)
    finally:
        driver.quit()

if __name__ == '__main__':
    run()
