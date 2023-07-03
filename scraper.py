from linkedin_scraper import Person, actions
from selenium import webdriver

driver = webdriver.Chrome()

email = "dev@gssp.io"
password = "mez9jcr_bfq7JCD6xeg"
actions.login(driver, email, password)
# if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/gssp/", driver=driver)
