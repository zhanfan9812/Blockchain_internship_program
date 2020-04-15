import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.1.8:5555")

if __name__ == '__main__':
    print('zmq client start....')
    for i in range(1, 10):
        socket.send_string("hello")
        message = socket.recv()
        print('received reply message:{}'.format(message))