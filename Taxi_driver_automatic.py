from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import logging
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(THIS_FOLDER, 'result.log'), encoding='utf-8', level=logging.INFO)

def fill_element(elementName, text):
    elem = driver.find_element_by_name(elementName)
    elem.clear()
    elem.send_keys(text)

# instantiate
config = ConfigParser()

# read settings.ini file
settings = os.path.join(THIS_FOLDER, 'settings.ini')
config.read(settings)

# read values from a settings.ini file
baseUrl = config.get('DEFAULT', 'Url')
name = config.get('DEFAULT', 'NameField')
phone = config.get('DEFAULT', 'PhoneField')

# open browser
driver = webdriver.Safari()
driver.get(baseUrl)

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://forms.yandex.ru/surveys/10017467/?iframe=1&theme=&lang=ru&click_id=")]'))

driverName = "Водитель_1"
driverPhone = "8896464"
# enter data
fill_element(name, driverName)
fill_element(phone, driverPhone)
print('Обработаны данные для: ' + driverName + ' - ' + driverPhone)
logging.info('Обработаны данные для: ' + driverName + ' - ' + driverPhone)

driver.switch_to.default_content()
driver.close()