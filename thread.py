import threading
import time
class even(threading.Thread):
    def run(self):
        for p in range(1,11):
            if p%2==0:
                print(p,end=',')
            time.sleep(1)

class odd(threading.Thread):
    def run(self):
        for q in range(1,11):
            if q%2!=0:
              print(q,end=',')
            time.sleep(1)


x1=even()
x1.start()
y1=odd()
y1.start()