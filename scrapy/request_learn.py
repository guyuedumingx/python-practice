import requests
from bs4 import BeautifulSoup
import re
import bs4
import xlwt

def get_html(url):
    #爬取网页内容
    try:
        r = requests.get(url, timeout = 30)   
        r.raise_for_status()      #异常判断
        r.encoding = r.apparent_encoding
        return r.text           #返回文本格式的网页
    except:
        print ("")

def find_html(job_name, job_from, job_pay, job_info, job_place, html):
    """用于清洗网页并获取关键信息"""
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all('dl',"list-noimg job-list clearfix new-dl"):
        job_name.append(tag.find('dt').a.string)                        #获取工作内容   
        job_from.append(tag.find('div', "new-dl-company").a.string)     #获取发布工作的公司名称
        job_pay.append(tag.find('div', "new-dl-salary").string)         #获取工作薪资信息
        job_info.append(tag.find('div', "new-dl-tags").text)            #获取福利信息
        job_place.append(tag.find('dd', "pay").string)                  #获取工作地点

name = []
pay = []
company = []
info = []
place = []
url = 'http://gz.ganji.com/zpruanjiangongchengshi/zhaopin/o0/'
html = get_html(url)
find_html(name, company, pay, info, place, html)



# 表格样式设置
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Work Information')
font = xlwt.Font()
font.bold = True
font.name = 'SimSun'            #设置标题为宋体
font.height = 12 * 20           #设置行高
style = xlwt.XFStyle()
style.font = font
al = xlwt.Alignment()
al.horz = 0x02                  # 设置水平居中
style.alignment = al

#设置标题及其样式
worksheet.write_merge(0, 0, 0, 2, "工作内容", style)
worksheet.write_merge(0, 0, 3, 5, "公司名称", style)
worksheet.write_merge(0, 0, 6, 8, "薪酬范围", style)
worksheet.write_merge(0, 0, 9, 11, "附加信息", style)
worksheet.write_merge(0, 0, 12, 14, "工作地点", style)


# 打印相关信息
for i in range(len(name)):
    worksheet.write_merge(i+1, i+1, 0, 2, name[i])
    worksheet.write_merge(i+1, i+1, 3, 5, company[i])
    worksheet.write_merge(i+1, i+1, 6, 8, pay[i])
    worksheet.write_merge(i+1, i+1, 9, 11, info[i])
    worksheet.write_merge(i+1, i+1, 12, 14, place[i])
workbook.save('work_imformation.xls')               #保存表格
