from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = True
        # firefox_capabilities["binary"] = "/Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin"
        # driver = webdriver.Firefox(capabilities=firefox_capabilities)
        # self.browser = webdriver.Firefox(capabilities=firefox_capabilities)
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard a new cool todo app.
        # She went to look its home page.
        self.browser.get('http://localhost:8000')

        # 他發現首頁標題與標頭顯示待辦事項
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # 他馬上受邀輸入一個待辦事項
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # 他在文字方塊輸入"購買孔雀羽毛"
        # 他的興趣是綁蒼蠅魚餌
        inputbox.send_keys('Buy peacock feathers')

        # 當他按下Enter時, 網頁會耕興,現在網頁列出
        # "1. 購買孔雀羽毛" 一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows), "New to-do item did not appear in table"
        )

        # 此時仍然有一個文字方塊讓他可以加入一個項目
        # 她輸入"使用孔雀羽毛來製作一隻蒼蠅" (EDITH非常有條理)
        self.fail('Finish the test!')
        # 網頁再次更新 現在他的清單上有這兩個項目

        # Edith 不知道網站能否記得他的清單
        # 接著他看到網站產生一個唯一的URL給他
        # 網頁有一些文字說明這個效果

        # 他前往那個URL 他的待辦清單仍然在那裡

        # 他很滿意的上床睡覺

if __name__ == '__main__':
    unittest.main(warnings='ignore')
