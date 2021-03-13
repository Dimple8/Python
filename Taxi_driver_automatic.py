from selenium import webdriver
from selenium.webdriver.common.keys import Keys
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

def fill_element(elementName, text):
    elem = driver.find_element_by_name(elementName)
    elem.clear()
    elem.send_keys(text)

# instantiate
config = ConfigParser()

# parse existing file
config.read('settings.ini')

# read values from a settings.ini file
baseUrl = config.get('DEFAULT', 'Url')
name = config.get('DEFAULT', 'NameField')
phone = config.get('DEFAULT', 'PhoneField')

# open browser
driver = webdriver.Safari()
driver.get(baseUrl)

print(driver.title)

driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://forms.yandex.ru/surveys/10017467/?iframe=1&theme=&lang=ru&click_id=")]'))

fill_element(name, "Водитель_1")
fill_element(phone, "8896464")

# try:
#     usernameElem = driver.find_element_by_name(nameElement)
#     usernameElem.clear()
#     usernameElem.send_keys("Driver1")

#     phoneElem = driver.find_element_by_name(phoneElement)
#     phoneElem.clear()
#     phoneElem.send_keys("12345678")
# except:
#     print("Произошла ошибка при вводе данных элементу , 'ФИО'.")

driver.switch_to.default_content()
driver.close()