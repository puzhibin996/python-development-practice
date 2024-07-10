
#函数装饰器
# 装饰器是一个高阶函数，他接受一个函数作为参数，并返回一个新的函数。在编写装饰器时，使用*args 和**kwargs可以确保装饰器能够适用于任何参数签名的函数。
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before")
        result = func(*args,**kwargs)
        print("after")
        return result
    return wrapper


@my_decorator
def demo1(name,age):
    print(f"hello ,{name},you is year{age}")

demo1("puzhibin","214124124")


#参数转发
# 当一个函数需要调用另一函数，并且不修改参数时，使用*args 和 **kwargs 可以方便地转发参数。

def log_and_call(func, *args, **kwargs):
    print(f"Calling {func.__name__} with args:{args} and kwargs:{kwargs}")
    return func(*args, **kwargs)

def add(a,b):
    return a+b

result = log_and_call(add,3,4)
print("等于：",result)


# 通过API接口
# 在设计需要处理各种参数的通用API接口时，*args和**kwargs 可以使接口更加灵活和通用。

class API:
    def request(self,endpoint,*args,**kwargs):
        print(f"Request to {endpoint} with args:{args} and kwargs:{kwargs}")

api = API()
api.request('/users','GET',id=123,include_details=True)