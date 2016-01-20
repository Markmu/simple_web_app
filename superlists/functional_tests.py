from selenium import webdriver
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
        self.fail('Finish the test!')

        #应用邀请性感美丽的她输入一个待办事项


if __name__ == '__main__':
    unittest.main(warnings='ignore')
