from time import sleep
from threading import Thread

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
    '''

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

t1 = Thread(target=vai_demorar, args=('Olá mundo 1', 10))
t1.start()

while t1.is_alive():
    print('Esperando a Thread.')
    sleep(2)

print('Thread acabou!')