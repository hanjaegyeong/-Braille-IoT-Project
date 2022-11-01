import bluetooth
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect(("B8:D6:1A:82:4D:92", 1))
print("bluetooth connected!")

msg = input("send message")
socket.send(msg)
socket.close()
