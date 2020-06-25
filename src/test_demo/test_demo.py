from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options =  webdriver.ChromeOptions()
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--deny-permission-prompts")
driver =  webdriver.Chrome('C:\\Users\\x1055082\\workspaces\\python\\testmove\\chromedriver.exe')
baseURL="http://www.python.org"



driver.get(baseURL)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()