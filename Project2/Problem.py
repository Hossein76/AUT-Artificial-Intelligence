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

    def mix(self,parent1,parent2,num_attr=0):
        return State();

    def mutate(self,node):
        return State();

    def Goal_test(self,node):
        return False;

    def create_neighbers(self,node):
        return [];

    def create_random_neighber(self,node):
        return State();
