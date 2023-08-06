import unittest

from weixin.mp import WeixinMP


class TestWeixinMP(unittest.TestCase):
    def setUp(self):
        self.mp = WeixinMP('wxa8d4fa7f869317b7',
                           '4536fbddf0d7c07252320bb30af7808b')

    def test_get_access_token(self):
        self.mp
        self.assertIsNotNone(self.mp.access_token)

    def test_get_jsapi_ticket(self):
        self.mp.get_jsapi_ticket()
        self.assertIsNotNone(self.mp.jsapi_ticket)


if __name__ == '__main__':
    unittest.main()
