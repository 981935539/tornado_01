# coding=utf-8
from handlers.index import IndexHandler, GetPageHandler, LoginHandler
from handlers.up_show_pic import PictureHandler

urls = [
    (r'/', IndexHandler),
    (r'/pic', PictureHandler),
    (r'/get', GetPageHandler),
    (r'/login', LoginHandler)
]