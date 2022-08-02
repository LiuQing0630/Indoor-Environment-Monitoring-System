# 室内环境监测系统

#### 介绍
基于micro:bit的开源项目
高中浙教版信息技术必修2-信息系统与社会 项目搭建实例

#### 硬件准备
1.micro:bit V2
https://wiki.dfrobot.com.cn/Micro_bit

2.掌控IO扩展板
https://wiki.dfrobot.com.cn/_SKU_MBT0014_%E6%8E%8C%E6%8E%A7IO%E6%89%A9%E5%B1%95%E6%9D%BF

3.SKU Gravity OBLOQ - IoT Module 物联网模块 
https://wiki.dfrobot.com.cn/_SKU___Gravity__OBLOQ_-_IoT_Module_%E7%89%A9%E8%81%94%E7%BD%91%E6%A8%A1%E5%9D%97_IIC%E7%89%88%E6%9C%AC_

4.Gravity Speech Synthesis module 语音合成模块
https://wiki.dfrobot.com.cn/_SKU_DFR0760_Gravity_Speech_Synthesis_module_V2.0

5.DHT11 数字温湿度传感器
https://wiki.dfrobot.com.cn/_SKU_DFR0067_DHT11%E6%95%B0%E5%AD%97%E6%B8%A9%E6%B9%BF%E5%BA%A6%E4%BC%A0%E6%84%9F%E5%99%A8V2

6.数字大按钮模块
https://wiki.dfrobot.com.cn/_SKU_DFR0029_%E6%95%B0%E5%AD%97%E5%A4%A7%E6%8C%89%E9%92%AE%E6%A8%A1%E5%9D%97_V2

#### 购买店铺
京东:https://shop.m.jd.com/?shopId=195980&gx=RnFiwmAIbTffndRP--txWYP9kujWCmJ52Mfr&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=CopyURL

淘宝:https://m.tb.cn/h.f1eb3R2?sm=b3a63a

#### 软件下载
1.Mind+  http://mindplus.cc/download.html                                                                                                                          
2.Python IDLE https://www.python.org/downloads/                                                                                                                         
3.Google Chrome https://www.google.cn/intl/zh-CN/chrome/

#### 使用教程
硬件接入
1.  将micro:bit插入扩展板[有两个按键的一面对着micro:bit字样]
2.  将IoT模块接在Pin1,Pin2上[黑,红,蓝接Pin1 绿接Pin2]
3.  将两个按钮模块分别接在Pin8,Pin9上
4.  将DHT11模块接在Pin16上
5.  将语音识别模块调至I2C模式 & 接在IIC接口上['+' '-' 'c' 'd'分别对应红 黑 蓝 绿]
6.  连接micro:bit与电脑
![总布置](https://images.gitee.com/uploads/images/2021/0830/094227_ee83d954_9537357.jpeg "IMG_20210830_093454.jpg")
![接口](https://images.gitee.com/uploads/images/2021/0830/094247_b03d3179_9537357.jpeg "微信图片_20210830093659.jpg")
![接入](https://images.gitee.com/uploads/images/2021/0830/094308_e49835a2_9537357.jpeg "IMG_20210830_093426.jpg")

软件设置
1.  用Mind+打开'环境监测.sb3'文件,修改Obloq设置
2.  点击'连接设备',选择Microbit
![输入图片说明](https://images.gitee.com/uploads/images/2021/0830/085818_a332f89a_9537357.png "屏幕截图(6).png")
3.  点击'上传到设备',等待完成.至此,服务端已部署完成.
4.  打开本项目中'室内环境监测系统'文件目录,在当前路径地址栏中直接输入‘cmd’，然后回车
![打开cmd](https://images.gitee.com/uploads/images/2021/0830/090648_f25d9f00_9537357.png "屏幕截图(10).png")
5.  在cmd中输入' Python webapp.py ',即可启动客户端程序.
6.  复制'Running on'后的网址(黄色下划线部分),打开Chrome粘贴并进入,即可进入显示界面.
![打开网页](https://images.gitee.com/uploads/images/2021/0830/091255_acfff8fd_9537357.jpeg "屏幕截图(13)_LI.jpg")
![显示界面](https://images.gitee.com/uploads/images/2021/0830/091648_3d7fe511_9537357.png "屏幕截图(15).png")
7.  若要退出程序,返回cmd界面,按下'CTRL+C'即可.

#### 功能使用
1.在界面内,可查看当前室内温度与湿度                               
2.长按连接Pin8的按键可语音输出当前温度                                
3.长按连接Pin9的按键可语音输出当前湿度                                 
4.在Python IDLE中打开'get_json.py',运行并输入传感器编号即可查看数据折线图       
p.s.温度传感器编号为'1',湿度传感器编号为'2'

#### 困难提示
1.  如何查看电脑IP地址
        一.按下Win+R，输入CMD，按下回车键打开命令行
        二.在命令行中输入IPCONFIG，输入完按下回车键，看到IPv4地址，就是电脑的IP地址
        p.s.若电脑为WiFi连接,则查看'无线局域网适配器'
            若电脑为以太网接入,则查看'以太网适配器'

2.  IoT模块亮灯异常
![亮灯异常说明](https://images.gitee.com/uploads/images/2021/0830/083029_4ba79e61_9537357.png "屏幕截图(4).png")
        
3.  micro:bit运行较长时间后有几率失效,需重新写入程序

####文件作用                                                                                                     
1.setup.py
功能：用于首次使用本系统时运行一次即可，以后无需运行。                                                                           
注意事项：传感器名称与极值修改，通过14、15行。                                                     
2.webapp.py 
功能：用于显示当前数据、增加数据                                                       
（1）显示当前数据：http://0.0.0.0:8080                                                                                      
（2）增加数据格式：http://0.0.0.0:8080/input?id=1&val=22.50                                                                                                                           
     注意：“1”指传感器编号、“22.50”指当前温度（未作容错处理，请用2位小数表示）                                                                                              
     带返回值：超过所设定的极值，返回“1”，否则返回“0”                                                                             
（3）查询数据：                                                                                                                    
    http://0.0.0.0:8080/get?id=1                                                                 
    注意：“1”指传感器编号                                                         
    带返回值：json格式。样例如下：                                               
{                                        
    "sensorid":1,                     
    "value":[                            
            {                       
                "sensorvalue":39,                         
                "updatetime":"2017-05-13 13:34:19"                           
            },                      
            {                          
                "sensorvalue":40.09,                   
                "updatetime":"2017-05-13 13:35:04"                                 
            },                                             
            {                                                 
                "sensorvalue":38.12,                                                    
                "updatetime":"2017-05-13 13:38:02"                                       
            }                                               
        ]                                              
}                                                       

3.data/data.db                                              
功能：数据库文件，运行setup.py自动建立                                                   
4.templates/vews.html                     
功能：用于显示当前数据                          
5.get_json.py                                 
功能：用于读取系统返回的json数据，并且画出折线图。
