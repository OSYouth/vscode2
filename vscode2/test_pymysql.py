# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="localhost", user='root',password='lc12345678',database='world',charset='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print ("Database version : %s " % data)

cursor.execute("Drop table if exists user2")
# 定义要执行的SQL语句
sql = """
CREATE TABLE USER2 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""
print(sql)
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()