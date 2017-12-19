import random



class State:
    def __init__(self,utility=0,state_list=[0,0,0,0,0,0,0,0]):
        self.state_list=state_list;
        self.utility=utility;

class Problem:
    def __init__(self):
        pass;

    def random_node(self):
        state_list=[];
        for i in range(0,8):
            state_list.append(random.randint(0,7));
        node=State(state_list=list(state_list));
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
        node.state_list[random.randint(0,len(node.state_list)-1)]=random.randint(0,7);
        node.utility=self.calculate_utility(node);
        return node;

    def Goal_test(self,node):
        if node.utility==0:
            return  True;
        else : return False;

    def create_neighbers(self,node):
        neighbers=[];
        for i in range(0,8):
            j=0;
            while(j<8):
                if(j==node.state_list[i]):
                    j+=1;
                    continue;
                temp=State(state_list=list(node.state_list));
                temp.state_list[i]=j;
                temp.utility=self.calculate_utility(temp);
                neighbers.append(temp);
                j+=1;
        return neighbers ;

    def create_random_neighber(self,node):
        temp=State(state_list=list(node.state_list),utility=node.utility);
        rand_var=random.randint(0,7);
        rand_var2=random.randint(0,7);
        while(temp.state_list[rand_var]==rand_var2):
            rand_var2 = random.randint(0, 7);
        temp.state_list[rand_var]=rand_var2;
        temp.utility=self.calculate_utility(temp);
        return temp;

    def calculate_utility(self,node):
        utility=0;
        for i in range(0,8):
            for j in range(i+1,8):
                if (node.state_list[i]==node.state_list[j]):utility+=1;
                else:
                  temp=j-i;
                  temp_up= node.state_list[i]+temp;
                  temp_down=node.state_list[i]-temp;
                  if(node.state_list[j]==temp_down):utility+=1;
                  elif (node.state_list[j]==temp_up):utility+=1;
        return utility;