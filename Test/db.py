###python链接MySQL数据库
###时间:2021.01.19
###编写人：码农

##安装python链接mysql数据库的接口pymysql，在终端输入：pip install pymysql 
#引用pymysql
import pymysql as pymysql

#------链接数据库说明---------#
#------1.建立链接数据库
#方式1
""" conn=pymysql.connect('localhost','root','123456') """

#方式2：关键字参数
conn=pymysql.connect(host='localhost',user='root',passwd='123456',port=3306,db='test',charset='utf8')

#方式3：字典进行连接参数
""" config={
    host='localhost',
    user='root',
    passwd='123456',
    port=3306,
    db='pythonDB',
    charset='utf8'
}
conn=pymysql.connect(**config) """

#------2.执行数据库操作--------#
cursor=conn.cursor()
sql="select * from user"
cursor.execute(sql)
results=cursor.fetchall()
for row in results:
    print(row)  


#------3.关闭连接--------#
cursor.close() 
conn.close() 




