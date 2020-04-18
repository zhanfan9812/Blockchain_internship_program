import time
import zmq
import json
import os
import threading

_basepath = os.path.abspath(os.path.dirname(__file__))
conf = {}
conf['private_server'] = '*'            #miner ip
conf['port'] = '5555'                   #new port
conf['signal_port'] = '5556'            #reply port
conf['write_port'] = '5557'             #write_port

class Block:

    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
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
            time.sleep(2)
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
            time.sleep(2)
            print('publish_write_newblock', i)
            write_blockfile(bytes(block_string,'utf-8'))
            i+=1
            if i==3:
                break

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
        f.write(json.dumps(obj_data,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    block = Block(1, 'transaction', 'pre_hash')
    pub = publisher(conf['private_server'], conf['port'], 'new_block')
    # pub.publish_newblock(block)
    print('Server publish_newblock port start')
    _pub_thread = threading.Thread(target=pub.publish_newblock, kwargs={'data': block})
    _pub_thread.start()
    # get finished status
    _status = publisher(conf['private_server'], conf['signal_port'], '')
    print('Server rep port start')
    _status_thread = threading.Thread(target=_status.req_rep)
    _status_thread.start()