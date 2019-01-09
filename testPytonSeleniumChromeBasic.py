import os
from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
import time 


PATHCHROMEDRIVER = "/usr/local/bin/chromedriver"
#URL = 'https://phptravels.com/demo/'
URL = 'http://192.168.11.186/Migracion-Web/admin/login'


chromedriver = PATHCHROMEDRIVER
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get( URL )


#**********************************************************************
#Admin Login:

#Ingresa Datos en Formulario Login (username, password)
driver.find_element_by_id("username").send_keys("zweicom")
driver.find_element_by_id("password").send_keys("zweicom")

#Click en Button Login:
submit_button = driver.find_element_by_id('login')
submit_button.click()



#**********************************************************************
#Ventana Menu de Opciones:

time.sleep(2)

#Click en Menu Administracion 144:
menu = driver.find_element_by_id('dijit__TreeNode_2_label')
menu.click()

menu = driver.find_element_by_id('dijit__TreeNode_2_label')
menu.click()


time.sleep(1)


#Click en SubMenu Plan Code:
subMenu = driver.find_element_by_id('dijit__TreeNode_12_label')
subMenu.click()

time.sleep(1)


nombreTab = driver.find_element_by_id('tabContainer_tablist_mainTabModule43')

print nombreTab.get_attribute('innerHTML')


titleTab = "Highlighted Deal"

if( nombreTab.get_attribute('innerHTML') == titleTab ):
    print "test esta ok..."
else:
    print "test no coincide el  nombre del Tab..."









'''
delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'dijit__TreeNode_5_label')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"




'''



'''
browser = webdriver.Firefox()
browser.get("url")
delay = 3 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
    
'''
