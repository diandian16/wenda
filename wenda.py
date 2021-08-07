# -*- coding: UTF-8 -*-

import os
import asyncio
import random
from ppgan.apps import Photo2CartoonPredictor#人像动漫化
from PIL import Image

from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)

os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = "c2fc312912f6449cada8ddd8562c70ef"
os.environ['WECHATY_PUPPET_SERVICE_ENDPOINT'] = "47.100.50.78:8080"
os.environ['CUDA_VISIBLE_DEVICES']='0'

dir1={'1':['距离地球最近的巨行星是：Ａ．土星 Ｂ．木星 Ｃ．海王星 Ｄ．冥王星','b'],'2':['下列现象中，发生在太阳光球层的是：Ａ．耀斑 Ｂ．黑子 Ｃ．太阳风 Ｄ．日饵','b'],'3':['距离太阳最远的类地行星是：Ａ．金星 Ｂ．土星 Ｃ．火星 Ｄ．海王星','d'],'4':['下列现象中，发生在太阳色球层的是：Ａ．耀斑 Ｂ．黑子 Ｃ．太阳风 Ｄ．极光','a'],'5':['由于地球自转而产生的自然现象是：Ａ．昼夜更替 Ｂ．四季更替 Ｃ．昼夜长短变化 Ｄ．正午太阳高度变化','a'],'6':['6．下列各组星座中，均位于北天极周围的是：Ａ．仙后座、大熊座、小熊座 Ｂ．大熊座、天琴座、天鹰座 Ｃ．大熊座、小熊座、天琴座 Ｄ．小熊座、仙后座、天鹅座','c'],'7':['下列各天体系统中，级别最低的是：Ａ．银河系 Ｂ．地月系 Ｃ．河外星系 Ｄ．总星系','b'],'8':['8．北斗七星所在的星座是：Ａ．大熊星座 Ｂ．小熊星座 Ｃ．天鹰星座 Ｄ．仙后星座','a'],'9':['下列各地中，每年两次受到太阳直射的是：Ａ．20°N，30°E Ｂ．25°N，25°E Ｃ．23.5°S，60°N Ｄ．40°S，120°W','c'],'10':['下列各地在一年中昼夜长短变化幅度最大的是：Ａ．赤道上 Ｂ．北极圈内 Ｃ．南回归线上 Ｄ．北纬５０度','b']}
b=0
a=0
c=1
d=0

def Stitching_images(input_path:str):
    """
    input_path:输入图像地址
    return:覆盖生成图像
    本函数将完成生成图像与护照的拼接
    """
    save_img = input_path
    M_Img = Image.open('D:\\CIE评审\\output\\huzhao.jpg')
    S_Img = Image.open(input_path)
    coordinate=(21,64)
    M_Img.paste(S_Img, coordinate, mask=None)
    M_Img.save(save_img)

