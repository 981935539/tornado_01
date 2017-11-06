# coding=utf-8

import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from config import settings, log_path
from urls import urls

tornado.options.define("port", default=8000, type=int, help="start server on this port")


def main():
    tornado.options.options.log_file_prefix = log_path
    tornado.options.parse_command_line()
    app = tornado.web.Application(urls, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
