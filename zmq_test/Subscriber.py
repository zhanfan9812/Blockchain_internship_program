import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://192.168.1.4:5555")

# 客户端需要设定一个过滤，否则收不到任何信息
socket.setsockopt_string(zmq.SUBSCRIBE, '')

if __name__ == '__main__':
    print('订阅者一号启动....')
    while True:
        message = socket.recv_string()
        print("（订阅者一号）接收到'发布者'发送的消息：{}".format(message))