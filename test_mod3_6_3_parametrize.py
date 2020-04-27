#

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('urlTest',
    ["https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])

class TestFindAnswer(object):
    def test_get_link(self, browser, urlTest):
        link = f"{urlTest}"
        browser.get(link)
        answer = math.log(int(time.time()))
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID,'ember70')))
        answerTextArea = browser.find_element_by_tag_name("textarea")
        answerTextArea.send_keys(str(answer))
        button = browser.find_element_by_css_selector("button")
        button.click()
        print("Vse ok")
        # находим элемент, содержащий текст
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'pre')))
        correct_text_answer = browser.find_element_by_tag_name("pre")
        # записываем в переменную correct_text текст из элемента correct_text_answer
        correct_text = correct_text_answer.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        if "Correct!" != correct_text:
            file = open("notCorrectAnswer.txt", "a")
            file.write(correct_text)
            file.close()
        assert "Correct!" == correct_text, correct_text

        
#pre - tag; class - smart-hints__hint; text - Correct!
#class = "submit-submission" - класс у кнопки
#тег textarea - у поля для ввода

