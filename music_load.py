import os
import time
from tkinter import *
from selenium import webdriver
from urllib.request import urlretrieve
#第三步，下载歌曲
def song_load(item):
    song_id = item['song_id']
    song_name = item['song_name']
    song_url = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
#第四步，创建文件夹
    os.makedirs('music_neteasy', exist_ok=True)
    path = 'C:\Users\Administrator\Desktop\music_neteasy\{}.mp3'.format(song_name)
    #显示数据到文本框
    time_now = time.strftime('%Y-%m-%d %H:%M:%S')
    #print('北京时间：'+time_now)
    text.insert(END, '北京时间：'+time_now)
    text.insert(END, '歌曲：{},正在下载...'.format(song_name))
    #文本框滚动
    text.see(END)
    #文本框更新
    text.update()
#第五步，保存下载
    urlretrieve(song_url, path)
    text.insert(END, '下载完成:{},请试听！'.format(song_name))
    text.see(END)
    text.update()
#第二步，爬虫部分
def get_music_name():
    #获取搜索的歌名
    name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    #隐藏浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)
    #driver = webdriver.Chrome()
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    req = driver.find_element_by_id('m-search')
    # #获取ID
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    print(a_id)
    #分割歌曲ID，保留等号后面的ID
    song_id = a_id.split('=')[-1]
    print(song_id)
    #获取歌曲名字
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    print(song_name)
    #定义一个字典
    item = {}
    item['song_id'] = song_id
    item['song_name'] = song_name
    driver.close()
    song_load(item)
# 第一步，搭建界面
root = Tk()
# 标题
root.title ('音乐下载器v1.0')
# 阻止修改大小
root.resizable(0, 0)
# 设置大小
root .geometry("550x410+400+200")
# 标签控件
label = Label(root, text="请输入歌曲的名称：", font=("黑体", 20))
# 标签定位
label.grid()
# 输入框
entry = Entry(root, font=("黑体", 20))
# 定位
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=("黑体", 16), width=50, height=15)
# 定位columnspan 组件横跨的列数
text.grid(row=1, columnspan=2)
# 点击按钮
button1 = Button(root, text="开始下载", font=("黑体", 16), command=get_music_name)
button1.grid(row=2, column=0, sticky=W)
button2 = Button(root, text="退出程序", font=("黑体", 16), command=root.quit)
button2.grid(row=2, column=1, sticky=E)
# 显示界面
root.mainloop()

