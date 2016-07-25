import time

from selenium.webdriver.support.ui import WebDriverWait

from .base import FunctionalTest

TEST_EMAIL = 'edith@mockmyid.com'

class LoginTest(FunctionalTest):
    

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

    def test_login_with_persona(self):
        # Edith 前往很棒的超級清單網站
        # 並且在第一次來到時, 發現了一個"Sign in" 連結
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        # 一個Persona 登入方塊出現了
        self.switch_to_new_window('Mozilla Persona')

        # Edith 用他的email 地址登入
        ## 使用 mockmyid.com 來測試 email
        self.browser.find_element_by_id(
            'authentication_email'
        ).send_keys(TEST_EMAIL)
        self.browser.find_element_by_tag_name('button').click()

        # Persona 視窗關閉
        self.switch_to_new_window('To-Do')

        # 他可以看到她登入了
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # 重新整理網頁時，他看到他是真正的工作階段登入，
        # 而非只是一次性的登入網頁
        self.browser.refresh()
        self.wait_to_be_logged_in(email=TEST_EMAIL)

        # 他被這個新功能嚇到，反射性地按下 "logout"
        self.browser.find_element_by_id('id_logout').click()
        self.wait_to_be_logged_out(email=TEST_EMAIL)

        # 'logged out' 狀態在重新整理後也會保持
        self.browser.refresh()
        self.wait_to_be_logged_out(email=TEST_EMAIL)


