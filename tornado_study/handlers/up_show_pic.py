# coding=utf-8

from handlers.base import BaseHandler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Picture
import base64


class PictureHandler(BaseHandler):
    def get(self):
        self.render("up_pic.html")

    def post(self):
        # 获取图片对象
        imgae = self.request.files["pic"][0]
        if imgae:
            img_name = imgae.filename
            img_data = imgae.body
            # 保存图片文件
            with open("./statics/images/"+img_name, "wb") as f:
                f.write(img_data)

            # 把图片保存进数据库
            # 连接数据库
            engine = create_engine('postgresql://yang:123456@localhost:5432/exampledb', echo=True)
            # 创建会话对象，用来操作数据库
            Session = sessionmaker(bind=engine)
            session = Session()
            img_data = base64.b64encode(img_data)
            pic = Picture(name=img_name, imge=img_data)
            session.add(pic)
            session.commit()
        self.render("pic_show.html", name=img_name)