from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith 前往首頁 並且不小心試著提交
        # 一個空的清單項目 他在空的輸入方塊中按下Enter
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # 首頁重新整理 有一個錯誤訊息
        # 說不能有空白的清單項目
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # 他再試一次 在項目中加入一些文字 現在可以動作了
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # 離譜的事 現在他決定要提交第二個空白的清單項目
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # 他在清單網頁上看到類似的警告
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")


        # 他可以填入一些文字來修正他
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')
