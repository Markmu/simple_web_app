from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #性感的艾丽听说有一个很酷的待办事项应用
        #早上，她睁开惺忪的睡眼半裸着酥胸去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        #她抬起修长的手臂伸了个懒腰，注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #应用邀请性感美丽的她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # 她在文本框中输入了购买一套情趣内衣
        # 拥有魔鬼身材的性感的爱丽的一个爱好是穿着骚骚的情趣内衣在镜子前自恋
        inputbox.send_keys('购买一套超级性感的情趣内衣')

        # 她按下回车键之后，页面更新了
        # 代办事项表格中显示了 “1：购买一套超级性感的情趣内衣”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: 购买一套超级性感的情趣内衣' for row in rows),
                'New to-do item did not appear in table'
        )

        # 页面中又显示了一个文本框，可以输入其它待办事项
        # 她输入了穿情趣内衣发自拍吸引网友
        # 没错，艾丽就是这么骚！！！
        self.fail('Finish the test!')

        # 页面再次更新，她的清单中显示了这两个待办事项
        # ......

if __name__ == '__main__':
    unittest.main(warnings='ignore')
