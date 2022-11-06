# import time
#
# from behave import *
# from selenium import webdriver
#
#
# @given('Open the browser and enter the valid url')
# def launch_browser(context):
#     context.driver = webdriver.Chrome()
#     context.driver.maximize_window()
#     context.driver.implicitly_wait(20)
#
#
# @when('Open the PharmEasy application')
# def offer_btn(context):
#     context.driver.get("https://pharmeasy.in/")
#     time.sleep(5)
#
#
# @when('Click on Offers tab')
# def offer_btn(context):
#     context.driver.find_element("xpath", '//a[@aria-label="offers"]').click()
#
#
# @then('All offers should be displayed')
# def offer_page(context):
#     pass
#
#
# @when('Click on Payment button')
# def all_btn(context):
#     context.driver.find_element("xpath", '//div[text()="Payment"]').click()
#
#
# @when('Click on Copy Code button')
# def copy_btn(context):
#     try:
#         context.driver.find_element("xpath",
#                                     '//div[@class="OffersCard_container__2g9dg"][1]//span[text()="Copy Code"]').click()
#     except:
#         context.driver.find_element("xpath",
#                                     '//div[@class="OffersCard_container__2g9dg"][1]//span[text()="Continue"]').click()
#
#
# @when('Click on Coupon')
# def copy_btn(context):
#     try:
#         context.driver.find_element("xpath", '//div[@class="OffersCard_container__2g9dg"][1]').click()
#     except:
#         pass
#
#
# @when("Click on Coupon's Copy Code button")
# def copy_btn(context):
#     try:
#         context.driver.find_element("xpath", '//button[text()="COPY CODE"]').click()
#     except:
#         pass
#
#
# @when("Click on Coupon's Copy Code and Proceed button")
# def copy_btn(context):
#     try:
#         context.driver.find_element("xpath", '//button[text()="Copy Code & Proceed"]').click()
#     except:
#         pass
#
#
# @then(
#     'Payment mode offers should be displayed and User is able to click on Copy Code button and offer code Pop-Up message is displayed')
# def step_impl(context):
#     context.driver.close()
