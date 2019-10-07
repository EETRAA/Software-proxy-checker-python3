import threading
import time
import queue
import os
import requests

def consume(q):
    while(True):
        #name = threading.currentThread().getName()
        #print ()
        item = q.get()
        time.sleep(1)
        #time.sleep(3)  # spend 3 seconds to process or consume the tiem
        print ("get an item -->"+item+"-- current queue size -->"+str(q.qsize()))
        proxies1 = {'http': "socks5://"+item}
        print (proxies1)
        r=requests.get('http://www.baidu.com', proxies=proxies1, timeout=10)
        print(r.status_code)
        if r.status_code == 200:
            #of = open("C:\\Users\\hades\\Desktop\\o.txt","a")
            of.write(str(proxies1))
            #
    q.task_done()
 
		
def producer(q):
    # the main thread will put new items to the queue
 
    for line in open("C:\\Users\\hades\\Desktop\\temp_socks_list_parsed.txt"):
        #name = threading.currentThread().getName()
        #print ()
        #item = "item-" + str(i)
        time.sleep(0.1)
        line = line.rstrip("\n")
        q.put(line)
        print ("put an item in queue"+str(q.qsize()))
        print ("******************"+str(q.queue))
    q.join()
 
if __name__ == '__main__':
	#of = open("C:\\Users\\hades\\Desktop\\temp_socks_list_parsed.txt")
    of = open("C:\\Users\\hades\\Desktop\\o.txt","a")
    q = queue.Queue(maxsize = 50)

    #1 thread to procuce
    t = threading.Thread(name = "ProducerThread", target=producer, args=(q,))
    t.start()
 
    threads_num = 3  # three threads to consume
    for i in range(threads_num):
        t = threading.Thread(name = "ConsumerThread-"+str(i), target=consume, args=(q,))
        t.start()
 

    q.join()
    #of.close()
