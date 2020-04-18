from selenium import webdriver
import time
import math


def calc(x, y):
  return str((int(x) + int(y)))

try:  
    link = "http://suninjuly.github.io/selects2.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    
    x_element = browser.find_element_by_css_selector("span[id='num1']")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("span[id='num2']")
    y = y_element.text
    print (x)
    print (y)
    sum_answ = calc(x, y)
    print (sum_answ)
    
    #Ответ выбираем
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_answ)
    #browser.find_element_by_tag_name("select").click()
    #browser.find_element_by_css_selector("[value=sum_answ]").click()
                    
    # Жмакаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
  
    print("Vse ok")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
