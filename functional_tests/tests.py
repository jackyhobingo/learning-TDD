# Functional test
import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return 
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()


    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard a new cool todo app.
        # She went to look its home page.
        self.browser.get(self.server_url)
        self.browser.get(self.live_server_url)

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

        # 當他按下Enter時,他會被帶到一個新的URL 
        # 現在網頁列出 "1. Buy peacock feathers" 
        # 一個待辦事項清單項目
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # 此時仍然有一個文字方塊讓他可以加入一個項目
        # 她輸入"使用孔雀羽毛來製作一隻蒼蠅" (EDITH非常有條理)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 網頁再次更新 現在他的清單上有這兩個項目
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')


        # 在新的使用者Francis 來到網站

        # 我們使用一個新的瀏覽器工作階段來確保
        ## Edith 的任何資訊都不會被cookies 等機制送出
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # Francis 造訪首頁 沒有任何Edith清單的跡象
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a flys', page_text)

        # Francis 輸入一個新的項目 做出一個新的清單
        # 他比Edith 無趣...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis 取得他自己獨一無二的URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # 同樣的，沒有Edith的清單的任何跡象
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # 他很滿意，都會去睡覺了

        # self.fail('Finish the test!')

        # 他前往那個URL 他的待辦清單仍然在那裡

        # 他很滿意的上床睡覺

    def test_layout_and_styling(self):
        # Edith 前往首頁
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        
        # 他發現輸入方塊已被妥善地置中
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
        # 他開始編輯一個新清單，看到這裡的
        # 輸入欄位也妥善地置中
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

