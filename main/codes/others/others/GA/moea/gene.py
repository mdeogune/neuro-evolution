#gene.py

class Node:
    def __init__(self,node_ctr,nature):
        self.num=node_ctr
        self.nature=nature  #'I','H1','H2','O'


class Conn:
    def  __init__(self,innov_num,source,destination,weight):
        self.status=status          #determines enabled or disabled
        self.source=source          #a node object
        self.destination=destination#same as above
        self.weight=weight
        self.innov_num=innov_num
    def get_status(self):
        return self.status
    def get_innov_num(self):
        return self.innov_num

    def get_couple(self):
        return (self.source,self.destination)


class BiasConn(Conn):
    def __init__(self,out_node,weight):
        numb=-1
        nature=-1
        Conn.__init__(-1,Node(numb,nature),out_node,weight)

