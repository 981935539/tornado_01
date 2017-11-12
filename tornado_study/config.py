# coding=utf-8

import os

# Application配置参数

settings = dict(
    debug=True,
    static_path = os.path.join(os.path.dirname(__file__), "statics"),
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    cookie_secret = "sjfkdsjfksldjfklsdj9ewohriew",
    # xsrf_cookies = True
)

# logs
log_path = os.path.join(os.path.dirname(__file__), "logs/log")