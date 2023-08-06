import unittest

from weixin import WeixinMsg


class TestWeixinMsg(unittest.TestCase):
    def setUp(self):
        self.msg = WeixinMsg('TwigC0des')

    def test_text_reply(self):
        self.assertRegex(self.msg.reply(
            username='test',
            type='text',
            sender='sender',
            content='Hello, world!'
        ),
            "<xml><ToUserName><!\[CDATA\[test]]></ToUserName><FromUserName><!\[CDATA\[sender]]></FromUserName><CreateTime>[0-9]+</CreateTime><MsgType><!\[CDATA\[text]]></MsgType><Content><!\[CDATA\[Hello, world!]]></Content></xml>")

    def test_news_reply(self):
        self.assertRegex(self.msg.reply(
            username='test',
            type='news',
            sender='sender',
            articles=[dict(
                title='Hello, world!',
                description='Hello, world!',
                picurl='http://www.baidu.com/img/bdlogo.gif',
                url='http://www.baidu.com'
            )]
        ),
            "<xml><ToUserName><!\[CDATA\[test]]></ToUserName><FromUserName><!\[CDATA\[sender]]></FromUserName><CreateTime>[0-9]+</CreateTime><MsgType><!\[CDATA\[news]]></MsgType><ArticleCount>1</ArticleCount><Articles><item><Title><!\[CDATA\[Hello, world!]]></Title><Description><!\[CDATA\[Hello, world!]]></Description><PicUrl><!\[CDATA\[http://www\.baidu\.com/img/bdlogo\.gif]]></PicUrl><Url><!\[CDATA\[http://www\.baidu\.com]]></Url></item></Articles></xml>")


if __name__ == '__main__':
    unittest.main()
