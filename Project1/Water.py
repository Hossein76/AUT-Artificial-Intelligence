

class State:
    def __init__(self,parent=None,cost=0,heu=0,depth=0,three=0,four=0):
        self.parent=parent;
        self.cost=cost;
        self.heu=heu;
        self.depth=depth;
        self.three=three;
        self.four=four;



class Problem:
    def __init__(self):
        pass;

    def check_state(self,node1 , node2):
        if (node1.three==node2.three and node1.four==node2.four):
            return True;
        else: return False;

    def expand(self,node):
        mylist=[];
        if(node.four<4):
            mylist.append(State(parent=node,three=node.three,four=4));
            if (node.three>0):
                if (node.three+node.four<=4):
                    mylist.append(State(parent=node, three=0, four=node.three+node.four));
                else:
                    mylist.append(State(parent=node, three=node.three+node.four-4, four=4));
        if (node.three < 3):
            mylist.append(State(parent=node, three=3, four=node.four));
            if (node.four > 0):
                if (node.three + node.four <= 3):
                    mylist.append(State(parent=node, four=0, three=node.three + node.four));
                else:
                    mylist.append(State(parent=node, four=node.three + node.four - 3, three=3));
        if (node.four > 0):
            mylist.append(State(parent=node, three=node.three, four=0));
        if (node.three >0):
            mylist.append(State(parent=node, three=0, four=node.four));

        return mylist;

    def Goal_test(self,node):
        if (node.four==2):
            return True;
        else:return False;

    def Solution(self,node):
        mylist=[];
        n=node;
        while (n!=None):
            mylist.insert(0,n);
            n=n.parent;
        print ("found something");

        return mylist;

    def initialize(self):
        return [State(four=0,three=0)];