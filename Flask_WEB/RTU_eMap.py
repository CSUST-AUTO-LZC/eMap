#!/user/python
# coding=utf-8
"""
ProjectName：RTU-emap系统
NAME:RTU管控网页服务器
Author：CSUST-Auto-LZC&Geeks
Date:2019/05/30
ver:1.0
"""

# 导入所需要的功能模块包
from flask import Flask, render_template, request, json
import mysql.connector


# 数据库连接信息
config = {
    "user": "root",
    "password": "csust2019",
    "host": "localhost",
    "database": "test"
         }


app = Flask(__name__)


@app.route('/echartindex', methods=['GET'])
# RTU数据E-chart主页访问路由(即输入以上网址即可访问监控界面主页)
def mysql_getIndex1():
    return render_template("Echart_htmlDoc.html")   #将Templates文件夹下的网页模版返回给游览器


@app.route('/mjpeg', methods=['GET'])
# 智能家居-index主页访问路由(即输入以上网址即可访问监控界面主页)
def mysql_getIndex2():
    return render_template("index.html")   #将Templates文件夹下的网页模版返回给游览器


@app.route('/emapindex', methods=['GET'])
# RTU_eMAP主页访问路由(即输入以上网址即可访问监控界面主页)
def mysql_getIndex3():
    return render_template("emapIndex.html")   #将Templates文件夹下的网页模版返回给游览器


@app.route('/getdata/<name>', methods=['GET', 'POST'])
# 网页获取数据库的数据路由(输入对应网址即可得到数据库中的数据-Json格式数据)
def Html_getdata(name):
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)     # 创建一个游标对象用于执行查询语句时使用

    # 查找数据
    sql_stmt = "SELECT * FROM test.rtudata WHERE name='" + name + "';"    # 设定SQL查询语句：获取数据库中gsmdata的所有数据
    cur.execute(sql_stmt)                       # 执行SQL语句，将获得的查询结果保存在游标对象中

    # To 列表变量数据
    for user_data in cur.fetchall():        # 遍历游标数据中的查询结果并存入列表变量
        result = dict()     # 创建一个字典用于存储查询结果
        result["id"] = str(user_data[0])    # 数据在游标中是按数据中的列顺序排列的
        result["name"] = str(user_data[1])
        result["state"] = str(user_data[2])
        result["longitude"] = str(user_data[3])
        result["latitude"] = str(user_data[4])
        result["height"] = str(user_data[5])
        result["speed"] = str(user_data[6])
        result["direction"] = str(user_data[7])
        result["temp"] = str(user_data[8])
        result["light"] = str(user_data[9])
        result["data1"] = str(user_data[10])
        # print(json.dumps(result))       # 在控制台返回查询的结果供Debug使用，正常时可屏蔽它

        cur.close()     # 关闭游标对象
        cnx.close()     # 关闭与Mysql数据库的连接

        return json.dumps(result)   # 将字典数据转换成Json格式的数据返回给访问端


@app.route('/postdata/<rtuname>&<state>&<data>', methods=['POST', 'GET'])
# 网页端向服务器提交数据并更新到Mysql数据库保存 name：终端名 state:终端工作状态值 angle:舵机角度值
def Html_postdata(rtuname, state, data):
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)             # 创建一个游标对象用于执行SQL语句时使用
    if (state == "1"):
        data1 = "data1+" + data
    else:
        data1 = "data1-" + data

    # 更新数据库数据
    sql_stmt = "UPDATE test.rtudata SET state=%s,data1=%s WHERE name='%s';" % (state, data1, rtuname)  # 设定SQL语句：更改数据库中rtudata的相应数据
    cur.execute(sql_stmt)                       # 执行SQL更新语句
    cnx.commit()                # 提交到数据库执行
    cur.close()     # 关闭游标对象
    cnx.close()     # 关闭与Mysql数据库的连接
    return "Data:{} Recieved: OK!".format("[$Name:" + rtuname + "$State:" + state + "$Data1:" + data1 + "]")


@app.route('/gsmpostdata/<rtuname>&<longitude>&<latitude>&<height>&<speed>', methods=['POST', 'GET'])
# GSM终端向服务器提交数据并更新到Mysql数据库保存 name=终端名 temp:输液温度 data：其它数据
def GSM_postdata(rtuname, longitude, latitude, height, speed):
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)             # 创建一个游标对象用于执行SQL语句时使用

    # GPS数据格式转换与校定处理 11300.14558%20E&2804.40360%20N
    longitudeArry = longitude.split(" ", 1)
    latitudeArry = latitude.split(" ", 1)
    print(longitudeArry)
    print(latitudeArry)

    longitudeValue = float(longitudeArry[0])
    longitudeValue = longitudeValue / 100
    longitudeValuesmall = longitudeValue % 1

    latitudeValue = float(latitudeArry[0])
    latitudeValue = latitudeValue/100
    latitudeValuesmall = latitudeValue % 1

    longitude = int(longitudeValue) + longitudeValuesmall/0.6 + 0.012151  # 偏差补偿
    latitude = int(latitudeValue) + latitudeValuesmall/0.6 + 0.002661 - 0.000132  # 偏差补偿
    print(longitude)
    print(latitude)


    # 更新数据库数据
    sql_stmt = "UPDATE test.rtudata SET longitude=%s,latitude=%s,height=%s,speed=%s WHERE name='%s';" % (longitude, latitude, height, speed, rtuname)  # 设定SQL语句：更改数据库中gsmdata的相应数据
    cur.execute(sql_stmt)               # 执行SQL更新语句
    cnx.commit()                # 提交到数据库执行

    # 查找数据
    sql_stmt = "SELECT * FROM test.rtudata WHERE name='" + rtuname + "';"    # 设定SQL查询语句：获取数据库中gsmdata的所有数据
    cur.execute(sql_stmt)                    # 执行SQL语句，将获得的查询结果保存在游标对象中

    # To 列表变量数据
    for user_data in cur.fetchall():        # 遍历游标数据中的查询结果并存入列表变量
        longitude = str(user_data[3])           # 获取所需的数据经度
        latitude = str(user_data[4])           # 获取所需的数据纬度

    cur.close()         # 关闭游标对象
    cnx.close()         # 关闭与Mysql数据库的连接
    # "Data:{} Recieved: OK!".format("[$Name:" + name + "$State:" + state + "$angle:" + angle + "]")     # 备用返回格式，可忽略
    return "Data:{} Recieved: OK!".format("[$Name:" + rtuname + "$State:" + longitude + "$Data1:" + latitude + "]")   # 返回角度值给GSM终端并以@作为数据起始字符，e作为结束字符供GSM单片机端提取报文中的有效数据angle


@app.after_request
# 以下为防止网页游览器报错的引用代码：主要是配置响应头的，没有也可访问无大碍，只是游览器后台会有一些报错记录     详情参考网址：https://www.jianshu.com/p/212ecf096023
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/')
def Index():
    return render_template("main.html")     # 'Hello! This is Flask Web zone! For CSUST-AUTO-LZC@2019'


if __name__ == '__main__':
    print("RTU运程监控系统网页服务")     # 启动前在控制台输出启动提示信息
    print("Starting")
    app.run(host="0.0.0.0", port=80, debug=False)   # 启动app。即开始运行服务器程序'172.16.11.142'
