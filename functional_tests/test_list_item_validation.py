from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith 前往首頁 並且不小心試著提交
        # 一個空的清單項目 他在空的輸入方塊中按下Enter

        # 首頁重新整理 有一個錯誤訊息
        # 說不能有空白的清單項目

        # 他再試一次 在項目中加入一些文字 現在可以動作了

        # 離譜的事 現在他決定要提交第二個空白的清單項目

        # 他在清單網頁上看到類似的警告

        # 他可以填入一些文字來修正他
        self.fail("write me!")

