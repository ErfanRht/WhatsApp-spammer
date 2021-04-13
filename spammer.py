# This is a whatsapp-spambot
# You must install selenium library
from selenium import webdriver
from time import sleep
import random

# The Functions
# This function is for clicking on a section
def click(section_xpatch):
    driver.find_element_by_xpath(section_xpatch).click()

# This function is for clearing a text feild
def clear(section_xpatch):
    driver.find_element_by_xpath(section_xpatch).clear()

# This function is for fill a text feild
def fill(section_xpatch, key):
    driver.find_element_by_xpath(section_xpatch).send_keys(str(key))

# This function is for find a section
def find(section_xpatch):
    driver.find_element_by_xpath(section_xpatch)

# The Values
whatsapp_xpatch_base = '//*[@id="main"]/footer/div[1]/'
whatsapp_textfeild_xpatch = whatsapp_xpatch_base+'div[2]'
whatsapp_sendmessagebutton_xpatch = whatsapp_xpatch_base+'div[3]'

# You must download the chromedriver
# This file is in my repository
driver = webdriver.Chrome(executable_path='/home/[username]/Desktop/chromedriver')
driver.get('https://web.whatsapp.com/')

# Waiting for loading to complete
status = ''
while status != 'ok!':
    try:
        find('//*[@id="side"]/header/div[2]/div/span/div[3]')
        status = 'ok!'
        # end
    except:
        # repeat
        pass
# Site loading completed

click('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div')

time = 0
protection = 0
for i in range (2020):
    if protection == 200:
        print('sleep')
        sleep(5)
        protection = 0
    i = i+1
    try:
        click(whatsapp_textfeild_xpatch)
        fill(whatsapp_textfeild_xpatch,i)
        if driver.find_element_by_xpath(whatsapp_textfeild_xpatch+'/div/div[2]').text == str(i):
            click(whatsapp_sendmessagebutton_xpatch)
        else:
            clear(whatsapp_textfeild_xpatch+'/div/div[2]').clear()
            click(whatsapp_textfeild_xpatch)
            fill(whatsapp_textfeild_xpatch,i)
            if driver.find_element_by_xpath(whatsapp_textfeild_xpatch+'/div/div[2]').text == str(i):
                click(whatsapp_sendmessagebutton_xpatch)

    except:
        click('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div')
        sleep(1)

    protection = protection + 1
    time = protection
    print(time)

print("The mission was completed successfully!")
# The end
