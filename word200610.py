# 时间2020.06.10
# 安装包：bs4，requests，time(自带)，xlsxwriter，win32com(pypiwin32)
# 读excel单词进行翻译、

import xlrd
from bs4 import BeautifulSoup
import requests
import time
import xlsxwriter as wx
import win32com.client

xlsx = xlrd.open_workbook("D:\excel20200610.xlsx")
table = xlsx.sheets()[0]
dst_wb = wx.Workbook('words_try.xls')
worksheet = dst_wb.add_worksheet()

for row in range(0, table.nrows):
    time.sleep(1)
    word = table.cell(row, 0).value
    url = 'http://www.youdao.com/w/eng/' + word

    web_data = requests.get(url).text
    soup = BeautifulSoup(web_data, 'lxml')
    meaning = str(soup.select('#phrsListTab > div.trans-container>ul>li')).replace('<li>', '').replace('</li>', '')
    translation = meaning[1:-1]
    print(word)
    worksheet.write(row, 0, word)
    worksheet.write(row, 1, translation)
dst_wb.close()

speaker = win32com.client.Dispatch("SAPI.SpVoice")
xlsx = xlrd.open_workbook('words_try.xls')
table = xlsx.sheets()[0]
for row in range(0, table.nrows):
    time.sleep(1)
    word = table.cell(row, 0).value
    word_segment = []
    for i in word:
        word_segment.append(i)
        word_segment.append('-')
        word_2 = ''.join(word_segment)
    speaker.Speak(str(table.cell(row, 0).value))
    speaker.Speak(str(word_2))
    speaker.Speak(str(table.cell(row, 0).value))
    speaker.Speak(str(table.cell(row, 1).value))
