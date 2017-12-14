class State:
    def __init__(self,utility=0):
        self.utility=utility;

class Problem:
    def __init__(self):
        pass;
    def random_node(self):
        return State();

    def check_state(self,node1,node2):
        if node1==node2:
            return True;
        else:
            return False;