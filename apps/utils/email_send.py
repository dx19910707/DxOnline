from random import Random

from django.core.mail import send_mail

from DxOnline.settings import EMAEL_FROM
from users.models import EmailVerifyRecord

__author__ = 'duxi'
__date__ = '2017-9-1 20:06'



def generate_random_str(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for i in range(randomlength):
        str += chars[Random().randint(0, len(chars) - 1)]
    return str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = generate_random_str(4)
    else:
        code = generate_random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '杜学在线网注册激活链接'
        email_body = '请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{}'.format(code)

        send_status = send_mail(email_title, email_body, EMAEL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '杜学在线网密码重置链接'
        email_body = '请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{}'.format(code)
        send_status = send_mail(email_title, email_body, EMAEL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = '杜学在线修改邮箱验证码'
        email_body = '你的邮箱验证码为：{}'.format(code)
        send_status = send_mail(email_title, email_body, EMAEL_FROM, [email])
        if send_status:
            pass


