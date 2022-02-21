import socket
import time
print("Скрипт сделан Имёном, подпишись на канал t.me/imen_channel")
a = input("Введите ticket:")
s = a.replace('  ', '')
m = s.encode("utf-8").hex()
c = "000000740a2435353537333038632d643430312d343334312d613364652d336231386662333030376239121648616e647368616b6552656d6f7465536572766963651a0e70726f746f48616e647368616b6522241a220a20" + m
b = "0000004c0a2462353138316665652d373231322d346439382d613764352d6564396238633961303633351213506c6179657252656d6f7465536572766963651a0f7365744f6e6c696e65537461747573"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('158.177.37.2', 2222))
sock.send(bytes.fromhex(c))
time.sleep(0.1)
while 1:
    sock.send(bytes.fromhex(b))
    time.sleep(10)
    print("Цикл прошел успешно ")
