from selenium import webdriver;
import time;
import os

driver=webdriver.Chrome();
#driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.seleniumeasy.com/test")

simple_title = driver.title
print(simple_title)


# filling form
#
driver.find_element_by_xpath("//a[text()='Input Forms']").click()


time.sleep(3)

simpleDemoForm = "//a[text()='Input Forms']/parent::li/descendant::a[contains(text(),'Simple Form')]"

driver.find_element_by_xpath(simpleDemoForm).click()
time.sleep(2)


inputMessage = "Python"

driver.find_element_by_xpath("//input[@id='user-message']").send_keys(inputMessage)
time.sleep(1)


driver.find_element_by_xpath("//button[@class='btn btn-default' and text()='Show Message']").click()


validationMessage = driver.find_element_by_xpath("//*[@id='display']").text

if validationMessage in inputMessage :
    print("Passed")
else:
    print("Failed")



# driver.forward()
#
# driver.back()


#current url
# currentUrl = driver.current_url
#
# print(currentUrl)

#Page_source
# page_source = driver.page_source
#
# if "Examples to Basic start with Selenium" in page_source :
#     print("Passed")
# else:
#     print("Failed")

#Link text
# myLinkWebEle = driver.find_element_by_partial_link_text("Practising")
#
# myLinkWebEle.click()

# css selectors
# myLinkWebEle = driver.find_element_by_css_selector("h3.head.text-center")
# print(myLinkWebEle.text)


# xpath
# webele = driver.find_element_by_xpath("//a[@id='btn_basic_example']")
# webele.click()
# #
# time.sleep(2)
#
#
# driver.refresh()





# listVar = driver.find_elements_by_xpath("(//h3[@class='head text-center'])[2]")
#
#
# print(len(listVar))
#
#
# for ele in listVar:
#     print(ele.text)



time.sleep(3)

# driver.quit()