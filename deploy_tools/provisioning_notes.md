配置新网站
==========

## 需要安装的包:

* nginx
* Python 3
* Git
* pip
* virtualenv

以Ubuntu为例，可以执行下面命令安装:

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## 配置Nginx虚拟主机

* 参考 nginx.template.conf
* 把SITENAME替换成所需的域名，例如staging.my-domain.com

## Upstart任务

* 参考gunicorn-upstart.template.conf
* 把SITENAME替换成所需的域名，例如staging.my-domain.com

## 文件夹结构

假设有用户家目录 /home/username

/home/username
  |
  |----sites
      |
      |----SITENAME
          |
          |----database
          |----source
          |----static
          |----virtualenv

