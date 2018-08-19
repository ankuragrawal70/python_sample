from threading import Thread
from time import sleep
from multiprocessing import Process
from multiprocessing import Pool


def check_primes(elements):
    for i in range(0, 5):
        sleep(0.2)
        print("checking primes", i)


def check_square_root(elements):
        for i in range(0, 10):
            print "checking square root", i


def call_threads():
    print("calling threads")
    threads = []

    p = Thread(target=(check_primes), args=(['10', '20'], ))
    p_sq = Thread(target=(check_square_root), args=(['10', '20'], ))

    p.start()
    p_sq.start()

    p.join()
    p_sq.join()



def invoke_wrapper():
    pass



import os
os.statvfs()

def check_variable_and_invoke_wrapper():
    print("calling wrapper")
    for i in range(0, 100):
        sleep(1)
        print(i)
    print("finishing wrapper")


def success(obj):
    print("success is True")
    print(obj.__dict__)

def call_other_methods():
    # pool = Pool(processes=1)

    print "final method called"
    ip = Process(target=check_variable_and_invoke_wrapper, name="python_my_process")
    # ip.daemon = True
    ip.start()
    ip.join()
    # ip.join(timeout=1)

    
    # ip = Process(check_variable_and_invoke_wrap)
    # ip.daemon = Thread                         # i   call_final()
    # ip.start()                                 # pool.apply_async(check_variable_and_invoke_wrapper, callback=success)
    # ip.join(timeout=1)                         call_final()

def call_final():
    print("final method")

if __name__ == "__main__":
        call_threads()
        call_other_methods()
        #call_final()
