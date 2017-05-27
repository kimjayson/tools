#!/usr/bin/python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from .myconfig import *

ITZ_DB_CONNECT_STRING = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(MYSQL_USER,MYSQL_PASS,MYSQL_HOST_M,MYSQL_DB)
itz_engine = create_engine(ITZ_DB_CONNECT_STRING, encoding='utf8', poolclass=NullPool, echo=False)
ITZ_DB_Session = sessionmaker(bind=itz_engine)
itz_session = ITZ_DB_Session()

BBS_DB_CONNECT_STRING = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(BBS_USER,BBS_PASS,BBS_HOST_M,BBS_DB)
bbs_engine = create_engine(ITZ_DB_CONNECT_STRING, encoding='utf8', poolclass=NullPool, echo=False)
BBS_DB_Session = sessionmaker(bind=bbs_engine)
bbs_session = BBS_DB_Session()

GRC_DB_CONNECT_STRING = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(GRC_USER,GRC_PASS,GRC_HOST_M,GRC_DB)
grc_engine = create_engine(GRC_DB_CONNECT_STRING, encoding='utf8', poolclass=NullPool, echo=False)
GRC_DB_Session = sessionmaker(bind=grc_engine)
grc_session = GRC_DB_Session()