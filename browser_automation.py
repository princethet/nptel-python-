#browser automation like whatsapp
""" pip install selenium  
    It is requried to install for this project
    
    step 2 - installing the webdriver for the chrome

    """

from selenium import webdriver
# wd = r"C:\Users\91799\Downloads"
browser = webdriver.Chrome("C:\webdriver")

# browser.get("https://www.selenum.org")

# elem = browser.find_element_by_link_text('download')

# elem.click()

# search = browser.find_element_by_link_id('q')

# search.send_keys('download')


# #whatsapp automation

# from selenium import webdriver
# from selenium.webdriver.support.ui import webdriverWait
# from selenium.webdriver.support import expected_conditions as EC 
# from selenium.webdriver.common.keys import Keys 
# from selenium.webdriver.common.by import By 
# import time
# driver = webdriver.chrome("cpy the path of the webdriver here")
# driver.get("https://web.watsapp.com/")
# wait = webDriverWait(driver,600)
# target = '"sunny"'
# string = "you're hacked and fucked"
# x_arg = "//span[contains(@title, + target + ')]"
# target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
# target.click()

# input_box = driver.find_element_by_class_name('write here the class of the message text box of the whatsapp using the inspect method')

# for i in range(100):
#     input_box.send_keys(string+Keys.ENTER)