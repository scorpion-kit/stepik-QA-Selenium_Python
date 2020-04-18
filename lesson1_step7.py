from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html" 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код
    img_x_element = browser.find_element_by_css_selector("img#treasure")
    x_element = img_x_element.get_attribute ("valuex")
    print (x_element)
    y = calc(x_element)

    #Ответ вписываем
    answer = browser.find_element_by_tag_name("input#answer")
    answer.send_keys(y)

    # Ставим флажок и переключатель
    chbox = browser.find_element_by_id("robotCheckbox")
    chbox.click()

    radiob = browser.find_element_by_id("robotsRule")
    radiob.click()

    # Жмакаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
  
    print("Vse ok")
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
