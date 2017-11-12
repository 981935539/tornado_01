# coding=utf-8

from tornado.testing import AsyncTestCase, gen_test
from tornado.httpclient import AsyncHTTPClient
import unittest

class MyAsyncTest(AsyncTestCase):

    @gen_test
    def test_xx(self):
        client = AsyncHTTPClient(self.io_loop)
        path = "http://localhost:8000/"
        responses = yield [client.fetch(path) for i in range(10)]

        for response in responses:
            print response.body

if __name__ == '__main__':
    unittest.main()