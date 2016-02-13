from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 艾丽范文首页，不小心提交了一个空待办事项
        # 输入框中没输入内容，她就按下了回车键
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # 首页刷新了，显示了一个错误消息
        # 提示待办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can\'t have an empty list item.')

        # 她输入一些文字，然后再次提交，这次没问题了
        self.get_item_input_box().send_keys('some words\n')
        self.check_for_row_in_list_table('1: some words')

        # 她贱不索索的又提交了一个空的待办事项
        self.get_item_input_box().send_keys('\n')

        # 在清单页面她看到了一个类似的错误消息
        self.check_for_row_in_list_table('1: some words')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'You can\'t have an empty list item.')
        # 输入文字之后就没有问题了
        self.get_item_input_box().send_keys('some other words\n')
        self.check_for_row_in_list_table('1: some words')
        self.check_for_row_in_list_table('2: some other words')

    def test_cannot_add_duplicate_items(self):
        # 艾丽访问首页，新建一个清单
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('shopping\n')
        self.check_for_row_in_list_table('1: shopping')

        # 她不小心输入了一个重复的待办事项
        self.get_item_input_box().send_keys('shopping\n')

        # 她看到一条有帮助的错误消息
        self.check_for_row_in_list_table('1: shopping')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You've already got this in your list.")
