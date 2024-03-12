import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    f = open("microLog/" +name +".log", "a")
    logging.info("Thread %s: finishing", name)
    f.write("Logging for " + name +" start")
    f.close()

if __name__ == "__main__":
    
    logtype=['INFO' ,'DEBUG' ,'WARNING', 'ERROR','FATAL' ]
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x1 = threading.Thread(target=thread_function, args= ("microserv1", ) )
    logging.info("Main    : before running thread")
    x1.start()
    x2 = threading.Thread(target=thread_function, args=("microserv2", ))
    logging.info("Main    : before running thread")
    x2.start()
    x3 = threading.Thread(target=thread_function, args = ("microserv3", ))
    logging.info("Main    : before running thread")
    x3.start()
    logging.info("Main    : wait for the thread to finish")
    x1.join()
    x2.join()
    x3.join()
    logging.info("Main    : all done")



