async def on_message(msg: Message):
    global a
    global b
    global c
    global d
    talker = msg.talker()
    if msg.text() == 'ding':
        await msg.say('这是自动回复: dong dong dong')
    if c==1 and  msg.text()=='提问':
        a=random.randint(1,2)
        await talker.say('准备回答问题拉，一共5题，看看你能回答对几道题呀')
        if a==1:
            b = 1
            await talker.say(dir1['1'][0])
        if a==2:
            b = 1
            await talker.say(dir1['2'][0])
    if a==1 and b==1 and msg.text()=='b':
        d=d+1
        await talker.say('回答正确')
        c=c+1
        b=0
    if a==1 and b==1 and (msg.text()=='a' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==2 and b==1 and msg.text()=='b':
        c = c + 1
        b = 0
        d=d+1
        await talker.say('回答正确')


    if a==2 and b==1 and (msg.text()=='a' or msg.text()=='c'or msg.text()=='d'):
        c = c + 1
        b = 0
        await talker.say('回答不正确')

    if c==2 and  msg.text()=='下一题':
        a=random.randint(3,4)
        if a==3:
            b = 1
            await talker.say(dir1['3'][0])
        if a==4:
            b = 1
            await talker.say(dir1['4'][0])
    if a==3 and b==1 and msg.text()=='d':
        c = c + 1
        b = 0
        d=d+1
        await talker.say('回答正确')


    if a==3 and b==1 and (msg.text()=='a' or msg.text()=='c'or msg.text()=='b'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==4 and b==1 and msg.text()=='a':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==4 and b==1 and (msg.text()=='b' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==5 and b==1 and msg.text()=='a':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==5 and b==1 and (msg.text()=='b' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==6 and b==1 and msg.text()=='c':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==6 and b==1 and (msg.text()=='b' or msg.text()=='a'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==7 and b==1 and msg.text()=='b':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==7 and b==1 and (msg.text()=='a' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==8 and b==1 and msg.text()=='a':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==8 and b==1 and (msg.text()=='b' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==9 and b==1 and msg.text()=='c':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==9 and b==1 and (msg.text()=='b' or msg.text()=='a'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0

    if a==10 and b==1 and msg.text()=='b':
        d=d+1
        await talker.say('回答正确')
        c = c + 1
        b = 0

    if a==10 and b==1 and (msg.text()=='a' or msg.text()=='c'or msg.text()=='d'):
        await talker.say('回答不正确')
        c = c + 1
        b = 0


    if c==3 and  msg.text()=='下一题':
        a=random.randint(5,6)
        if a==5:
            b = 1
            await talker.say(dir1['5'][0])
        if a==6:
            b = 1
            await talker.say(dir1['6'][0])
    if c==4 and  msg.text()=='下一题':
        a=random.randint(7,8)
        if a==7:
            b = 1
            await talker.say(dir1['7'][0])
        if a==8:
            b = 1
            await talker.say(dir1['8'][0])
    if c==5 and  msg.text()=='下一题':
        a=random.randint(9,10)
        if a==9:
            b = 1
            await talker.say(dir1['9'][0])
        if a==10:
            b = 1
            await talker.say(dir1['10'][0])
    if c==6 and  msg.text()=='下一题':
        await talker.say('你已经问答了所有题目拉')
        print(d)
        if d==0:
            await talker.say('你一共获得了0分,发张你的照片给你做个证书！')

        if d==1:
            await talker.say('你一共获得了20分,发张你的照片给你做个证书！')

        if d==2:
            await talker.say('你一共获得了40分,发张你的照片给你做个证书！')

        if d==3:
            await talker.say('你一共获得了60分,发张你的照片给你做个证书！')

        if d==4:
            await talker.say('你一共获得了80分,发张你的照片给你做个证书！')

        if d==5:
            await talker.say('你一共获得了100分,发张你的照片给你做个证书！')









    if msg.text() == 'hi' or msg.text() == '你好':
        await msg.say('欢迎来玩宇宙知识问答~发送提问获得题目，答完第一题可以发送下一题答题')

    if msg.text() == '图片':
        url = 'https://z3.ax1x.com/2021/08/04/fFcS2R.jpg'

        # 构建一个FileBox
        file_box_1 = FileBox.from_url(url=url, name='xx.jpg')

        await msg.say(file_box_1)


    if msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        #  制作平面星球护照
        await talker.say('已收到照片，开始制作中')
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()

        # 获取图片名
        img_name = file_box_user_image.name

        # 图片保存的路径
        img_path = './image/' + img_name

        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        # await msg.say('已收到证件照，开始制作中。。。。。。')

        p2c = Photo2CartoonPredictor(output_path='./output')
        p2c.run('./' + img_path)
        print("生成成功！")
        Stitching_images('./output/p2c_cartoon.png')  # 制作护照图像
        file_box_final_result = FileBox.from_file('./output/p2c_cartoon.png')

        await talker.say('制作完成，感谢来答题。')
        await msg.say(file_box_final_result)

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan', on_scan)
    bot.on('login', on_login)
    bot.on('message', on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())
