# -*- encoding: utf-8 -*-
"""
@File    : win_servicer.py
@Time    :  2020/2/13 21:45
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
import io
import os
import sys
import urllib

from app.server import Connect_server, Connect_sftp
from app.server.Windows.resource import Windows

if __name__ == '__main__':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='UTF-8')
    ip = urllib.parse.unquote(sys.argv[1])
    username = urllib.parse.unquote(sys.argv[2])
    password = urllib.parse.unquote(sys.argv[3])

    conn = Connect_server(ip=ip, username=username, password=password)
    ssh = conn.open_server()        # 获得ssh
    win = Windows(ssh=ssh)          # 实例化windows

    path = win.get_path()[0].strip()

    if "True" not in win.command()[0].strip():    # 判断文件是否存在
        conn = Connect_sftp(ip=ip, username=username, password=password)
        sftp = conn.conn_sftp()

        win.put_file(sftp=sftp, path=path)
        conn.close_sftp()   # 关闭连接

    else:

        print(win.command("python winInfo.py"))

    print(win.command("python winInfo.py"))


