from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import time
import csv



user = 'x1055082'
passw = 'KaFaA1wz' 
time_to_sleep = 10
data_files = ['Java_Update_PLT3.csv','Java_Update_W_Fixes_PLT1.csv','Java_Update_W_Fixes_PLT3.csv']
urls = [
    'https://pdtjira.eps.ti.com/secure/Tests.jspa#/testCycle/NSS-C57',
    'https://pdtjira.eps.ti.com/secure/Tests.jspa#/testCycle/NSS-C58',
    'https://pdtjira.eps.ti.com/secure/Tests.jspa#/testCycle/NSS-C59'
    ]
data_file_element= 1

chrome_options =  Options()
#Los siguientes dos lineas deshabilitan las infobars.
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--deny-permission-prompts")
driver =  webdriver.Chrome(executable_path='C:\\Users\\x1055082\\workspaces\\python\\resources\\chromedriver.exe', chrome_options=chrome_options)
driver.implicitly_wait(40) # seconds


driver.get('https://pdtjira.eps.ti.com/secure/Dashboard.jspa')
driver.find_element_by_name('os_username').send_keys(user)
driver.find_element_by_name('os_password').send_keys(passw)
driver.find_element_by_name('login').click()
time.sleep(5)
#driver.get('https://pdtjira.eps.ti.com/secure/Tests.jspa#/testCycle/NSS-C53')
driver.get(urls[data_file_element])
print("Accediendo a la URL: " + urls[data_file_element])
wait = WebDriverWait(driver,20)
element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div > div > div > floating-header > div > ng-transclude > header-content > aui-navigation > nav > div > div > ul > li:nth-child(2) > a')))
element.click()

try:
    time.sleep(10)
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[class="sc-jzJRlG dkPHSs"]')))
    element.click()
    time.sleep(10)
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#ngdialog1 > div.ngdialog-content > span > div > div.ktm-modal-dialog-content > div > div.ktm-library-test-case-list > div.ktm-toolbar-placeholder > div > div:nth-child(1) > div > div.ktm-library-toolbar-right > button')))
    element.click()
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#ngdialog1 > div.ngdialog-content > span > div > div.ktm-modal-dialog-content > div > div.ktm-library-test-case-list > div.ktm-toolbar-placeholder > div > div.ktm-row.ktm-filters.ng-scope > div > div.ktm-filter-content > test-case-field-chooser > filter-button > button')))
    element.click()
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#ktm-uid-1 > div > div.ktm-popup-search > div > input')))
    element.send_keys('QC Test ID')
    element =  driver.find_elements_by_css_selector('li[ng-click="toggleItem(displayItem)"][class="ng-scope"][role="button"]')
    element[0].click()

    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(),"QC Test ID: All")]')))
    element.click()
    
    list_of_elements=[]
    print("Utilizando %s" % data_files[data_file_element])
    with open('C:\\Users\\x1055082\\workspaces\\python\\testmove\\src\\test_move\\'+data_files[data_file_element]) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            list_of_elements.append(row)

    with open('C:\\Users\\x1055082\\workspaces\\python\\testmove\\src\\test_move\\'+data_files[data_file_element]) as csv_file:
        csv_reader = csv.reader(csv_file)
        file = open("log_invalidos_"+data_files[data_file_element]+".txt",'w')
        for row in csv_reader:
            if row =="":
                print("Elemento vacio")
                continue
            element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="text"][placeholder="Contains text"]')))
            element.clear()
            time.sleep(time_to_sleep)
            element.send_keys(row,Keys.RETURN)
            time.sleep(time_to_sleep)
            hidden_element =  driver.find_element_by_xpath('//button[contains(text(),"modifying")]')
            try:
                checkbox_test_case = driver.find_element_by_css_selector('input[ng-model="testCase.$selected"]')
            except:
                pass
            if  hidden_element.is_displayed() or not checkbox_test_case.is_displayed():
                if hidden_element.is_displayed():
                    print('El elemento no se encuentra', row)
                else:
                    print("Elemento ya agregado.", row)
                file.write("%s \n" % row)
                if row == list_of_elements[len(list_of_elements)-1]:
                    close_element = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(),"Close")]')))
                    close_element.click()
                else:
                    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"QC Test ID:")]')))
                    time.sleep(20)
                    element.click()
                    continue
            else:
                print("Elemento valido", row)
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'input[type="checkbox"][class="ng-pristine ng-untouched ng-valid ng-empty"]')))
                time.sleep(time_to_sleep)
                element.click()
                element = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(),"Add")]')))
                time.sleep(time_to_sleep)
                element.click()
                if row == list_of_elements[len(list_of_elements)-1]:
                    continue
                element = WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'//span[contains(text(),"Add test cases")]')))
                time.sleep(time_to_sleep)
                element.click()
                element = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(text(),"QC Test ID:")]')))
                time.sleep(time_to_sleep)
                element.click()
                time.sleep(time_to_sleep)
    file.close()
    element = wait.until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Save")]')))
    time.sleep(time_to_sleep+2)
    element.click()
    time.sleep(3)

except ValueError:
    print('Fail in execution.')
    driver.close()

finally:
    driver.get_screenshot_as_file("fail_moment.png")
    driver.close()

print("Prueba completada")
driver.quit()
