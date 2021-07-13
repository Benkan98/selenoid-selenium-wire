import time
import logging

from selenium import webdriver

# selenoid without selenium-wire works great!

logging.basicConfig(level=logging.DEBUG)

capabilities = {
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True
    }
}

driver = webdriver.Remote(
    desired_capabilities=capabilities
)

driver.get("http://host.docker.internal:5000") #localhost:5000

print(driver.title)



time.sleep(15)
driver.close()
