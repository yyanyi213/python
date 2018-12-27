import requests
import random
from urllib import error

# 打开浏览器请求头 
user_agents = open("user-agents.txt", "r")
headers_list = []
for i in user_agents:
    headers_list.append(i.strip())
# 从user-agents列表中随机读取一个
random_headers = random.choice(headers_list)
headers = {'user-agent': random_headers}

url = input("请输入要扫描的网址:")

# 把字典写入网址后面形成要扫描的网址列表
url_list=[]
try:
    with open ('dicc.txt','r') as f:
        for each in f:
            each = each.replace('\n','')
            url_list.append(each)
except:
    print('打开字典失败')

# 开始扫描
for li in url_list:
    connection = "http://" + url + "/"+ li
    response = requests.get(connection,headers = headers,allow_redirects = False)
# response.status_code
    try:
        print("[+++]%s----------------->%s" % (connection, response.status_code))
    except error.HTTPError as e:
        print("[---]%s----------------->%s" % (connection, e.code))
    except error.URLError:
        print("域名访问失败!")
        exit(1)


