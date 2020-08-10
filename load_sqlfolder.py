#!/usr/bin/python3
# -*- coding:utf-8 -*-

import subprocess
import time
import json
import os
import logging
import sys


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    while True:
        run()

def run():
    # 导航信息
    print("=============================")
    print("3  = 刷入 mystest 3")
    print("5  = 刷入 mystest 5")
    print("6  = 刷入 mystest 6")
    print("7  = 刷入 mystest 7")
    print("1  = 刷入 mystest 1")
    print("2  = 刷入 mystest 2")
    print("8  = 刷入 mystest 8")
    print("14 = 刷入 mystest 14")
    print("15 = 刷入 mystest 15")
    print("16 = 刷入 mystest 16")
    print("0 = 退出")
    print("=============================")

    key = input()

    if key == "0":
        sys.exit()

    # 按键设置
    server_key = {"3": "test03", "5": "test05", "6": "test06", "7": "test07", "1": "test01", "2": "test02", "8": "test08", "14": "test14", "15": "test15", "16": "test16"}
    try:
        server_name = server_key[key]
    except KeyError:
        logging.error("无效的输入，请重新输入。")
        return

    config_path = './config/config.json'

    # 读取配置文件
    with open(config_path) as data_file:
        data = json.load(data_file)

    ip = data["database"][server_name]["ip"]
    user = data["database"][server_name]["user"]
    password = data["database"][server_name]["password"]
    port = data["database"][server_name]["port"]

    print("=============================")
    print("请输入刷库的sql文件路径")
    print("1.刷入PM_Create.sql")
    print("0 = 退出")
    print("=============================")

    key = input()

    if key == "0":
        sys.exit()
        os.system("cls")
    if key == "1":
        path = r'D:\SVN\脚本开发\3dmy_tools\lua_to_sql\PM_Create.sql'
        # 刷库
        logging.info("PM_Create.sql正在刷入数据库。")
        # 电脑未安装 mysql，使用 bin 目录中的 mysql.exe
        sql_string = "bin\mysql.exe -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + path
        # 电脑已安装 mysql，使用 path 路径中的 mysql
        # sql_string = "mysql -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + key
        sql_btime = time.time()
        p = subprocess.Popen(sql_string, shell=True, stdout=None)
        p.wait(60)

        sql_etime = time.time()
        if p.returncode == 0:
            logging.info("刷库完成，耗时：%s %s", round(sql_etime - sql_btime, 2), "秒。")
            print('\n')
        else:
            logging.error("刷库出错。")
            print('\n')

    else:
        if not os.path.exists(key):
            print('文件路径不存在，请重新输入。')
            return
        fold = 'null'
        first_load = False
        for root, dirs, files in os.walk(key):
            fold = files
        for name in fold:
            if '建库更新' in name:
                path = os.path.join(key, name)
                print('当前文件为：', name)
                # 刷库
                logging.info("正在刷入数据库。")
                # 电脑未安装 mysql，使用 bin 目录中的 mysql.exe
                sql_string = "bin\mysql.exe -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + path
                # 电脑已安装 mysql，使用 path 路径中的 mysql
                # sql_string = "mysql -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + key
                sql_btime = time.time()
                p = subprocess.Popen(sql_string, shell=True, stdout=None)
                p.wait(60)

                sql_etime = time.time()
                if p.returncode == 0:
                    logging.info("刷库完成，耗时：%s %s", round(sql_etime - sql_btime, 2), "秒。")
                    print('\n')
                else:
                    logging.error("刷库出错。")
                    print('\n')
                break
        for name in fold:
            if '建库更新' not in name:
                path = os.path.join(key, name)
                print('当前文件为：', name)
                # 刷库
                logging.info("正在刷入数据库。")
                # 电脑未安装 mysql，使用 bin 目录中的 mysql.exe
                sql_string = "bin\mysql.exe -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + path
                # 电脑已安装 mysql，使用 path 路径中的 mysql
                # sql_string = "mysql -u" + user + " -p" + password + " -h" + ip + " -P" + port + "<" + key
                sql_btime = time.time()
                p = subprocess.Popen(sql_string, shell=True, stdout=None)
                p.wait(60)

                sql_etime = time.time()
                if p.returncode == 0:
                    logging.info("刷库完成，耗时：%s %s", round(sql_etime - sql_btime, 2), "秒。")
                    print('\n')
                else:
                    logging.error("刷库出错。")
                    print('\n')

if __name__ == '__main__':
    main()
