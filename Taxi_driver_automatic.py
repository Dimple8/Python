from selenium import webdriver
from selenium.webdriver.common.keys import Keys
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

# instantiate
config = ConfigParser()

# parse existing file
config.read('settings.ini')

# read values from a section
baseUrl = config.get('DEFAULT', 'Url')
nameElement = config.get('DEFAULT', 'FullName_elementName')
phoneElement = config.get('DEFAULT', 'Phone_elementName')

driver = webdriver.Safari()
driver.get(baseUrl)

# print(driver.title)

# driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://forms.yandex.ru/surveys/10017467/?iframe=1&theme=&lang=ru&click_id=")]'))

# try:
#     username = driver.find_element_by_name("answer_short_text_89867")
#     username.clear()
#     username.send_keys("Driver1")

#     username = driver.find_element_by_name("answer_phone_89868")
#     username.clear()
#     username.send_keys("12345678")
# except:
#     print("Произошла ошибка при вводе данных элементу 'ФИО'.")

# driver.switch_to.default_content()
driver.close()