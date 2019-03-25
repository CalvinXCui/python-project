import  pymysql;#首先需要安装 MySQLdb

def bdbase(self):
    DATABASE = {
        'host' : '127.0.0.1' ,#如果这里是远程数据库，此处则为远程服务器得IP地址
        'database' : 'practice',
        'user' : 'root',
        'password' : 'root',
        'charset' : 'utf8mb4'
    }
    db = pymysql.connect(host="localhost",user="root",password="root",db="practice",charset="utf8mb4")
    #等价于   当不知道顺序的时候  采用上面的即可
    db = pymysql.connect("localhost","root","root","practice","utf8mb4")
    #等价于
    db = pymysql.connect(**DATABASE)#可变参数
    return db

def operationData(self):
    db = bdbase()
    cursor = db.cursor()#游标
    return cursor

'''查询数据库的操作'''
def get_study():
    sql="select * from study"
    cursor = operationData()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results :
        print(row)

'''修改数据库的操作'''
def update_study():
    sql="updata 'study' set 'name'='张天爱'，'age'=26 where 'id'=6"
    cursor = operationData()
    cursor.execute(sql)
    db = bdbase()
    db.commit()

'''增加数据库的操作'''
def insert_study():
    values = "'{}',"*3+"'{}'"
    sql_values = values.format()
    sql ="""
        inset into 'study' ('id' , 'name' ,'age')
        values({})
    """.format(sql_values)
    cursor = operationData()
    cursor.execute(sql)
    db = bdbase()
    db.commit()
'''删除数据库的操作'''
