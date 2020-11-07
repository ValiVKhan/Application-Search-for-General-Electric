import time
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

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
    driver.get('https://apps.gehealthcare.com/request-more-information')
    print ("Form Opened")
    time.sleep(3)
opener()

product_number = 0

def submit():

    file_open = open('productnames.txt', 'r')

    all_lines = file_open.readlines()

    product_name = (all_lines[product_number])


    #Country  
    Country = driver.find_element_by_xpath('//*[@id="Country"]/option[2]')
    Country.click()
    time.sleep(.1)

    #Email
    Email =  driver.find_element_by_xpath('//*[@id="Email"]')
    Email.send_keys("Vajih.khan@ge.com")

    #First name
    First_name = driver.find_element_by_xpath('//*[@id="FirstName"]')
    First_name.send_keys("Vajih")

    #Last name
    Last_name = driver.find_element_by_xpath('//*[@id="LastName"]')
    Last_name.send_keys("Khan")

    #Job Title
    Job = driver.find_element_by_xpath('//*[@id="Title"]')
    Job.send_keys("Consultant Software Marketplace")

    #Company
    Comapny = driver.find_element_by_xpath('//*[@id="formCompanyName"]')
    Comapny.send_keys("GE")

    #Postal Code
    #Post = driver.find_element_by_xpath('//*[@id="PostalCode"]')
    #Post.send_keys("77382")

    #How Can We Help You
    Help = driver.find_element_by_xpath('//*[@id="inquiry_type"]/option[2]')
    Help.click()

    #QUESTIONS / REQUEST DETAILS:
    Questions = driver.find_element_by_xpath('//*[@id="contact_question"]')
    Questions.send_keys("This is a TEST.")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("I am testing the ‘Request More Information’ page on GE Software Marketplace.")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("Please email me this form submission at: vajih.khan@ge.com")
    Questions.send_keys(Keys.RETURN)
    Questions.send_keys("This test was submitted on the form for: " + str(product_name))

    #Submit
    Submit = driver.find_element_by_xpath('//*[@id="mktoForm_63597"]/div[29]/span/button')
    Submit.click()



submit()
