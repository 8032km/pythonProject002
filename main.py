import threading
from time import sleep


def cook(name='bludo', t=5):
    print(f"You started cooking {name}")
    sleep(t)
    print(f'{name} ready')


t1 = threading.Thread(target=cook, args=('borsch'))

cook('borsch')
