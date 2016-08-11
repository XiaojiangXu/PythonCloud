# -*- coding:utf-8 -*-

import sys, os
import multiprocessing
import logging
import random
import time, datetime
import MySQLdb
from MySQLdb import cursors
from pymongo import MongoClient

class Config:
    #tables = ['hs_card', 'hs_hero', 'hs_set', 'hs_skill', 'hs_level', 'hs_pack', 'hs_salesevent']
    tables = ['user']
    index = {
             'user': ['userId'],
    }

class Mysql2Mongo(object):
    mysql_host = 'localhost'
    mysql_port = 3306
    mysql_user = "root"
    mysql_pass = "root"
    mysql_db = "sshdemo"

    mongo_host = 'localhost'
    mongo_port = 2222

    conn = None
    cursor = None
    mongo = None
    mongodb = None

    def __init__(self, logger):
        self.logger = logger

        self.conn = self.getMysqlConn()
        self.cursor = self.conn.cursor()

        self.mongo = MongoClient(host=self.mongo_host, port=self.mongo_port)
        self.mongodb = self.mongo['sshdemo']



    def getMysqlConn(self):
        return MySQLdb.connect(host=self.mysql_host, port=self.mysql_port, user=self.mysql_user, \
                 passwd=self.mysql_pass, db=self.mysql_db, cursorclass=MySQLdb.cursors.SSCursor)


    def setMongoCollectionDocument(self, table, data):
        if(isinstance(data, dict) == False):
            return False
        else:
            self.mongodb[table].insert(data)


    def getMysqlTableDesc(self, table):
        sql = """desc %s""" % (table)
        n = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        keys = []
        types = []
        for row in data:
            key = str(row[0])
            if(row[1].find('int') >= 0):
                type = 1

            elif (row[1].find('char') >= 0):
                type = 2
            elif (row[1].find('text') >= 0):
                type = 2
            elif(row[1].find('decimal') >= 0):
                type = 3
            else:
                type = 2
            keys.append(key)
            types.append(type)
        return keys, types

    def mysql2Mongo(self, table):
        self.mongodb[table].drop()
        keys, types = self.getMysqlTableDesc(table)

        sql = """select * from  %s order by userId asc""" % (table)
        n = self.cursor.execute(sql)
        data = self.cursor.fetchall()
        #print table, keys, types
        for row in data:
            ret = {}
            for k, key in enumerate(keys):
                if key == 'userId':
                    key = '_id'
                    #ret[key] = int(row[k])
                if(types[k] == 1):
                    if row[k]==None:
                        ret[key]= 0
                        continue
                    #print k, key, row
                    ret[key] = int(row[k])
                elif(types[k] == 2):
                    if row[k]==None:
                        ret[key]= ''
                        continue
                    ret[key] = str(row[k])
                elif(types[k] == 3):
                    if row[k]==None:
                        ret[key]= ''
                        continue
                    ret[key] = float(row[k])
                else:
                    if row[k]==None:
                        ret[key]= ''
                        continue
                    ret[key] = str(row[k])
            #if(table== 'hs_card') or (table== 'hs_hero'):
                #ret['rand'] = random.random()
            print ret
            self.setMongoCollectionDocument(table, ret)



    def __del__(self):
        self.mongo.close()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)

    # args = sys.argv
    t1 = time.time()
    cls = Mysql2Mongo(logger)
    for tb in Config.tables:
        cls.mysql2Mongo(tb)
        
    #index    
    for t, f in Config.index.items():
        pass
    
    print time.time() - t1
    logger.info("done")
