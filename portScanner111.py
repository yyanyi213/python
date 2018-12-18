# python端口扫描器
import re
import socket
import sys
import threading


def analysis_host(host):  # 将域名解析为点分十六进制并返回
    pattern = re.compile(r'\d{1-3}\.\d{1-3}\.\d{1-3}\.\d{1-3}')
    match = pattern.match(host)
    if match:
        return(match.group())
    else:
        return(socket.gethostbyname(host))


def analysis_port(port):  # 数组形式返回需要扫描的端口列表
    pattern = re.compile(r'(\d+)-(\d+)')
    match = pattern.match(port)
    if match:
        start_port = int(match.group(1))
        end_port = int(match.group(2))
        return([x for x in range(start_port, end_port + 1)])
    else:
        return([int(x) for x in port.split(',')])


def scanner(host, port):  # 扫描
    # AFINET--IPV4  SOCK_STREAM---TCP   0--自动协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.settimeout(5)
    try:
        s.connect((host, port))
        print('+++端口%s打开' % port)
    except socket.timeout:
        print('---端口%s关闭' % port)


def main():
    host = input('请输入需要扫描的网址，域名: ')
    port = input('请输入端口，格式如 1-100 ，或者20,21,8080,9200: ')
    host = analysis_host(host)
    port = analysis_port(port)
    for single_port in port:
        t = threading.Thread(target=scanner, args=(host, single_port))  # 多线程扫描
        t.start()

if __name__ == '__main__':
    main()
