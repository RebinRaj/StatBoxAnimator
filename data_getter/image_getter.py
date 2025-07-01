from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import os
import undetected_chromedriver as uc
import random

def download_images(query, info, download_path):

    #Stop chrome popup using options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    #Instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    #Open Google Images
    driver.get("https://www.google.com/imghp")
    
    #Get search box element, type query and search
    search_box = driver.find_element("name", "q")
    query_val = query + info
    search_box.send_keys(query_val)
    search_box.send_keys(Keys.RETURN)

    #Wait for the page to load
    wait = WebDriverWait(driver, 10)

    #Scroll down to load more images
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait = WebDriverWait(driver, 10)

    #Get all image elements in a list
    img_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.YQ4gaf")))

    valid_imgs = [
    img for img in img_elements
    if img.get_attribute("src") and "http" in img.get_attribute("src") and
    img.get_attribute("width") and int(img.get_attribute("width")) > 60]
    
    #Click first element
    if valid_imgs:
        try:
            target_img = valid_imgs[0]
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", target_img)
            time.sleep(random.uniform(1, 3))
            driver.execute_script("arguments[0].click();", target_img)
            #Create the download directory and download from source
            os.makedirs(download_path, exist_ok=True)
            img_url = target_img.get_attribute("src")
            img_name = os.path.join(download_path, f"{query}.jpg")
            urllib.request.urlretrieve(img_url, img_name)
            print(f"Downloaded: {img_name}")
        except Exception as e:
            print("Error while clicking image:", e)
            
    else:
        print("No valid image found to click.")

    
    # Close the browser
    driver.quit()

    return True


def download_images_up(query, info, download_path):

    #Stop chrome popup using options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    #Instance of the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    
    #Open Google Images
    driver.get("https://www.google.com/imghp")
    
    #Get search box element, type query and search
    search_box = driver.find_element("name", "q")
    query_val = query + info
    search_box.send_keys(query_val)
    search_box.send_keys(Keys.RETURN)
    
    #Wait for the page to load
    wait = WebDriverWait(driver, 10)

    #Scroll down to load more images
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait = WebDriverWait(driver, 10)

    #Get all image elements in a list
    img_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.YQ4gaf")))

    valid_imgs = [
    img for img in img_elements
    if img.get_attribute("src") and "http" in img.get_attribute("src") and
    img.get_attribute("width") and int(img.get_attribute("width")) > 60]
    
    #Click first element
    if valid_imgs:
        try:
            target_img = valid_imgs[0]
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'})", target_img)
            time.sleep(random.uniform(1, 3))
            driver.execute_script("arguments[0].click();", target_img)

            full_img_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.sFlh5c.FyHeAf.iPVvYb")))
            for full_img in full_img_elements:
                img_url = full_img.get_attribute("src")
                if img_url and "http" in img_url:
                    os.makedirs(download_path, exist_ok=True)
                    img_name = os.path.join(download_path, f"{query}.jpg")
                    urllib.request.urlretrieve(img_url, img_name)
                    print(f"Downloaded: {img_name}")
                    break
                else:
                    print("Full-size image not found.")

        except Exception as e:
            print("Error while clicking or downloading:", e)
    else:
        print("No valid images to click.")

    # Close the browser
    driver.quit()
    return True
