# coding: utf8
import spider
import craw_thread
import queue


def main(save_mode='db', way=0, multithreading=0):
    '''
    第1个参数：保存的模式，可以保存为 1）sqllite/mysql, 2）csv文件， 3）mongodb ，
              值为’db' 保存至sqllite/mysql， 值为’csv' 保存为csv文件， 值为’db' 保存至mongodb，
    第2个参数：爬取html的方法， 该参数默认使用0
             way=0时使用requests 爬取html,   way=1时使用selenium请求html源码（慢，适合动态页面）
    第3个参数：是否启动多线程爬取，0为不启动，1为启动，默认为0
            线程个数请到craw_thread.py 文件的 thread_main（）的for循环设置，此处默认各启动3的线程
    '''
    queue_detail_url = queue.Queue()
    if 0 == multithreading:
        for i in range(1, 6):
            url = 'http://www.qiwen007.com/xiaohua/ye%d.html' % i
            spider.spider_main(url, save_mode, way)
    else:
        for i in range(1, 6):
            url = 'http://www.qiwen007.com/xiaohua/ye%d.html' % i
            queue_detail_url.put(url)
        craw_thread.thread_main(queue_detail_url, save_mode, way)


if __name__ == '__main__':
    main('csv', 0, 0)  # 3 个参数都可以为空，设置了默认值
    '''
        第1个参数：保存的模式，可以保存为 1）sqllite/mysql, 2）csv文件， 3）mongodb ，
                  值为’db' 保存至sqllite/mysql， 值为’csv' 保存为csv文件， 值为’db' 保存至mongodb， 
        第2个参数：爬取html的方法， 该参数默认使用0
                 way=0时使用requests 爬取html,   way=1时使用selenium请求html源码（慢，适合动态页面）
        第3个参数：是否启动多线程爬取，0为不启动，1为启动，默认为0，
                线程个数请到craw_thread.py 文件的 thread_main（）的for循环设置，此处默认各启动3的线程
    '''