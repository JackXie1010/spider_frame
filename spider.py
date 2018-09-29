# coding: utf8
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
from lxml import etree


def save_data(data, mode='db'):
    if 'db' == mode:
        save_config.save_as_db(data)
    elif 'csv' == mode:
        save_config.save_as_csv(data)
    else:
        save_config.save_as_mongodb(data)


def extract_target(html, dict_arg):
    tree = etree.HTML(html)
    obj = dict()
    if isinstance(dict_arg, dict):
        for k, v in dict_arg.items():
            ret = tree.xpath(v)
            # ret = '*'.join(ret)
            obj[k] = ret
        return obj
    else:
        return '参数格式错误！'


def craw_html(url, way=''):
    if not way:
        headers = {'user-agent': ''}
        html = requests.get(url, headers=headers, verify=False).content
    else:
        c_options = Options()
        c_options.add_argument('--headless')
        browser = webdriver.Chrome(chrome_options=c_options, executable_path='D:/A/exe/chromedriver.exe')
        # browser = webdriver.Chrome(executable_path='D:/A/exe/chromedriver.exe')
        browser.get(url)
        html = browser.page_source
        browser.quit()
    return html


def spider_main(url, save_mode, way):
    html = craw_html(url, way)
    data = extract_target(html, config.parser_arg)
    save_data(data, save_mode)


if __name__ == '__main__':
    import save_config
    base_url = 'http://www.qiwen007.com'
    for i in range(1, 6):
        url = 'http://www.qiwen007.com/xiaohua/ye%d.html' %i
        html = craw_html(url)
        data = extract_target(html, config.parser_arg)
        for obj in save_config.get_obj_list(data):
            url = base_url + obj['img']
            img = requests.get(url).content
            with open(obj['title']+'.jpg', 'wb') as f:
                f.write(img)
                f.close()



