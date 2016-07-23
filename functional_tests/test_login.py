import time

from selenium.webdriver.support.ui import WebDriverWait

from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        # Edith 前往很棒的超級清單網站
        # 並且在第一次來到時, 發現了一個"Sign in" 連結
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('login').click()

        # 一個Persona 登入方塊出現了
        self.switch_to_new_window('Mozilla Persona')

        # Edith 用他的email 地址登入
        ## 使用 mockmyid.com 來測試 email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        # Persona 視窗關閉
        self.switch_to_new_window('To-Do')

        # 他可以看到她登入了
        self.wait_for_element_with_id('logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edith@mockmyid.com', navbar.text)

    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail('could not find window')

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=100).until(
            lambda b: b.find_element_by_id(element_id)
        )