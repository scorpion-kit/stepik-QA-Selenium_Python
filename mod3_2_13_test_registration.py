from selenium import webdriver
import time
import math
import unittest

class TestRegistration(unittest.TestCase): #класс, наследуемый от TestCase
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[placeholder=\"Input your first name\"]")
        input1.send_keys("Ivanov")
        input2 = browser.find_element_by_css_selector("input[placeholder=\"Input your last name\"]")
        input2.send_keys("Petr")
        input3 = browser.find_element_by_css_selector("input[placeholder=\"Input your email\"]")
        input3.send_keys("S@ya.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",
                welcome_text,
                "Should be \'Congratulations! You have successfully registered!\'")
        
    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input[placeholder=\"Input your first name\"]")
        input1.send_keys("Ivanov")
        input2 = browser.find_element_by_css_selector("input[placeholder=\"Input your last name\"]")
        input2.send_keys("Petr")
        input3 = browser.find_element_by_css_selector("input[placeholder=\"Input your email\"]")
        input3.send_keys("S@ya.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!",
                welcome_text,
                "Should be \'Congratulations! You have successfully registered!\'")
    
#конструкция if __name__ == "__main__"
#служит для подтверждения того что данный скрипт был запущен напрямую
if __name__ == "__main__":
    unittest.main()
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
