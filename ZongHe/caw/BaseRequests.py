"""
1、使用session发送请求，自动管理Cookie
2、增加异常处理
3、增加打印日志
"""
import requests


class BaseRequests:
    # 在构造方法中，创建一个session，使用这个瑟斯on发送请求
    def __init__(self):
        self.session = requests.session()

    def get(self, url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            print(f"发送get请求，url：{url}，请求参数：{kwargs}，成功")
            return r
        except Exception as e:
            print(f"发送get请求，url：{url}，请求参数：{kwargs}，异常信息：{e}")

    def post(self, url, **kwargs):
        try:
            r = self.session.post(url, **kwargs)
            print(f"发送post请求，url：{url}，请求参数：{kwargs}，成功")
            return r
        except Exception as e:
            print(f"发送post请求，url：{url}，请求参数：{kwargs}，异常信息：{e}")


if __name__ == '__main__':
    b = BaseRequests()
    r = b.get("http://www.httpbin.org/get?user=root&pwd=123456")
    print(r.text)
    r = b.post("http://www.httpbin.org/post", data={"user": "root"})
    print(r.text)
    r = b.get("http://dqz:0090")
