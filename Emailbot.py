#You can simplify this code
#I chose protonmail
user = input("enter the username: ")
passw = input("enter the password: ")
to = input("enter the recipient email: ")
body = input("enter what message you want to send: ")

from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True  # To make browser visible set it to False
path = chromedriver_autoinstaller.install()  # Returns path of the chromedriver.exe
driver = webdriver.Chrome(executable_path=path, options=options)

driver.get('https://mail.protonmail.com/login')

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




actions = ActionChains(driver)
actions.send_keys(str(user))#your proton mail user
actions.perform()

time.sleep(4)

actions2 = ActionChains(driver)
actions2.send_keys(Keys.TAB)
actions2.perform()

time.sleep(1)

actions3 = ActionChains(driver)
actions3.send_keys(str(passw))#your protonmail password
actions3.perform()

time.sleep(1)

actions4 = ActionChains(driver)
actions4.send_keys(Keys.TAB)
actions4.perform()
actions4.perform()

time.sleep(1)

actions5 = ActionChains(driver)
actions5.send_keys(Keys.ENTER)
actions5.perform()

time.sleep(10)

compose_button = driver.find_element_by_xpath("""//*[@id="pm_sidebar"]/button""")
compose_button.click()
time.sleep(3)

actions6 = ActionChains(driver)
actions6.send_keys(str(to)) #To
actions6.perform()

time.sleep(2)

actions7 = ActionChains(driver)
actions7.send_keys(Keys.TAB)
actions7.perform()
actions7.perform()
actions7.perform()

actions8 = ActionChains(driver)
actions8.send_keys(str(body))#Body
actions8.perform()

actions9 = ActionChains(driver)
actions9.send_keys(Keys.TAB)
actions9.perform()
actions9.perform()
actions9.perform()
actions9.perform()
actions9.perform()
actions9.perform()

time.sleep(3)

actions10 = ActionChains(driver)
actions10.send_keys(Keys.ENTER)
actions10.perform()

time.sleep(1)

actions10.perform()

time.sleep(7)


