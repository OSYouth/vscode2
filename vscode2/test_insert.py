
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("gz-cdb-41jktpwi.sql.tencentcdb.com","outside","lc123456","rankORG", 63055)
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2001)
sql = "INSERT INTO ARWU2018(id, world_rank, insitution, country, reginal_rank, total_score,\
         Alumni, Award, HiCi, NS, PUB, PCP)\
         VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
         (0, '45', 'Mac', 'Mohan','22', 20, 2000, 200, 100, 50)

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
