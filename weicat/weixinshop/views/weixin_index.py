import hashlib
from flask import Blueprint, render_template, redirect, request, session, make_response,Flask

weixin_index = Blueprint('weixin_index', __name__)  # type:Flask


@weixin_index.route('/weixin_index', methods=['GET', 'POST'])
def index():
    if request.method == "GET":  # 判断请求方式是GET请求
        my_signature = request.args.get('signature')  # 获取携带的signature参数
        my_timestamp = request.args.get('timestamp')  # 获取携带的timestamp参数
        my_nonce = request.args.get('nonce')  # 获取携带的nonce参数
        my_echostr = request.args.get('echostr')  # 获取携带的echostr参数

        token = 'yaohailong'  # 一定要跟刚刚填写的token一致

        # 进行字典排序
        data = [token, my_timestamp, my_nonce]
        data.sort()
        print(data)
        # 拼接成字符串
        temp = ''.join(data)

        # 进行sha1加密
        mysignature = hashlib.sha1(temp).hexdigest()

        # 加密后的字符串可与signature对比，标识该请求来源于微信
        if my_signature == mysignature:
            return my_echostr

