import time
import logging

from seleniumwire import webdriver

logging.basicConfig(level=logging.DEBUG)

# does not work, gives bad gateway

sw_options = {
    'auto_config': False,
    'addr': '127.0.0.1',
    'port': 9922, #setups up proxy on host machine 127.0.0.1:9922
}

capabilities = {
    "browserName": "chrome",
    "selenoid:options": {
        "enableVNC": True
    },
    'goog:chromeOptions': {'extensions': [],
                           'args': ['--proxy-server=host.docker.internal:9922', # tell selenium that the proxy exists on the host machine
                                    '--ignore-certificate-errors']
                           }
}

driver = webdriver.Remote(
    desired_capabilities=capabilities,
    seleniumwire_options=sw_options,
    command_executor="http://localhost:4444/wd/hub"
)

driver.get("http://host.docker.internal:5000") #localhost:5000
print(driver.title)

time.sleep(15)
driver.close()
