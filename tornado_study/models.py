# coding=utf-8

from sqlalchemy import create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
import faker
import random

# 连接数据库
# engine = create_engine('postgresql://yang:123456@localhost:5432/exampledb', echo=True)
engine = create_engine('sqlite:////home/python/Databases/test.db')
print engine
Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='author')
    userinfo = relationship('UserInfo', backref='user', uselist=False)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)


class UserInfo(Base):

    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    qq = Column(String(11))
    phone = Column(String(11))
    link = Column(String(64))
    user_id = Column(Integer, ForeignKey('users.id'))


class Article(Base):

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    cate_id = Column(Integer, ForeignKey('categories.id'))
    tags = relationship('Tag', secondary='article_tag', backref='articles')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)
    articles = relationship('Article', backref='category')

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


article_tag = Table(
    'article_tag', Base.metadata,
    Column('article_id', Integer, ForeignKey('articles.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)


class Tag(Base):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)

if __name__ == '__main__':
    # 创建数据表
    Base.metadata.create_all(engine)

    # 创建会话对象，用来操作数据库
    Session = sessionmaker(bind=engine)
    session = Session()

    # 创建一个faker工厂对象,用来产生虚假信息
    # faker = faker.Factory.create()
    faker = faker.Faker()

    # 生成１０个用户
    faker_users = [User(
        # 使用 faker 生成一个人名
        username=faker.name(),
        # 使用 faker 生成一个单词
        password=faker.word(),
        # 使用 faker 生成一个邮箱
        email=faker.email(),
    ) for i in range(10)]
    # add_all 一次性添加多个对象
    session.add_all(faker_users)

    # 生成 5 个分类
    faker_categories = [Category(name=faker.word()) for i in range(5)]
    session.add_all(faker_categories)

    # 生成２０个标签
    faker_tags = [Tag(name=faker.word()) for i in range(20)]
    session.add_all(faker_tags)

    # 生成 100 篇文章
    for i in range(100):
        article = Article(
            # sentence() 生成一句话作为标题
            title=faker.sentence(),
            # 文章内容为随机生成的 10-20句话
            content=' '.join(faker.sentences(nb=random.randint(10, 20))),
            # 从生成的用户中随机取一个作为作者
            author=random.choice(faker_users),
            # 从生成的分类中随机取一个作为分类
            category=random.choice(faker_categories)
        )
        # 从生成的标签中随机取 2-5 个作为分类，注意 sample() 函数的用法
        for tag in random.sample(faker_tags, random.randint(2, 5)):
            article.tags.append(tag)
        session.add(article)
    session.commit()
