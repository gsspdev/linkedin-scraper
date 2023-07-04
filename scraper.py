from linkedin_scraper import Person, actions
from selenium import webdriver

driver = webdriver.Chrome("~/chromedriver")

email = ""
password = ""
actions.login(driver, email, password)
# if email and password isnt given, it'll prompt in terminal
person = Person("", driver=driver)
