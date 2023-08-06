import socket
import threading
import dtptcpy.tempP as tempP
import multiprocessing
import time
class DtptcSerCore:
    def __init__(self,chanelcount:int=10) -> None:
        self.defaultport = ["127.0.0.1",12346]
        self.database = {}
        for idx in range(chanelcount):
            self.database[idx]=[]
        

    def bindport(self):
        def run_check():
            time.sleep(0.2)
            cli = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            cli.connect(tuple(self.defaultport))
            cli.send(b"ko")
        while self.defaultport[1]<65535:
            print(self.defaultport)
            try:
                self.ser = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                self.ser.bind(tuple(self.defaultport))
                self.ser.listen()
                threading.Thread(target=run_check).start()
                cll = self.ser.accept()
                dd=cll[0].recv(2)
                if dd==b"ko":
                    tempP.write(str(self.defaultport[1]))
                    return
                else:
                    raise Exception()
            except:
                self.defaultport[1]=self.defaultport[1]+1
        raise Exception("建立服务失败")
        
    def SerSendData(self,obj,channel):
        if len(self.database[channel])>0:
            data = self.database[channel].pop(0)
            obj[0].send(f"ok-{len(data)}-".ljust(100,"0").encode())
            obj[0].send(data)
        else:
            obj[0].send("fail-".encode())

    def SerSendLen(self,obj,channel):
        data = len(self.database[channel])
        obj[0].send(f"ok-{data}-".ljust(100,"0").encode())
    def SerRecvData(self,obj,channel,recvlen):
        # print(1)
        data = obj[0].recv(recvlen)
        # print(2)
        self.database[channel].append(data)
        # print(3)
        obj[0].send(f"ok-".ljust(100,"0").encode())
    def SingleConnectDeal(self,cli_obj):
        gg=cli_obj[0].recv(100)
        # print(gg)
        args = gg.split(b"-")
        # print(args)
        if gg.find(b"getlen")==-1:
            if gg.find(b"getdata")==-1:
                if gg.find(b"senddata")==-1:
                    pass
                else:
                    self.SerRecvData(cli_obj,int(args[1]),int(args[2]))
            else:
                self.SerSendData(cli_obj,int(args[1]))
        else:
            self.SerSendLen(cli_obj,int(args[1]))
        cli_obj[0].close()
    def run(self):

        while True:
            cli = self.ser.accept()
            threading.Thread(target=self.SingleConnectDeal,args=(cli,)).start()
            # print(22)

class DtptcSer:
    def _runser(self,channel:int):
        xxe = DtptcSerCore(channel)
        xxe.bindport()
        xxe.run()
    def run(self,channel:int):
        pp=multiprocessing.Process(target=self._runser,args=(channel,))
        pp.start()
        time.sleep(0.4)
        return pp
if __name__=="__main__":
    xxe = DtptcSer()
    xxe.run(21)

# ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# ss.bind(("127.0.0.1",2333))
# ss.listen()
# #接收数据 数据存入
# #接收查询 获取数据 数据去除
# #-->连接发送列表长度-->获取客户端操作指令-->"send"-->接收数据并存储
# #-->连接发送列表长度-->获取客户端操作指令-->“recv”-->获取单条数据
# def SendLen():
#     ...
# def SendSingleData():
#     ...
# def RecvSingleData():
#     ...

# while True:
#     xx = ss.accept()
#     print("in")
#     xx[0].send("2333".encode("gbk"))
#     time.sleep(1000)
#     xx[0].send("2444".encode("gbk"))
#     xx[0].close()
#     print("out")

# for idx in database:
#     print(idx,database.get(idx))
