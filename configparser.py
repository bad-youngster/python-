import configparser
start = configparser.ConfigParser()
start.read("config.ini")
section = start.section()
print(section)
options = start.options('mysqld')
print('options')
options1 = start.options('count')
items = start.items('mysqld')
items1 = start.items('count')
print (items)
print (items1)

host = start.get("mysqld","host")
port = start.get("mysqld","port")
user = start.get("mysqld","user")
password = start.get("mysqld","password")

print(host)
print(port)
print(user)
print(password)
'''
start.add_section("add")
添加[add]
start.write(open("config.ini","w"))
写入到配置文件里
'''

if start.has_section("add"):
	print("already add")
else:
	print("not add ")
	start.add_section("add")
	start.set("add","name","test")
	start.write(open("config.int","w"))


if start.has_section("del"):
	print("already del")
else:
	print("not del ")
	start.remove_section("del")
	print("delete success")
	start.write(open("config.int","w"))


'''
start.remove_option("count","count_num")
删除[count]的count_num类数据
start.write(open("config.int","w"))
写入到配置文件
'''

if  start.del_option("count","count_num"):
	print("if count_num,new delete")
	start.remove_option("count","count_num")
	start.write(open("config.ini","w"))
	print("delete count_num")
else:
	print("not count_num")

'''
start.set("count","count_num","22")
start.write(open("config.int","w"))
'''
if start.new_section("count","count_num","2"):
	start.set("count","count_num","22")
	start.write(open("config.ini","w"))
else:
	print("error")
