# -*- coding:utf-8 -*-
import cx_Oracle

#打开db文件，获得连接
conn = cx_Oracle.connect('zbbsmz_test','smzSMZ123','192.168.71.171/orcl')
#conn = cx_Oracle.connect('zbbsmz_test/smzSMZ123@192.168.71.171/orcl')
print conn.version
#获得游标
c = conn.cursor()
#执行SQL
c.execute('select sfzh from T_RY_JBXX')
#c.execute('select sysdate from dual')
rows = c.fetchall()
for row in rows:
    #print "%d, %s, %s, %s" %(row[0], row[1], row[2], row[3])
    print row
print "Number of rows returned: %d" %c.rowcount
#如果有对数据的修改操作，那就需要commit一下
conn.commit()
#关闭游标
c.close()
#关闭连接
conn.close()