import threading
from time import sleep

x = []


def cook(name='bludo', t=3):
    print(f"You started cooking {name}")
    sleep(t)
    print(f'{name} ready')


t1 = threading.Thread(target=cook, args=('borsch',))
t2 = threading.Thread(target=cook, args=('rise',))
t3 = threading.Thread(target=cook, args=('plov',))

t1.start()
t2.start()

t2.join()
print('U can use for plov')
t3.start()

t1.join()
t3.join()




print(x)