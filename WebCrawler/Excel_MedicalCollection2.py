import xlrd
import xlwt
from xlutils.copy import copy
import urllib.request
import urllib.error
import urllib
import re
import random
import time


# 打开源Excel工作表格对象
path = './Resources/Part2_UseURL.xls'
workbook = xlrd.open_workbook(path)    # 打开文件目标xls
# sheet = workbook.sheets()[0]   # 打开第1个表格：Sheet1-decrease
# sheet = workbook.sheets()[0]
# sheet = workbook.sheet_by_index(0)
sheet = workbook.sheet_by_name('Sheet1')
nameCols = sheet.col_values(0)     # 打开表格第1列
codeCols = sheet.col_values(2)     # 打开表格第1列

# 建立临时表格对象
new_workbook = copy(workbook)    # 打开文件目标xls
new_worksheet = new_workbook.get_sheet(0)   # 从新工作簿获取第一个表格单

inputInfo = 1

# 循环爬取采购URL信息
for i in range(0, 610):     # 定义搜索范围
    print(i+1)
    if codeCols[i]:
        continue_tag = True
        while continue_tag:

            continue_tag = False
            keyword = urllib.parse.quote(nameCols[i])   # 字符转化
            # keyword = nameCols[i]
            print(nameCols[i] + ":" + keyword)  # Debug Info
            # URL构造
            # url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=' + keyword + '&oq=%25E6%2590%259C%25E7%25B4%25A2%25E7%259A%2584URL&rsv_pq=ff4781aa0003544e&rsv_t=bdaaQOyOAgvqN5IcJU8sMxtJHRD8W3M0MbyhEWIVrQKZ09bMrJLQ5ZSECp4&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_sug3=12&rsv_sug1=7&rsv_sug7=101&inputT=4341&rsv_sug4=5097'
            url = 'http://data.huaxuejia.cn/search.php?search_keyword=' + str(keyword)
            # url = 'http://www.molbase.cn/new/product/?keyword=' + str(keyword)
            print("URL:" + url)      # Debug Info 信息获取资源定位URL
            headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")

            try:
                opener = urllib.request.build_opener()
                opener.addheaders = [headers]
                data = opener.open(url).read()
                data = str(data)
                print(data)
            except urllib.error.HTTPError as e:
                print(e.code)
                inputInfo = input("Need input Verification-Code, Continue or not ?")
                continue_tag = True
            except urllib.error.URLError as e:
                print(e.reason)
                inputInfo = input("Error ,Continue or not ?")
                continue_tag = True

            # 错误等待处理
            if inputInfo == 0:
                break
            if continue_tag:
                continue

            # 正则表达式匹配信息过滤
            req = '<a href="(.*?)" target="_blank">'  # r'<a href="(.*?)" target="_blank"'
            # req = r'<a target="_blank" href="(.*?)" class="detial-btn cut-2">'
            res = re.compile(req).findall(data)
            print(str(res))
            # 判断是否获取到对应信息：无则返回None
            if not res:
                print('None')
                res.insert(0, 'None')

            surl = "http:" + res[0]     # 补全URL

            #数据存入Excel
            new_worksheet.write(i, 1, str(surl))
            new_worksheet.write(i, 2, 0)
            print(str(nameCols[i]), str(surl))  # 输出获得的有效信息
            new_workbook.save(path)     # 保存并替换原工作簿
            time.sleep(random.randint(3, 5))   # 反检测延时操作
