# coding=utf-8
from handlers.base import BaseHandler
from tornado.httpclient import AsyncHTTPClient
from tornado import gen, escape


class IndexHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect('/login')
            return
        print self.current_user
        name = escape.xhtml_escape(self.current_user)
        print name
        self.write("hello:%s" % name)

class LoginHandler(BaseHandler):
    """登录处理类"""
    def get(self):
        """返回登录页面"""
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        name = self.get_argument("name")
        if name:
            self.set_secure_cookie("name", name)
            self.redirect('/')
        else:
            self.write("请输入用户名!")


class GetPageHandler(BaseHandler):
    """请求网页处理类"""
    @gen.coroutine
    def get(self):
        """get请求方法"""
        client = AsyncHTTPClient()
        response = yield client.fetch("http://hq.sinajs.cn/list=sz000001")
        self.write(response.body.decode('gbk'))