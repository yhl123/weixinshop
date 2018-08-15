import json
import requests
from settings import Config

s = requests.session()


# 获取access_token
def token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
        Config.AppID, Config.AppSecret)
    res = s.get(url=url)
    access_token = json.loads(res.text).get('access_token')
    return access_token


# 自定义菜单
def createMenu():
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % token()
    menu={}#自定义菜单字段属性
    res = requests.post(url, menu.encode('utf8'))
    return res.text


print(createMenu())
