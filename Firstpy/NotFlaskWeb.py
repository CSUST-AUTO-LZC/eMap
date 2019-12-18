import time


class NotFlask:
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        def decorator(f):
            self.routes[route_str] = f
            return f

        return decorator

    def serve(self, path):
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            print('Route "{}" has not been registered'.format(path))
            raise ValueError('Route "{}" has not been registered'.format(path))


app = NotFlask()


@app.route("/A")
def hello():
    print("My name is Python !")
    return "Hello World!"


@app.route("/B")
def byb():
    print("Nice to meet you! ,World.")
    return "Bye Bye!"


print(app.serve("/A"))
time.sleep(1)
print(app.serve("/B"))
time.sleep(1)
print(app.serve("/C"))
