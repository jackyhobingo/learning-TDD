from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
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