import zmq
import time
import random

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

if __name__ == '__main__':
    print("发布者启动.....")
    time.sleep(2)
    for i in range(1000):
        tempterature = random.randint(-10, 40)
        message = "我是publisher, 这是我发布给你们的第{}个消息！今日温度{}".format(i+1, tempterature)
        socket.send_string(message)