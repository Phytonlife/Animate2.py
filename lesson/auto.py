from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from data import username, password
import time
import random


# def login(username, password):
#     browser = webdriver.Chrome('../chromedriver/chromedriver')
#
#     try:
#
#         browser.get('https://www.instagram.com')
#         time.sleep(random.randrange(3, 5))
#
#         username_input = browser.find_element_by_name("username")
#         username_input.clear()
#         username_input.send_keys(username)
#
#         time.sleep(2)
#
#         password_input = browser.find_element_by_name("password")
#         password_input.clear()
#         password_input.send_keys(password)
#
#         password_input.send_keys(Keys.ENTER)
#         time.sleep(10)
#
#         browser.close()
#         browser.quit()
#     except Exception as ex:
#         print(ex)
#         browser.close()
#         browser.quit()
#
#
# login(username, password)

def hashtag_search(username,password,hashtag):
    browser = webdriver.Chrome('../chromedriver/chromedriver')

    try:

        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name("username")
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        try:
            browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
            time.sleep(5)

            browser.close()
            browser.quit()

        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()


    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()
hashtag_search(username,password,"%D0%B0%D1%82%D1%8B%D1%80%D0%B0%D1%83")
