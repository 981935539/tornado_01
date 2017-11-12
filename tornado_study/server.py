# coding=utf-8

import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from config import settings, log_path
from urls import urls
import time

tornado.options.define("port", default=8000, type=int, help="start server on this port")

def count():
    print "1 seconds has gone"

def main():
    tornado.options.options.log_file_prefix = log_path
    tornado.options.parse_command_line()
    app = tornado.web.Application(urls, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)

    # 周期性定时任务, 1秒打印一次
    # tornado.ioloop.PeriodicCallback(count, 1000).start()
    tornado.ioloop.IOLoop.current().start()
    # 单次定时任务
    # ioloop = tornado.ioloop.IOLoop.current()
    # ioloop.call_at(time.time()+5, count)
    # ioloop.start()


if __name__ == '__main__':
    main()
