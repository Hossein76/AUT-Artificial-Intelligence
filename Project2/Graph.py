import random
class State:
    def __init__(self,utility=0,state_list=[0,0,0,0,0,0,0,0,0,0,0,0]):
        self.state_list = state_list;
        self.utility = utility;

class Problem:
    def __init__(self,matrix=[]):
        self.degree=[];
        self.graph_nodes=[];
        for i in range(0,len(matrix)):
            temp_list=[];
            for j in range(0,len(matrix[i])):
                if (matrix[i][j]==1):
                    temp_list.append(j);
            self.graph_nodes.append(temp_list);
        for i in self.graph_nodes:
            self.degree.append(len(i));

    def random_node(self):
        node=State(state_list=[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)])
        node.utility=self.calculate_utility(node);
        return node;

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
        node.state_list[random.randint(0,len(node.state_list)-1)]=random.randint(0,1);
        node.utility=self.calculate_utility(node);
        return node;

    def Goal_test(self,node):
        if node.utility==0:
            return True;
        else:
            return False;

    def create_neighbors(self,node):
        temp_list=[];
        for i in range(0,len(node.state_list)):
            temp_node=State(state_list=list(node.state_list));
            temp_node.state_list[i]=1-temp_node.state_list[i];
            temp_node.utility=self.calculate_utility(temp_node);
            temp_list.append(temp_node);
        return temp_list;

    def create_random_neighbor(self,node):
        temp_node = State(state_list=list(node.state_list));
        rand_var=random.randint(0,len(node.state_list)-1);
        temp_node.state_list[rand_var] = 1 - temp_node.state_list[rand_var];
        temp_node.utility = self.calculate_utility(temp_node);
        return temp_node;

    def calculate_utility(self, node):
        utility=0;
        degree0=0;
        degree1=0;
        for i in range(0,len(node.state_list)):
            if node.state_list[i]==1:
                degree1+=self.degree[i];
                for j in self.graph_nodes[i]:
                    if (node.state_list[j]==0):
                        utility+=1;
            else:
                degree0+= self.degree[i];
        utility+=abs(degree1-degree0);
        return utility;