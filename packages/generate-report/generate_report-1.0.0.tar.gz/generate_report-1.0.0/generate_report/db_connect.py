# -*- coding: utf-8 -*-
import logging
import pymysql
from itertools import chain


class DBConnect:
    def __init__(self, dbinfo):
        try:
            self.db = pymysql.connect(
                host=dbinfo.get("host"),
                user=dbinfo.get("user"),
                password=dbinfo.get("password"),
                port=dbinfo.get("port"),
                database=dbinfo.get("database")
            )
            self.cursor = self.db.cursor()
            logging.info(f"数据库连接成功,host:{dbinfo.get('host')}")
        except Exception as e:
            logging.error("数据库连接失败!", exc_info=e)

    def select_data(self, sql):
        try:
            self.cursor.execute(sql)
            results = list(chain.from_iterable(self.cursor.fetchall()))
            # results = self.cursor.fetchall()
            # if len(results) == 1:
            #     results = results[0]
            logging.info(f"数据库获取的数据为:{results}")
            return results
        except Exception:
            logging.error("sql语句存在错误!")

    def execute_api(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            logging.info("执行成功!")
        except:
            self.db.rollback()
            logging.error("执行失败，数据回滚!")

    def select_data_list(self, sql):
        """
        将数据库返回的数据转换成二维列表
        ps:数据量较大时可使用
        :param sql: sql语句
        :return: 二维列表
        """
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            li = []
            for it in results:
                new_li = []
                for i in it:
                    new_li.append(i)
                li.append(new_li)
            logging.info(f"数据库获取的数据为:{li}")
            return li
        except:
            logging.error("sql语句存在错误!")

    @property
    def con_sql(self):
        """
        返回类属性
        """
        return self.db

    def __del__(self):
        self.cursor.close()
        self.db.close()
