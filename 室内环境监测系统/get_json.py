#读取传感器编号为1的json数据，并绘图
import sys, urllib.request, json
import pandas as pd
import matplotlib.pyplot as plt

a=int(input("请输入传感器编号:"))

if a==1:
    url = 'http://192.168.31.165:8080/get?id=1'
    print("您当前看到的是温度折线图")

else:
    url = 'http://192.168.31.165:8080/get?id=2'
    print("您当前看到的是湿度折线图")

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')

#content=open('new-json.txt').read()
if (content):
    #print(content)
    data = json.loads(content)

    #节点可以这样读出
    print(data['sensorid'])
    val=data["value"]

    #print(val[0])
    df=pd.DataFrame(val)

    #print(df)
    #绘图，默认是折线图
    ax=df.plot()

    #显示图形
    plt.show()
