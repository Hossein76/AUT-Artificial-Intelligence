import random



class State:
    def __init__(self,utility=0,poses=[0,0,0,0,0,0,0,0]):
        self.poses=poses;
        self.utility=utility;

class Problem:
    def __init__(self):
        pass;

    def random_node(self):
        poses=[];
        for i in range(0,8):
            poses.append(random.randint(0,7));
        node=State(poses=list(poses));
        node.utility=self.calculate_utility(node);
        return node;

    def check_state(self,node1,node2):
        for i in range(0,8):
            if(node1.poses[i]!=node2.poses[i]):
                return False;
        return True;

    def mix(self,parent1,parent2):
        return State();

    def mutate(self,node):

        return State();

    def Goal_test(self,node):
        if node.utility==0:
            return  True;
        else : return False;

    def create_neighbers(self,node):
        neighbers=[];
        for i in range(0,8):
            j=0;
            while(j<8):
                if(j==node.poses[i]):
                    j+=1;
                    continue;
                temp=State(poses=node.poses);
                temp.poses[i]=j;
                temp.utility=self.calculate_utility(temp);
                neighbers.append(temp);
                j+=1;
        return neighbers ;

    def create_random_neighber(self,node):
        temp=State(poses=list(node.poses),utility=node.utility);
        rand_var=random.randint(0,7);
        rand_var2=random.randint(0,7);
        while(temp.poses[rand_var]==rand_var2):
            rand_var2 = random.randint(0, 7);
        temp.poses[rand_var]=rand_var2;
        temp.utility=self.calculate_utility(temp);
        return temp;

    def calculate_utility(self,node):
        utility=0;
        for i in range(0,8):
            for j in range(i+1,8):
                if (node.poses[i]==node.poses[j]):utility+=1;
                else:
                  temp=j-i;
                  temp_up= node.poses[i]+temp;
                  temp_down=node.poses[i]-temp;
                  if(node.poses[j]==temp_down):utility+=1;
                  elif (node.poses[j]==temp_up):utility+=1;
        return utility;