# coding=utf-8
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self):
        self.write("OK")
