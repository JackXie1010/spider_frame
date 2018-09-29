# coding: utf8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Text, Integer
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'model.db'))   # 保存为sqllite 的db 文件， model.db为文件名
# engine = create_engine('mysql://root:root@localhost/xzj?charset=utf8', pool_size=100)   # 保存至mysql
Base = declarative_base(bind=engine)


# Model为数据库名，如果修改了数据库名请在save_config.py 文件的save_as_db（）中用Model 的地方做出相应修改，请在，insterest_img 为表明
class Model(Base):
    __tablename__ = 'insterest_img'      # insterest_img  为数据表名
    lid = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    img = Column(String(90), nullable=False)

