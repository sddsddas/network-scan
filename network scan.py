#!/bin/usr/python3
#本脚本只对C类网络有用

import socket

hostname=socket.gethostname()
address=socket.gethostbyname(hostname)

class Ip_scan:
    def __init__(self):

        time=0
        result=1
        number=address.rfind('.')
        new_address=address[:number:] + '.'

        while result<=254:

            goal=new_address+str(result)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            if goal ==address:
                result+=1
                continue

            try:
                s.connect((goal,80)) #本行代码如果该IP不存在的话就会报错,接下来执行报错代码
                s.shutdown(2)
                print(goal)
                result+=1
                continue
            except:
                result+=1
                time+=1

                if time == 30:
                    break

                continue

fuzz=Ip_scan()