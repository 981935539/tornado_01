# coding=utf-8

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        pass

    def set_default_headers(self):
        pass