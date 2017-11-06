# coding=utf-8
from handlers.index import IndexHandler
from handlers.up_show_pic import PictureHandler

urls = [
            (r'/', IndexHandler),
            (r'/pic', PictureHandler)
        ]