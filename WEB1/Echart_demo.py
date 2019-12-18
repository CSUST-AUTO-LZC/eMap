#!/user/python
'''

'''
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
#
def mysql_getdata():
    # 建立连接
    cnx = mysql.connector.connect(**config)     # 根据给定的config数据库信息与mysql数据库建立连接
    cur = cnx.cursor(buffered=True)     # 创建一个游标对象用于执行查询语句时使用

    # 查找数据
    sql_stmt = "SELECT * FROM test.gsmdata;"    # 设定SQL查询语句：获取数据库中gsmdata的所有数据
    cur.execute(sql_stmt)                       # 执行SQL查询语句，将获得的查询结果保存在游标对象中

    # To Json_data数据
    for user_data in cur.fetchall():        # 遍历游标数据中的查询结果并存入列表变量
        result = dict()     # 创建一个字典用于存储查询结果
        result["id"] = str(user_data[0])    # 数据在游标中是按数据中的列顺序排列的
        result["name"] = str(user_data[1])
        result["state"] = str(user_data[2])
        result["temp"] = str(user_data[3])
        result["angle"] = str(user_data[4])
        result["data"] = str(user_data[5])
        print(json.dumps(result))
    cur.close()     # 关闭与Mysql数据库的连接
    cnx.close()     # 关闭游标对象

    if request.method == 'POST':
        data = request.get_data().decode('utf-8')
        data = json.loads(data)
        print(data)

    return json.dumps(result)


@app.route('/postdata/<name>&<state>&<angle>', methods=['POST', 'GET'])
def Html_postdata(name, state,  angle):
    # 建立连接
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)

    # 查找数据
    sql_stmt = "UPDATE test.gsmdata SET state=%s,angle=%s WHERE name='%s';" % (state, angle, name)
    cur.execute(sql_stmt)
    cnx.commit()
    cur.close()
    cnx.close()
    return "Data:{} Recieved: OK!".format("[$Name:" + name + "$State:" + state + "$angle:" + angle+"]")


@app.route('/gsmpostdata/<name>&<temp>&<data>', methods=['POST', 'GET'])
def GSM_postdata(name, temp, data):
    # 建立连接
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor(buffered=True)

    sql_stmt = "SELECT * FROM test.gsmdata;"
    cur.execute(sql_stmt)

    # To Json_data数据
    for user_data in cur.fetchall():
        state = str(user_data[2])
        angle = str(user_data[4])

    # 更新数据
    sql_stmt = "UPDATE test.gsmdata SET temp=%s,data=%s WHERE name='%s';" % (temp, data, name)
    cur.execute(sql_stmt)
    cnx.commit()
    cur.close()
    cnx.close()
    return "Data:{} Recieved: OK!".format("[$Name:" + name + "$State:" + state + "$angle:" + angle+"]")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    # 这里不能使用add方法，否则会出现 The 'Access-Control-Allow-Origin' header contains multiple values 的问题
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    print("Starting")
    app.run('172.16.252.183', 80)
