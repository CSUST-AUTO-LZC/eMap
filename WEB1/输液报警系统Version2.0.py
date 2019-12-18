#!/user/python
# coding=utf-8
"""
ProjectName：输液报警系统
NAME:管理控制网页服务器
Author：CSUST-Auto-LZC
Date:2019/05/03
ver:2.0
"""

# 导入所需要的功能模块包
from flask import Flask, render_template, request, json
import mysql.connector


# 数据库连接信息
config = {
    "user": "root",
    "password": "18390927803",
    "host": "localhost",
    "database": "test"
         }


app = Flask(__name__)


@app.route('/index', methods=['GET'])
# 服务器主页访问路由(即输入以上网址即可访问监控界面主页)
def mysql_getIndex():
    return render_template("Echart_htmlDoc.html")   #将Templates文件夹下的网页模版返回给游览器


@app.route('/getdata', methods=['GET', 'POST'])
# 获取数据库的数据路由(输入对应网址即可得到数据库中的数据-Json格式数据)
def mysql_getdata():
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)     # 创建一个游标对象用于执行查询语句时使用

    # 查找数据
    sql_stmt = "SELECT * FROM test.gsmdata;"    # 设定SQL查询语句：获取数据库中gsmdata的所有数据
    cur.execute(sql_stmt)                       # 执行SQL语句，将获得的查询结果保存在游标对象中

    # To 列表变量数据
    for user_data in cur.fetchall():        # 遍历游标数据中的查询结果并存入列表变量
        result = dict()     # 创建一个字典用于存储查询结果
        result["id"] = str(user_data[0])    # 数据在游标中是按数据中的列顺序排列的
        result["name"] = str(user_data[1])
        result["state"] = str(user_data[2])
        result["temp"] = str(user_data[3])
        result["angle"] = str(user_data[4])
        result["data"] = str(user_data[5])
        # print(json.dumps(result))       # 在控制台返回查询的结果供Debug使用，正常时可屏蔽它

    cur.close()     # 关闭游标对象
    cnx.close()     # 关闭与Mysql数据库的连接

    return json.dumps(result)   # 将字典数据转换成Json格式的数据返回给访问端


@app.route('/postdata/<name>&<state>&<angle>', methods=['POST', 'GET'])
# 网页端向服务器提交数据并更新到Mysql数据库保存 name：终端名 state:终端工作状态值 angle:舵机角度值
def Html_postdata(name, state,  angle):
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)             # 创建一个游标对象用于执行SQL语句时使用

    # 更新数据库数据
    sql_stmt = "UPDATE test.gsmdata SET state=%s,angle=%s WHERE name='%s';" % (state, angle, name)  # 设定SQL语句：更改数据库中gsmdata的相应数据
    cur.execute(sql_stmt)                       # 执行SQL更新语句
    cnx.commit()                # 提交到数据库执行
    cur.close()     # 关闭游标对象
    cnx.close()     # 关闭与Mysql数据库的连接
    return "Data:{} Recieved: OK!".format("[$Name:" + name + "$State:" + state + "$angle:" + angle+"]")


@app.route('/gsmpostdata/<name>&<temp>&<data>', methods=['POST', 'GET'])
# GSM终端向服务器提交数据并更新到Mysql数据库保存 name=终端名 temp:输液温度 data：其它数据
def GSM_postdata(name, temp, data):
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)             # 创建一个游标对象用于执行SQL语句时使用

    # 查找数据
    sql_stmt = "SELECT * FROM test.gsmdata;"    # 设定SQL查询语句：获取数据库中gsmdata的所有数据
    cur.execute(sql_stmt)                    # 执行SQL语句，将获得的查询结果保存在游标对象中

    # To 列表变量数据
    for user_data in cur.fetchall():        # 遍历游标数据中的查询结果并存入列表变量
        state = str(user_data[2])           # 获取所需的数据state
        angle = str(user_data[4])           # 获取所需的数据angle

    # 更新数据库数据
    sql_stmt = "UPDATE test.gsmdata SET temp=%s,data=%s WHERE name='%s';" % (temp, data, name)      # 设定SQL语句：更改数据库中gsmdata的相应数据
    cur.execute(sql_stmt)               # 执行SQL更新语句
    cnx.commit()                # 提交到数据库执行
    cur.close()         # 关闭游标对象
    cnx.close()         # 关闭与Mysql数据库的连接
    #"Data:{} Recieved: OK!".format("[$Name:" + name + "$State:" + state + "$angle:" + angle + "]")     # 备用返回格式，可忽略
    return "@"+angle+"e"      # 返回角度值给GSM终端并以@作为数据起始字符，e作为结束字符供GSM单片机端提取报文中的有效数据angle

# 以下为防止网页游览器报错的引用代码：主要是配置响应头的，没有也可访问无大碍，只是游览器后台会有一些报错记录     详情参考网址：https://www.jianshu.com/p/212ecf096023
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    print("输液报警系统网页服务")     # 启动前在控制台输出启动提示信息
    print("Starting")
    app.run('172.16.252.183', 80)   # 启动app。即开始运行服务器程序
