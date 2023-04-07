import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://aprendepython.es")

toc = driver.find_elements(By.CSS_SELECTOR, 'div.sidebar-tree li.toctree-l1')

toc_list = []

for heading in toc:
    toc_list.append(heading.text)

def lleverInfo(list = []):

    list = toc_list

    return list

time.sleep(100)


