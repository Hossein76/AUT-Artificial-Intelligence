class State:
    def __init__(self,parent=None,cost=0,heu=0,depth=0,x=0,y=0):
        self.parent=parent;
        self.cost=cost;
        self.heu=heu;
        self.depth=depth;
        self.x=x;
        self.y=y;



class Problem:
    def __init__(self,m=0,n=0,map=[]):
        self.m=m;
        self.n=n;
        self.map=map;

    def check_state(self,node1 , node2):
        if (node1==node2):
            return True;
        else: return False;

    def expand(self,node):
        children=[];
        for i in [[1,0],[-1,0],[0,1],[0,-1]]:
            x_temp=node.x+i[0];
            y_temp=node.y+i[1];
            if (x_temp<self.n and x_temp>=0 and y_temp<self.m and y_temp>=0 ):
                if (self.map[y_temp][x_temp]==0):
                    continue;
                else :
                    children.append(State(parent=node,cost=node.cost+1,heu=node.cost+1+self.heuristic(x_temp,y_temp),depth=node.depth+1,x=x_temp,y=y_temp));
        return children;

    def Goal_test(self,node):
        if (node.x==self.n-1 and node.y==self.m-1):
            return True;
        else:
            return False;

    def Solution(self,node):
        mylist = [];
        n = node;
        while (n != None):
            mylist.insert(0, n);
            n = n.parent;
        print ("found something");
        return mylist;

    def initialize(self):
        return [State(heu=self.heuristic(0,0))];

    def heuristic(self, x,y):
        heu = 0;
        heu += abs(self.n-1 - x);
        heu += abs(self.m-1 - y);
        return heu;