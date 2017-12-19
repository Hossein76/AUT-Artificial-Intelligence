import random
class State:
    def __init__(self,utility=0,state_list=[]):
        self.state_list = state_list;
        self.utility = utility;

class Problem:
    def __init__(self):
        pass;
    def random_node(self):
        return State();

    def check_state(self,node1,node2):
        for i in range(0,len(node1.state_list)):
            if(node1.state_list[i]!=node2.state_list[i]):
                return False;
        return True;

    def mix(self,parent1,parent2,slice_point=0):
        temp_node=State(state_list=list(parent2.state_list));
        for i in range(0,slice_point):
            temp_node.state_list[i]=parent1.state_list[i];
        temp_node.utility=self.calculate_utility(temp_node);
        return temp_node;

    def mutate(self,node1):
        node=State(state_list=list(node1.state_list),utility=node1.utility);
        node.state_list[random.randint(0,len(node.state_list)-1)]=random.randint(0,7);
        node.utility=self.calculate_utility(node);
        return node;

    def Goal_test(self,node):
        return False;

    def create_neighbers(self,node):
        return [];

    def create_random_neighber(self,node):
        return State();

    def calculate_utility(self, node):
        utility=0;
        return utility;