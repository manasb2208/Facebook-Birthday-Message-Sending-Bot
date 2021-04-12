cd = "C:\\Users\\Manas\\Desktop\\chromedriver.exe"
em = "*********@domain.com" #Here user has to provide 
pwd = "abcd1234" #Provie password

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(cd) #creating webdriver
driver.get("https://www.facebook.com/login/") #to go to the sign in page of linked in 
time.sleep(5) #it will hold for 5 seconds
eml=driver.find_element_by_xpath("//input[@type = 'text']")
eml.send_keys(em)
pswrd = driver.find_element_by_xpath("//input[@type = 'password']")
pswrd.send_keys(pwd)
btn=driver.find_element_by_xpath("//button[@value = '1']")
btn.click()
time.sleep(15)

nots=driver.find_elements_by_xpath('//div[@class="cxgpxx05 sj5x9vvc"]')
nots[2].click()
time.sleep(3)

wish = 'Happy Birthday'
wish_b = driver.find_elements_by_xpath('//div[@class="_1mf _1mj"]')

for i in wish_b:
	i.send_keys(wish)
	i.send_keys(Keys.ENTER)


print("Done")
time.sleep(30)
driver.close()