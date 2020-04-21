import time
import zmq
import json
import os
import threading
from flask import session

_basepath = os.path.abspath(os.path.dirname(__file__))
conf = {}
conf['private_server'] = '*'            #miner ip
conf['port'] = '5555'                   #new port
conf['signal_port'] = '5556'            #reply port
conf['write_port'] = '5557'             #write_port

class Block:

    def __init__(self, index, product_data, previous_hash):
        self.index = index
        self.product_data = product_data
        #self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0


class publisher:
    def __init__(self, bindserver,port,pub_key,pub_data=''):
        self.server = bindserver
        self.port = port
        #self.timestamp = timestamp
        self.key = pub_key
        self.data = pub_data

    def publish_newblock(self,**block):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://{}:{}".format(self.server,self.port))

        block_string = json.dumps(block['data'].__dict__, sort_keys=True)

        i = 0
        while True:
            publisher.send_multipart([b'new_block', bytes(block_string,'utf-8')])
            time.sleep(1)
            print('publish_newblock',i)
            i+=1
            if i==3:
                break

        publisher.close()
        context.term()


    def publish_write_newblock(self,block):
        context = zmq.Context()
        publisher = context.socket(zmq.PUB)
        publisher.bind("tcp://{}:{}".format(self.server,self.port))

        block_string = json.dumps(block, sort_keys=True)

        i = 0
        while True:
            publisher.send_multipart([b'write_block', bytes(block_string,'utf-8')])
            time.sleep(1)
            print('publish_write_newblock', i)
            i+=1
            if i==3:
                break

        write_blockfile(bytes(block_string, 'utf-8'))
        # session['logistic'] = (bytes(block_string, 'utf-8'))
        # update_db(bytes(block_string, 'utf-8'))
        publisher.close()
        context.term()

    def req_rep(self):
        context = zmq.Context()
        socket = context.socket(zmq.REP)
        socket.bind("tcp://{}:{}".format(self.server,self.port))

        while True:
            #  Wait for next request from client
            data = socket.recv()
            data_str = data.decode(encoding="utf-8")

            if  'finished' in data_str:
                #time.sleep(10)
                data_obc = json.loads(data_str)
                print('从订阅者处收到的信息: ',data_obc)
                pub_write = publisher(conf["private_server"],conf["write_port"],'')
                print('Server publish_write_newblock port start')
                pub_write.publish_write_newblock(data_obc['finished'])

                socket.close()
                context.term()
                break

def write_blockfile(data):
    obj_data = json.loads(data.decode(encoding="utf-8"))
    #print('the file ==================',obj_data," and index is ",json.dumps(obj_data,indent=2,ensure_ascii=False))
    with open(_basepath+'\\pubBlock'+str(obj_data['index'])+'.txt', 'w',encoding="utf-8") as f:
        # f.write(json.dumps(obj_data,indent=2,ensure_ascii=False))
        f.write(json.dumps(obj_data, ensure_ascii=False))

# def update_db(data):
#     obj_data = json.loads(data.decode(encoding="utf-8"))
#     product_data=obj_data['product_data']
#     temp = product_data.split('\n')
#     temp1 = temp[0].split(' ')
#     product_name = temp1[1]
#     index = obj_data['index']
#     random_num = obj_data['nonce']
#     current_hash = obj_data['now_hash']
#     pre_hash = obj_data['previous_hash']
#
#     logistic = Logistic.query.filter(Logistic.chain_index == index, Logistic.product_name == product_name).first()
#     # logistic.current_hash = current_hash
#     # logistic.random_num = random_num
#     # logistic.pre_hash = pre_hash
#     # db.session.commit()

def add_block(index, product_data, pre_hash):
    block = Block(index, product_data, pre_hash)
    pub = publisher(conf['private_server'], conf['port'], 'new_block')
    # pub.publish_newblock(block)
    print('Server publish_newblock port start')
    # print(type({'data': block}))
    _pub_thread = threading.Thread(target=pub.publish_newblock, kwargs={'data': block})
    _pub_thread.start()
    # get finished status
    _status = publisher(conf['private_server'], conf['signal_port'], '')
    print('Server rep port start')
    _status_thread = threading.Thread(target=_status.req_rep)
    _status_thread.start()

if __name__ == '__main__':
    add_block(0,'product_data',1)