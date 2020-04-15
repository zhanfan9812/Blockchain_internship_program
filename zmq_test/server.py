import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
count = 0

if __name__ == '__main__':
    print('zmq server start....')
    while True:
        message = socket.recv()
        count += 1
        print('received request. message:{} count:{}'.format(message, count))
        time.sleep(1)
        socket.send_string("World!")