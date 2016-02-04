from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys

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
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 性感的艾丽听说有一个很酷的待办事项应用
        # 早上，她睁开惺忪的睡眼半裸着酥胸去看了这个应用的首页
        self.browser.get(self.server_url)

        #她抬起修长的手臂伸了个懒腰，注意到网页的标题和头部都包含“To-Do”这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请性感美丽的她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # 她在文本框中输入了购买一套情趣内衣
        # 拥有魔鬼身材的性感的爱丽的一个爱好是穿着骚骚的情趣内衣在镜子前自恋
        inputbox.send_keys('购买一套情趣内衣')

        # 她按下回车键之后，页面更新了
        # 代办事项表格中显示了 “1：购买一套超级性感的情趣内衣”
        inputbox.send_keys(Keys.ENTER)
        aili_list_url = self.browser.current_url
        self.assertRegex(aili_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: 购买一套情趣内衣')
        # 页面中又显示了一个文本框，可以输入其它待办事项
        # 她输入了穿情趣内衣发自拍吸引网友
        # 没错，艾丽就是这么骚！！！
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('穿上情趣内衣发自拍')
        inputbox.send_keys(Keys.ENTER)

        #页面再次更新，清单中显示了这两个代办事项
        self.check_for_row_in_list_table('1: 购买一套情趣内衣')
        self.check_for_row_in_list_table('2: 穿上情趣内衣发自拍')

        #现在一个新用户弗朗西斯访问了网站

        ## 使用一个新浏览器会话
        ## 确保艾丽的信息不会从cookies中泄露出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 弗朗西斯访问首页
        # 页面中看不到艾丽的清单
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('购买', page_text)
        self.assertNotIn('穿上', page_text)

        # 弗朗西斯输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # 弗朗西斯获得了他的唯一URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, aili_list_url)

        # 这个页面还是没有艾丽的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotEqual('买',page_text)
        self.assertIn('Buy milk', page_text)

        # 两个人都很满意，去睡觉了

    def test_layout_and_styling(self):
        # 访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        # 看到输入框居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
