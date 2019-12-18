import time

from flask import Flask

app = Flask(__name__)


@app.route('/python/name=<name>andpwd=<pwd>', methods=['POST', 'GET'])
def hello_world(name, pwd):
    print(name)
    return 'Hello {} World!'.format(name + pwd)


print("Starting")
time.sleep(1)
print(hello_world.__name__)
time.sleep(1)
print(hello_world.__doc__)
time.sleep(1)


if __name__ == '__main__':
    print("Starting")
    time.sleep(1)
    print(hello_world.__name__)
    time.sleep(1)
    print(hello_world.__doc__)
    time.sleep(1)
    app.run()
