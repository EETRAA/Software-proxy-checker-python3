import threading
import time
import queue
import os

def consume(q):
    while(True):
        #name = threading.currentThread().getName()
        #print ()
        item = q.get();
        time.sleep(1)
        #time.sleep(3)  # spend 3 seconds to process or consume the tiem
        print ("get an item."+item+"-----"+str(q.qsize()))
        q.task_done()
 
		
def producer(q):
    # the main thread will put new items to the queue
 
    for line in open("C:\\Users\\hades\\Desktop\\temp_socks_list_parsed.txt"):
        #name = threading.currentThread().getName()
        #print ()
        #item = "item-" + str(i)
        time.sleep(0.1)
        q.put(line)
        print ("put an item in queue"+str(q.qsize()))
 
    q.join()
 
if __name__ == '__main__':
	#of = open("C:\\Users\\hades\\Desktop\\temp_socks_list_parsed.txt")
    q = queue.Queue(maxsize = 50)
    
    threads_num = 3  # three threads to consume
    for i in range(threads_num):
        t = threading.Thread(name = "ConsumerThread-"+str(i), target=consume, args=(q,))
        t.start()
 
    #1 thread to procuce
    t = threading.Thread(name = "ProducerThread", target=producer, args=(q,))
    t.start()
 
    q.join()
    #of.close()