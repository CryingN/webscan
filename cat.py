#!/bin/python
#by:CryingN
#这里是一个简单的筛选数据脚本,通过for循环与判别式筛选可使用的类型库,并将结果保存在path路径上.

path = "/home/root_cn/python/webscan/data"
datas = open("{path}/list.txt".format(path=path),"r")
php = open("{path}/php_data".format(path=path),"w")
sql = open("{path}/sql_data".format(path=path),"w")
js = open("{path}/js_data".format(path=path),"w")
py = open("{path}/py_data".format(path=path),"w")
log = open("{path}/log_data".format(path=path),"w")
for data in datas:
    if "php" in data:
        php.write(data)
        pass
    elif "sql" in data or "SQL" in data or "db" in data:
        sql.write(data)
        pass
    elif "jsp" in data:
        js.write(data)
        pass
    elif "py" in data:
        py.write(data)
        pass
    elif "log" in data:
        log.write(data)
        pass
    else:
        print(data)
        pass


