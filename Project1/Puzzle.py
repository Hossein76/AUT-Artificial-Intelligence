class State:
    def __init__(self,parent=None,cost=0,heu=0,depth=0,matrix=[],zero=0):
        self.parent=parent;
        self.cost=cost;
        self.heu=heu;
        self.depth=depth;
        self.matrix=matrix;
        self.zero=zero;



class Problem:
    def __init__(self):
        pass;

    def check_state(self,node1 , node2):
        for i in range (0,9):
            if (node1.matrix[i]!=node2.matrix[i]):
                return False
        return False;

    def expand(self,node):
        children=[];
        if (node.depth%8==9):
            print(node.depth);
        for i in [1,-1,3,-3]:
            if (node.zero+i<9 and node.zero+i>=0):
                mylist=list(node.matrix);
                mylist[node.zero]=node.matrix[node.zero+i];
                mylist[node.zero+i]=0;
                children.append(State(parent=node,depth=node.depth+1,cost=node.cost+1,heu=node.cost+1+self.heuristic(mylist),matrix=mylist,zero=node.zero+i));
        return children;

    def Goal_test(self,node):
        for i in node.matrix:
            if (node.matrix[i]!=i):
                return False;
        return True;

    def Solution(self,node):
        mylist = [];
        n = node;
        while (n != None):
            mylist.insert(0, n);
            n = n.parent;
        print ("found something");
        return mylist;

    def initialize(self):
        mylist=[5,8,3,1,6,4,7,2,0];
        return [State(matrix=mylist,heu=self.heuristic(mylist),zero=8)];

    def heuristic(self,mylist):
        heu=0;
        for i in range(0,len(mylist)):
            j=mylist[i];
            j1=j%3;
            j2=j//3;
            i1=i%3;
            i2=i//3;
            heu+=abs(i1-j1);
            heu+=abs(i2-j2);
        return heu;