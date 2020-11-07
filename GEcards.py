import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
#Question
#spam_count = input("How many times? ")
start_time = time.time()
repeat_count = 0

# Initiliaze Webdriver
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#Form opener
def opener():
    # Opening Form.
    driver.get('https://apps.gehealthcare.com')
    print ("Form Opened")
    sleep(3)
opener()


global cardnum
cardnum = 1

def card():

    global cardnum

    cardname = driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div['+str(cardnum)+']/div/div/div[1]/a/h3')
    product_name = (cardname.text)
    print(cardname.text)
    sleep(5)

    cardnum = int(1)
    cardfidner = driver.find_element_by_xpath('//*[@id="root"]/main/div/div/div['+str(cardnum)+']/div/div/div[2]/a')
    cardfidner.click()
    cardnum += 1

    contactus = driver.find_element_by_xpath('//*[@id="root"]/main/section[2]/div[1]/div/div[4]/div[2]/div[3]/div[1]/div/button')
    contactus.click()
    #Requesting More Informatiomn
    requestmoreinfo = driver.find_element_by_xpath('//*[@id="eds-popover"]/div/div/a[2]')
    requestmoreinfo.click()
    sleep(3)


    #Country  
    Country = driver.find_element_by_xpath('//*[@id="Country"]/option[2]')
    Country.click()
    sleep(.2)

    #Email
    Email =  driver.find_element_by_xpath('//*[@id="Email"]')
    Email.send_keys("Vajih.khan@ge.com")
    sleep(.2)
    #First name
    First_name = driver.find_element_by_xpath('//*[@id="FirstName"]')
    First_name.send_keys("Vajih")
    sleep(.2)
    #Last name
    Last_name = driver.find_element_by_xpath('//*[@id="LastName"]')
    Last_name.send_keys("Khan")
    sleep(.2)
    #Job Title
    Job = driver.find_element_by_xpath('//*[@id="Title"]')
    Job.send_keys("Consultant Software Marketplace")
    sleep(.2)
    #Company
    Comapny = driver.find_element_by_xpath('//*[@id="formCompanyName"]')
    Comapny.send_keys("GE")
    sleep(.2)
    #Postal Code
    #Post = driver.find_element_by_xpath('//*[@id="PostalCode"]')
    #Post.send_keys("77382")
    sleep(.2)
    #How Can We Help You
    Help = driver.find_element_by_xpath('//*[@id="inquiry_type"]/option[2]')
    Help.click()
    sleep(.2)
    #QUESTIONS / REQUEST DETAILS:
    Questions = driver.find_element_by_xpath('//*[@id="contact_question"]')
    Questions.send_keys("This is a TEST.")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("I am testing the ‘Request More Information’ page on GE Software Marketplace.")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("Please email me this form submission at: vajih.khan@ge.com")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("This test was submitted on the form for: " + str(product_name))
    sleep(.2)
    #Submit
    Submit = driver.find_element_by_xpath('//*[@id="mktoForm_63597"]/div[29]/span/button')
    Submit.click()
    sleep(.2)    

while cardnum != 74:
    card()
    opener()
    sleep(5)