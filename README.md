中控指纹识别考勤终端iClock660越权下载系统数据库测试情况

由于本单位使用中控指纹识别考勤终端型号iClock660进行打卡，对该考勤终端进行研究，发现存在越权下载系统数据库问题
![image](https://github.com/rabbitsafe/iClock660/blob/main/1.jpg)
 
中控指纹识别考勤终端iClock660是中控科技推出的一款3.5寸彩屏指纹考勤机，该款产品在原来3.5寸彩屏考勤产品的基础上增加了摄像头拍照功能，内置130万像素高清摄像头，可以轻松实现员工照片拍摄和显示，标准的TCP/IP通讯，无缝连接网络,公对私的短消息功能、用户可自定义的定时响铃,其高贵典雅的外观设计必将注定又是考勤领域的一枝新秀。指纹门禁考勤设备是一种具备远程控制的物联网设备，设备本身集成人员进出管理、考勤统计、门禁门磁控制等多种功能于一身；指纹门禁考勤设备本身可通过配套的相关软件进行人员管理、考勤管理等。指纹门禁考勤系统的组成基于软硬件功能组合形成，系统既能完成人员签到，保证内部人员的进出自由；也能通过控制门磁门禁杜绝外来人员随意进出。

一、本地测试：

中控指纹识别考勤终端型号iClock660系统目录/form/下的DataApp文件中style变量权限设置存在问题，不需要登录后台，可直接备份下载系统数据库文件data.dat

中控智慧（中控科技）ZKeco/ZKSoftware指纹门禁考勤打卡设备，默认IP地址192.168.1.201，根据对指纹识别中控考勤终端iClock660设备的开放端口分析，相关设备开放端口如下：
端口                 对应服务
TCP/23	              Telnet
TCP/80	              WEB服务
TCP/4370             中控管理软件私有通讯协议端口
UDP/4370	          中控智慧私有协议通讯端口
UDP/65535	          中控智慧私有协议用于局域网广播

URL：http://192.168.1.201/
使用默认管理员1，默认口令123456，攻击者可登录WEB系统，抓取系统备份处存在下载系统数据库文件data.dat的数据包，经过验证，在不登录的情况下，提交该数据包下载系统数据库文件data.dat
数据包如下：
![image](https://github.com/rabbitsafe/iClock660/blob/main/2.png) 
![image](https://github.com/rabbitsafe/iClock660/blob/main/3.png) 
 
2.rar解压出来的文件重命名为22.rar，再对22.rar进行解压，获得系统数据库文件ZKDB.db
![image](https://github.com/rabbitsafe/iClock660/blob/main/4.png)  
该文件属于系统数据库文件，该系统使用的SQLite数据库，使用SQLite数据库管理软件可打开ZKDB.db文件
![image](https://github.com/rabbitsafe/iClock660/blob/main/5.png)  
可以查看指纹识别中控考勤终端iClock660所有数据内容
![image](https://github.com/rabbitsafe/iClock660/blob/main/6.png)  
指纹识别中控考勤终端iClock660开放4370端口

TCP/4370  中控管理软件私有通讯协议端口，可以使用中控管理软件进行连接
![image](https://github.com/rabbitsafe/iClock660/blob/main/7.png)  
默认4370端口连接密码是空，可以通过系统数据库文件data.dat获取连接密码，该设备修改的连接密码是666666
![image](https://github.com/rabbitsafe/iClock660/blob/main/8.png)  
![image](https://github.com/rabbitsafe/iClock660/blob/main/9.png)  
可控制该设备重启、关机、恢复出厂设置，可对人员数据进行管理等操作
![image](https://github.com/rabbitsafe/iClock660/blob/main/10.png)  

二、互联网测试

通过fofa.info进行搜索，使用关键字banner="ZK" && protocol="http" && server=="ZK Web Server"，发现存在2.5万多个IP，使用了中控智慧（中控科技）ZKeco/ZKSoftware指纹门禁考勤打卡设备，开放了WEB服务。
![image](https://github.com/rabbitsafe/iClock660/blob/main/11.png)   

针对该漏洞编写了POC脚本，该脚本可直接下载数据库文件
 

使用pocsuite3，编写了批量验证漏洞EXP的POC脚本
 

使用编写的漏洞EXP对fofa.info搜索的结果进行测试，批量测试过程截图如下：
![image](https://github.com/rabbitsafe/iClock660/blob/main/12.png)   

发现互联网大量系统存在漏洞，部分存在漏洞的URL如下：
![image](https://github.com/rabbitsafe/iClock660/blob/main/13.png)  

1、案例一
http://103.122.67.220/csl/login
![image](https://github.com/rabbitsafe/iClock660/blob/main/14.png)   
使用down-exp.py下载系统数据库文件data.dat
![image](https://github.com/rabbitsafe/iClock660/blob/main/15.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/16.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/17.png)   
管理员帐号是1，密码是123，成功登录WEB系统后台
![image](https://github.com/rabbitsafe/iClock660/blob/main/18.png)   

2、案例二
http://37.25.35.123/csl/login
![image](https://github.com/rabbitsafe/iClock660/blob/main/19.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/20.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/21.png)   
管理员帐号是1，密码是285414，成功登录WEB系统后台
![image](https://github.com/rabbitsafe/iClock660/blob/main/22.png)   

3、案例二
http://69.57.237.245/csl/login
![image](https://github.com/rabbitsafe/iClock660/blob/main/23.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/24.png)   
![image](https://github.com/rabbitsafe/iClock660/blob/main/25.png)   
管理员帐号是2，密码是9262，成功登录WEB系统后台
![image](https://github.com/rabbitsafe/iClock660/blob/main/26.png)   

