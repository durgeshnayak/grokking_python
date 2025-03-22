import selenium.webdriver.common.by
from selenium import webdriver


chrome_driver_path = "/Users/durgeshnayak/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

upcoming_events_schedule = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, 'div.event-widget time')
upcoming_events = driver.find_elements(selenium.webdriver.common.by.By.CSS_SELECTOR, 'div.event-widget li a')

dict_events = {}

for index in range(len(upcoming_events_schedule)):
    dict_events[index] = {
        "time": upcoming_events_schedule[index].text,
        "name": upcoming_events[index].text
    }

print(dict_events)

driver.quit()
