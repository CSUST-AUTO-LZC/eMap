import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def http_post(posturl, postdata):
    request_data = urllib.parse.urlencode(postdata).encode("utf-8")
    request_header = {}
    request_header['User-Agent'] = 'user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    response = urllib.request.Request(url=posturl, data=request_data, headers=request_header)
    html = urllib.request.urlopen(response).read()
    # 正则表达式匹配信息过滤
    # req = r'<a href="(.*?)" target="_blank"'
    # req = r'<a target="_blank" href="(.*?)" class="detial-btn cut-2">'
    # info = re.compile(req).findall(html)
    print(html)
    return 0


def http_get(url, keywords):
    url += keywords
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    return data


def Beautisoup(Htmltext):
    soup = BeautifulSoup(Htmltext, 'html.parser')
    print(soup.a.name)
    print(soup.a.attrs)
    print(soup.a.string)
    print(soup.a.Comment)
    print(soup.a.NavigableString)
    print(soup.a.get_text())
    print(soup.find_all(type='text/css')[0].get_text())
    return 0


if __name__ == '__main__':
    # url = "https://accounts.douban.com/passport/login"  # "https://china.guidechem.com/script/jq_scroll1.js?"
    # data = {'form_email': '24189705541@qq.com', 'form_password': '201659060221'}
    # http_post(posturl=url, postdata=data)

    # url = "https://cn.bing.com/search?q="  #Bing
    # url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=22073068_5_oem_dg&wd="  #Baidu
    url = "http://data.huaxuejia.cn/search.php"
    keywords = {'search_keyword': "肌氨酸", 'cookies': 'Y'}
    text = http_post(url, keywords)
    print(text)
    # htmlfile = open('./Resources/bing.html', 'wb')
    # htmlfile.write(text)
    # htmlfile.close()
    # Beautisoup(text)  # ('<a href="baidu.com" class="dt">hello</a>')

