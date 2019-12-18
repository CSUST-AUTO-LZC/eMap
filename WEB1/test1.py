from flask import Flask, redirect, make_response, render_template


def auth(func):
    print('我在上面')

    def inner(*args, **kwargs):
        return func(*args, **kwargs)

    return inner


app = Flask(__name__)


@app.route('/', methods=['GET'])
@auth  # 注意如果要给视图函数加装饰器，一点要加在路由装饰器下面，才会被路由装饰器装饰
def first_flask():
    response = make_response(render_template('index.html'))
    response.delete_cookie('key')
    response.set_cookie('key', 'value')
    response.headers['X-Something'] = 'A value'
    print('ffff')
    return response


if __name__ == '__main__':
    print(first_flask.__name__)
    app.run()

