# openscript

## Backblaze备份脚本

备份服务器文件的,但是我技术太烂力,写不出来啊qwq

## ehentai_inform

介绍: hentai@home服务器状态通知

所需依赖

```
# 服务器安装
apt install python-lxml
# Python pip 安装
pip install requests lxml BeautifulSoup4 Pyemail
```

### Cookie配置

配置28行的`Cookie`值

方法:

打开https://e-hentai.org/hentaiathome.php, 浏览器按`F12`打开开发者工具,选择`Network/网络`刷新一下,点`hentaiathome.php`下滑找到`cookie`

右键复制值填入cookie即可

### SMTP邮件通知

[Google你的邮件供应商](https://www.google.com.hk)

