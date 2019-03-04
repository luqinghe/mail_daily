# 环境  
本项目基于python3.7
# 启动  
- 修改`config.ini`，配置你的邮箱和密码
- 修改`addrs.txt`，配置发件人及收件人信息，名称和地址用英文逗号`,`分割
- 启动命令`python do_something.py`
# 自定义  
- 邮件发送的是`html`，内容在`template.html`模板中配置，可自行修改，修改后记得修改`do_something.py`中的`_get_html`方法。
# 效果
![Image text](https://raw.githubusercontent.com/luqinghe/mail_daily/master/show.png)
# 感谢
- 本项目参考了[https://github.com/Vincedream/NodeMail](https://github.com/Vincedream/NodeMail)创意
- 感谢[@blueSky1991](https://github.com/blueSky1991)的支持