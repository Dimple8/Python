from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pandas
from collections import defaultdict
import logging
import time
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

def get_list_from_excel_file(excelFile):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(THIS_FOLDER, excelFile)
    excel_data_df = pandas.read_excel(filePath, usecols=['ФИО', 'Корректный телефон', 'Click ID'])
    return excel_data_df.to_dict('records')


# instantiate
config = ConfigParser()

# read settings.ini file
settings = os.path.join(THIS_FOLDER, 'settings.ini')
config.read(settings)

# read values from a settings.ini file
baseUrl = config.get('DEFAULT', 'Url')
name = config.get('DEFAULT', 'NameField')
phone = config.get('DEFAULT', 'PhoneField')
timeout = config.getint('DEFAULT', 'Timeout')
isSumbit = config.getboolean('DEFAULT', 'Sumbit')

# get items from excel file
items = get_list_from_excel_file('Data.xlsx')

# open browser
driver = webdriver.Safari()
driver.maximize_window()

for item in items:
    driverName = item['ФИО']
    driverPhone = item['Корректный телефон']
    driverID = item['Click ID']

    driver.get(baseUrl + driverID)
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[starts-with(@src, "https://forms.yandex.ru/surveys/10017467/?iframe=1&theme=&lang=ru&click_id=")]'))

    # enter data
    fill_element(name, driverName)
    fill_element(phone, driverPhone) 

    if isSumbit:
        # click button                                   
        submitButton = driver.find_element_by_xpath('//button[contains(@class,"button_role_submit")]')        
        submitButton.send_keys(Keys.RETURN) 

        # try to get success message
        try:
            successMessage = driver.find_element_by_xpath('//div[starts-with(@class, "survey-success i-bem survey-success_js_inited")]')  
        except Exception as exception:
            print("Не удалось найти сообщение что заявка отправлена.")    
            logging.info("Не удалось найти сообщение что заявка отправлена.") 
            print(exception)
            raise  
           
    # write log
    print("ФИО: {0}, Телефон: {1}, Ссылка: {2}".format(driverName, driverPhone, baseUrl + driverID))    
    logging.info("ФИО: {0}, Телефон: {1}, Ссылка: {2}".format(driverName, driverPhone, baseUrl + driverID))

    driver.switch_to.default_content()
    time.sleep(timeout)
driver.close()