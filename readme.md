# 个人博客

博客已经能够部署，创建虚拟环境后按requirements.txt里安装所需环境即可运行，但由于个人水平过低，不知道怎么部署到国内的服务器上，运行速度也不快。打开一个网页需要1S-2S左右。

## 所用环境

* python3.6
* django2.2
* ubuntu18.04
* bootstrap3
* 其他的环境配置请看requirements.txt

## 参考资料
* python从入门到实践web项目
* django2.2.2官方英文文档

## 所遇问题
* 使用django1.8.4跟着代码实现一遍，部署到heroku，但是发现django1.8.4已经不再支持，所以相当了解了网站开发流程，期间自己在本地部署时发现无法添加新表单，查了一遍代码，没有码错，应该是代码的逻辑错误，而且书上的代码和配套资源的代码并不是完全相同，可能是读者反馈后作者进行了修改，拿到配套资源的时候已经实现了大部分功能，发现django1.8.4已经不再维护遂弃坑。[python从入门到实践配套源码](https://pan.baidu.com/s/1KZ3FJfwtnIcJC6CFd_4Esg )：
* 提取码：k0b3 
* 使用了国内云服务器的免费试用，自己无法解决uWSGI和nginx的配置问题，遂放弃部署
* 写好了，但是使用了bootstrap3，使用gunicorn当服务器对处理静态文件不理想，访问网页需要2S左右。配置MySQL之后速度提升。

## 收获

* 在使用django2.2的过程中利用网络查找答案，[解决了centos7.6配置python3.7.3+pip环境过程](https://www.cnblogs.com/cx55887/p/10538748.html)，,当初困扰了我两天

* 了解了玩Linux首先设置linux国内软件源和pip国内镜像源,节省因为网络等待的时间。centos建议使用[阿里云镜像源](http://mirrors.aliyun.com/repo/),，选择对应发行版本的软件源。ubuntu我用的是清华的镜像源

* 下载并配置了SSH远程连接主机，这个是在使用华为云免费试用主机的时候发现网页命令行无法粘贴，然后使用BASH远程连接之后命令可以粘贴，优化使用体验。大致过程为在自己的需要远程连接的主机上安装SSHServer，配置SHHServer。在其他机器安装SSHClient(安装git后bash自带SSHClient)，在命令行使用一下命令远程连接主机：

* ```
  shh [用户名]@【主机ip】 -p [主机开放的端口]
  ```

  连接后可以在其他机器的命令行复制粘贴自己曾经保存过的命令来安装和配置环境

* 尝试在ubuntu18.04下安装MYSQL,虚拟环境安装pymysql之后，网页的运行速度上了一个等级，django2.2配置使用本机数据库看官方英文文档里面的例子可以解决。
``` python
DATABASES = {
    'default': {
        'ENINE':'django.db.backends.mysql',
        'NAME':'my_blog',
        #必须使用root账户，否则没有权限读写mysql数据量
        'USER':'root',
        'PASSWORD':'your_passwd',
    }
}

#同一目录下的__init__.py
import pymysql
pymysql.install_as_MYSQLdb()
````

出现权限问题无法运行

```
#配置mysql后没有权限，下一条命令无法运行
python manage.py runserver
#使用sudo 或者 root权限运行
sudo python manage.py runserver
```





   

  

