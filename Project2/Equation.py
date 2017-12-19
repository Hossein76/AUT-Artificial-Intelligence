import random
class State:
    def __init__(self,utility=0,state_list=[0,0,0,0]):
        self.state_list = state_list;
        self.utility = utility;

class Problem:
    def __init__(self):
        pass;
    def random_node(self):
        temp_node=State(state_list=[random.randint(0,40),random.randint(0,20),random.randint(0,14),random.randint(0,10)]);
        temp_node.utility=self.calculate_utility(temp_node);
        return temp_node;

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
        node.state_list[random.randint(0,len(node.state_list)-1)]=random.randint(0,40);
        node.utility=self.calculate_utility(node);
        return node;

    def Goal_test(self,node):
        if node.utility==0:
            return True;
        else:
            return False;

    def create_neighbors(self,node):
        neighbors = [];
        for i in range(0, len(node.state_list)):
            j = 0;
            while (j < 40):
                if (j == node.state_list[i]):
                    j += 1;
                    continue;
                temp = State(state_list=list(node.state_list));
                temp.state_list[i] = j;
                temp.utility = self.calculate_utility(temp);
                neighbors.append(temp);
                j += 1;
        return neighbors;

    def create_random_neighbor(self,node):
        temp = State(state_list=list(node.state_list), utility=node.utility);
        rand_var=random.randint(0,len(node.state_list)-1);
        rand_var2=random.randint(0,40);
        while(rand_var2==temp.state_list[rand_var]):
            rand_var2 = random.randint(0, 40);
        temp.state_list[rand_var]=rand_var2;
        temp.utility=self.calculate_utility(temp);
        return temp;

    def calculate_utility(self, node):
        utility=(node.state_list[0])+(node.state_list[1]*2)+(node.state_list[2]*3)+(node.state_list[3]*4)-40;
        return abs(utility);