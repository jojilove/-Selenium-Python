from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input[name=first_name]")
    input1.send_keys("Her")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("s")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Gory")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("oof")
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
