"""
数据库操作
"""
import pymysql


def connect(db):
    """
    连接数据库
    :param db: 数据库相关信息，字典格式
    :return: 连接对象
    """
    host = db['host']
    port = db['port']
    user = db['user']
    pwd = db['pwd']
    name = db['name']
    try:
        # 连接数据库
        conn = pymysql.connect(host=host, port=port, user=user, password=pwd, database=name, charset='utf8')
        print("连接数据库成功")
        return conn
    except Exception as e:
        print(f"连接数据库失败，异常信息：{e}")


def disconnect(conn):
    """
    断开数据库
    :param conn: connect方法返回的连接对象
    :return: 无
    """
    try:
        conn.close()
        print("断开数据库成功")
    except Exception as e:
        print(f"断开数据库失败，异常信息：{e}")


def execute(conn, sql):
    """
    执行sql语句
    :param conn: connect方法返回的连接对象
    :param sql: 要执行的sql语句
    :return: 无
    """
    try:
        c = conn.cursor()  # 获取游标
        c.execute(sql)  # 使用游标执行sql语句
        conn.commit()  # 提交
        c.close()  # 关闭游标
        print(f"执行sql语句成功，sql：{sql}")
    except Exception as e:
        print(f"执行sql语句失败，异常信息：{e}")


def execute_query(conn, sql):
    """
    执行sql语句,查询类
    :param conn: connect方法返回的连接对象
    :param sql: 要执行的sql语句
    :return: 返回查询结果
    """
    try:
        c = conn.cursor()  # 获取游标
        c.execute(sql)  # 使用游标执行sql语句
        conn.commit()  # 提交
        a = c.fetchall()
        c.close()  # 关闭游标
        print(f"执行sql语句成功，sql：{sql}")
        return list(a)
    except Exception as e:
        print(f"执行sql语句失败，异常信息：{e}")


if __name__ == '__main__':
    db = {"host": "192.168.150.54", "port": 3306, "name": "apple", "user": "root", "pwd": "123456"}
    db = {"host": "jy001", "port": 4406, "name": "future", "user": "root", "pwd": "123456"}
    conn = connect(db)
    mobilephone = "18982549778"
    sql = f"delete from member where mobilephone={mobilephone}"
    execute(conn, sql)
    sql = f"select mobilephone from member where mobilephone={mobilephone}"
    a = execute_query(conn, sql)
    print(a)
    disconnect(conn)
