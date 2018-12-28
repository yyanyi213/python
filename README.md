# python
python编程小测试

一、编写一个端口扫描器(难度：中等)
    
    C:\Users\Administrator\python\port_scanner>python portScanner111.py
    请输入需要扫描的网址，域名: www.baidu.com
    请输入端口，格式如 1-100 ，或者20,21,8080,9200: 1-10
    ---端口10关闭
    ---端口9关闭
    ---端口7关闭
    ---端口5关闭
    ---端口3关闭
    ---端口1关闭
    ---端口6关闭
    ---端口2关闭
    ---端口4关闭
    ---端口8关闭

二、编写一个网站的目录、文件扫描器（类似御剑）（难度：中等）
    
    扫描速度很慢。
    使用了dirsearch的字典，将dicc.txt和user-agents.txt和dirsearchClone.py放在同一个目录下：
    
    C:\Users\Administrator\python\my_dirsearch>python dirSearchClone222.py
    请输入要扫描的网址:www.baidu.com
    [+++]http://www.baidu.com/!.gitignore----------------->302
    [+++]http://www.baidu.com/!.htaccess----------------->302
    [+++]http://www.baidu.com/!.htpasswd----------------->302
    [+++]http://www.baidu.com/%20../----------------->302
    [+++]http://www.baidu.com/%2e%2e//google.com----------------->302
    
    
三、编写一个简单的爬虫（难度：较难）
    
    使用scrapy爬虫框架
    将wiki.ioin.in第一页的数据存入mysql数据库，数据库配置如下：
    host='localhost',
    port=3306,
    db='secnewsdb', 
    user = 'root',
    passwd='root', 
    charset='utf8', 
    
    然后执行:
    C:\Users\Administrator\python\secnews_scrapy\secnews\spiders>scrapy crawl ioinspider
    
    数据已存入数据库中。
    
    
  
    
