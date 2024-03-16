'''
Apache License

All code written here by:
Author: Sandip Pal


'''


import logging
import threading
import time
import random
import datetime



logInfo =['Device working in turbo mode' , 'user xxx logged in',
          'Function called twice with mno bit', 'Got signal to peek load',
           'Memory allocated for jobs in queue', 'Service in healthy stage and can allocate more memory']
logWarn = []
logError = []
logFatal = ['function divide by 0 abort call issued' , 'wrong memory location access corruption, reboot issued',
            'kernel fault detected in core', 'Interrupt overflow, out of stack space']
logtype=['INFO' ,'DEBUG' ,'WARNING', 'ERROR','FATAL' ]



def thread_function(name):
    
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    f = open("microLog/" +name +".log", "w")
    random.seed(id(name))
    logging.info("Thread %s: finishing", name)
    time_in_millis = 1710605681000
    dt = datetime.datetime.fromtimestamp(time_in_millis / 1000.0, tz=datetime.timezone.utc)
    f.write("Logging for " + name +"       start \n")
    for i in range (1, 1000) :
        time_in_millis += random.randint(1,1000)
        time_in_millis = write_log(name, f, time_in_millis)
    f.close()
    
def write_log(name, f, tm):
    # we write log in chunks to imitate some function
    # chunks are also randon num betwen 3-10
    j = random.randint(3, 10)
    rnum = random.randint(0, 100) # give 10% chance for fatal or error
    if rnum > 90 :
        ltyp = logtype[random.randint(3,4)]
    else :
        ltyp = logtype[random.randint(0,2)]
    for i in range(1, j):
        if rnum > 90 :
            lgstr = random.choice(logFatal)
        else :
            lgstr = random.choice(logInfo)
        tm+= random.randint(1,1000)
        dt = datetime.datetime.fromtimestamp(tm / 1000.0, tz=datetime.timezone.utc)
        f.write(dt.strftime("%m/%d/%Y, %H:%M:%S") + " " + ltyp + ":   " + lgstr + "\n")
        
    return tm

if __name__ == "__main__":
    
   
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x1 = threading.Thread(target=thread_function, args= ("microserv1", ) )
    logging.info("Main    : before running thread")
    x1.start()
    x2 = threading.Thread(target=thread_function, args=("microserv2",))
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



















