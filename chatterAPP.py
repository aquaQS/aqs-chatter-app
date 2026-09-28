import socket
import threading

TARGET_IP =  "target IP is NOT your own IP"
PORT = 5000          


def theListener():
    while True:
        data, address = sock.recvfrom(1024)
        print(address,"> ", data.decode())

      
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", PORT)) 
listener_thread = threading.Thread(target=theListener, daemon=True)
listener_thread.start()


def main():
    while True:
        message = input("> ")

        if message == "q":
            break 

        else:
            sock.sendto(message.encode(), (TARGET_IP, PORT))



main()
