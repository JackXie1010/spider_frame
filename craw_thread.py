# coding: utf8
import queue
import threading
import spider
import config

queue_html = queue.Queue(maxsize=1000)
queue_data = queue.Queue(maxsize=1000)


def producer(queue_detail_url, queue_html, way):
    while True:
        print('------producer start---------')
        detail_url = queue_detail_url.get()
        html = spider.craw_html(detail_url, way)
        queue_html.put(html)


def middle(queue_html, queue_data):
    while True:
        print('-------middle start-------------')
        html = queue_html.get()
        data = spider.extract_target(html, config.parser_arg)
        print(data)
        queue_data.put(data)


def concumer(queue_data, save_method):
    while True:
        print('----consumer start-----')
        ret = queue_data.get()
        spider.save_data(ret, save_method)


def thread_main(queue_detail_url, save_mode, way):
    for i in range(3):
        t_producer = threading.Thread(target=producer, args=(queue_detail_url, queue_html, way))
        t_middle = threading.Thread(target=middle, args=(queue_html, queue_data))
        t_consumer = threading.Thread(target=concumer, args=(queue_data, save_mode))
        t_producer.start()
        t_middle.start()
        t_consumer.start()
        t_producer.join()
        t_middle.join()
        t_consumer.join()


if __name__ == '__main__':
    queue_detail_url = queue.Queue()
    for i in range(1, 6):
        url = 'http://www.qiwen007.com/xiaohua/ye%d.html' % i
        queue_detail_url.put(url)
    thread_main(queue_detail_url, 'mongo')
