
#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect("gz-cdb-41jktpwi.sql.tencentcdb.com","outside","lc123456","rankORG", 63055)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS ARWU2018")
 
# 使用预处理语句创建表
sql = """CREATE TABLE ARWU2018 (
         id INT NOT NULL,
         world_rank CHAR(10),
         insitution CHAR(50),  
         country CHAR(30),
         reginal_rank CHAR(10),
         total_score FLOAT,
         Alumni FLOAT,
         Award FLOAT,
         HiCi FLOAT,
         NS FLOAT,
         PUB FLOAT,
         PCP FLOAT )"""
 
cursor.execute(sql)
 
# 关闭数据库连接
db.close()
