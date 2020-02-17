import threading
import time
import queue
import os
import requests

def consume(q):
    while(q.qsize()!= 0):# changlog latest
        #name = threading.currentThread().getName()
        #print ()
        item = q.get()
        #time.sleep(1)
        #time.sleep(3)  # spend 3 seconds to process or consume the tiem
        print ("get an item -->"+item+"-- current queue size -->"+str(q.qsize()))
        proxies1 = {'https': "socks5://"+item}
        print (proxies1)
        try:
            r=requests.get('https://www.google.com', proxies=proxies1, timeout = 3)
        except:
            print("******************errs occurred******************")
        
        #print(r.status_code)
        try:
            if r.status_code == 200:
                #of = open("C:\\Users\\hades\\Desktop\\o.txt","a")
                of.write(str(proxies1))
                #
        except:
            print("_______________errs occurred_______________")
        q.task_done()

		
def producer(q):
    # the main thread will put new items to the queue

    for line in open("./temp_socks_list_parsed.txt"):
        #name = threading.currentThread().getName()
        #print ()
        #item = "item-" + str(i)
        print ("Now enter producer sub thread" + time.ctime())
        # time.sleep(1)
        line = line.rstrip("\n")
        q.put(line)
        print ("put an item in queue"+str(q.qsize()))
        print ("******************"+str(q.queue))
        print (time.ctime())
    # q.join()

if __name__ == '__main__':
	#of = open("C:\\Users\\hades\\Desktop\\temp_socks_list_parsed.txt")
    of = open("./o.txt","a")
    q = queue.Queue(maxsize = 2)
    producer_i = 0
    #1 thread to procuce
    t = threading.Thread(name = "ProducerThread", target=producer, args=(q,))
    t.start()
    #t.join()
#    time.sleep(5)
    threads_num = 10  # three threads to consume
    #for i in range(threads_num):
    t1 = threading.Thread(name = "ConsumerThread-1", target=consume, args=(q,))
    t1.start()
    t2 = threading.Thread(name = "ConsumerThread-2", target=consume, args=(q,))
    t2.start()
    t3 = threading.Thread(name = "ConsumerThread-3", target=consume, args=(q,))
    t3.start()
    t4 = threading.Thread(name = "ConsumerThread-4", target=consume, args=(q,))
    t4.start()
    t5 = threading.Thread(name = "ConsumerThread-5", target=consume, args=(q,))
    t5.start()
    t6 = threading.Thread(name = "ConsumerThread-6", target=consume, args=(q,))
    t6.start()
        

    q.join()
    print("main thread ends")
    of.close()
    print("file o.txt successfully closed")



#将数据存在内存里，完成之后再将数据转存到数据库
#创建临时存储数据的文件夹
#多线程消费与生产模型建立：抢食模型，慢食模型
#threading的锁
#！！创建类来写应用，哈哈哈哈
#异常处理
#变量现在是全局的，会判断失误，当上一个为通时，下一个会有概率出错
