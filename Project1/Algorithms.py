

class Algorithmes:
    def __init__(self,problem):
        self.problem=problem;
        self.f_list=[];
        self.e_list=[];
        self.num_nodes=0;
        self.max_nodes=0;
        self.num_expansion=0;

    def BFS_tree(self):
        self.f_list=self.problem.initialize();
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list)>0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            children=self.problem.expand(self.f_list.pop(0));
            self.num_expansion+=1;
            for i in children:
                self.num_nodes += 1;
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
            self.f_list.extend(children);
        print("no solution found");
        return None;

    def BFS_graph(self):
        self.f_list = self.problem.initialize();
        self.e_list=[];
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            node = self.f_list.pop(0);
            self.e_list.append(node);
            children = self.problem.expand(node);
            self.num_expansion+=1;
            for i in children:
                if (self.check_e(i) or self.check_f(i)):
                    continue;
                self.num_nodes += 1;
                self.f_list.append(i);
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
        print("no solution found");
        return None;

    def DFS_tree(self):
        self.f_list=self.problem.initialize();
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list)>0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            children=self.problem.expand(self.f_list.pop());
            self.num_expansion+=1;
            for i in children:
                self.num_nodes += 1;
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
            self.f_list.extend(children);
        print("no solution found");
        return None;

    def DFS_graph(self):
        self.f_list = self.problem.initialize();
        self.e_list = [];
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            node = self.f_list.pop();
            self.e_list.append(node);
            self.num_expansion+=1;
            children = self.problem.expand(node);
            for i in children:
                if (self.check_e(i) or self.check_f(i)):
                    continue;
                self.f_list.append(i);
                self.num_nodes += 1;
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
        print("no solution found");
        return None;

    def DLDFS_tree(self,depth):
        self.f_list = self.problem.initialize();
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            children = self.problem.expand(self.f_list.pop());
            for i in children:
                if (i.depth>depth):
                    continue;
                self.f_list.append(i);
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
        print("no solution found");
        return None;

    def DLDFS_graph(self,depth):
        self.f_list = self.problem.initialize();
        self.e_list = [];
        if (self.problem.Goal_test(self.f_list[0])):
            return self.problem.Solution(self.f_list[0]);
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            node = self.f_list.pop();
            self.e_list.append(node);
            children = self.problem.expand(node);
            for i in children:
                if (self.check_e(i) or self.check_f(i) or i.depth>depth ):
                    continue;
                self.f_list.append(i);
                if (self.problem.Goal_test(i)):
                    return self.problem.Solution(i);
        print("no solution found");
        return None;

    def IDDFS_tree(self,max_depth):
        depth=0;
        while (depth<=max_depth):
            self.f_list = self.problem.initialize();
            if (self.problem.Goal_test(self.f_list[0])):
                return self.problem.Solution(self.f_list[0]);
            while (len(self.f_list) > 0):
                if (len(self.f_list) > self.max_nodes): self.max_nodes = len(self.f_list);
                self.num_nodes += 1;
                children = self.problem.expand(self.f_list.pop());
                for i in children:
                    if (i.depth > depth):
                        continue;
                    self.f_list.append(i);
                    if (self.problem.Goal_test(i)):
                        return self.problem.Solution(i);
            depth+=1;
        print("no solution found");
        return None;

    def IDDFS_graph(self,max_depth):
        depth=0;
        while (depth<=max_depth):
            self.e_list=[];
            self.f_list = self.problem.initialize();
            if (self.problem.Goal_test(self.f_list[0])):
                return self.problem.Solution(self.f_list[0]);
            while (len(self.f_list) > 0):
                if (len(self.f_list) > self.max_nodes): self.max_nodes = len(self.f_list);
                self.num_nodes += 1;
                node = self.f_list.pop();
                self.e_list.append(node);
                children = self.problem.expand(node);
                for i in children:
                    if (self.check_e(i) or self.check_f(i) or i.depth > depth):
                        continue;
                    self.f_list.append(i);
                    if (self.problem.Goal_test(i)):
                        return self.problem.Solution(i);
            depth+=1;
        print("no solution found");
        return None;

    def BID_tree(self):
        pass;
    def BID_graph(self):
        pass;

    def UFC_tree(self):
        self.f_list = self.problem.initialize();
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            node=self.f_list.pop(0);
            if (self.problem.Goal_test(node)):
                return self.problem.Solution(node);
            children = self.problem.expand(node);
            for i in children:
                self.insert_with_cost(i);
        print("no solution found");
        return None;
    def UFC_graph(self):
        self.e_list=[];
        self.f_list = self.problem.initialize();
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            node = self.f_list.pop(0);
            self.e_list.append(node);
            if (self.problem.Goal_test(node)):
                return self.problem.Solution(node);
            children = self.problem.expand(node);
            for i in children:
                self.insert_with_cost(i);
        print("no solution found");
        return None;
    def Astar_tree(self):
        self.f_list = self.problem.initialize();
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            node = self.f_list.pop(0);
            if (self.problem.Goal_test(node)):
                return self.problem.Solution(node);
            children = self.problem.expand(node);
            for i in children:
                self.insert_with_heuristic(i);
        print("no solution found");
        return None;
    def Astar_graph(self):
        self.e_list = [];
        self.f_list = self.problem.initialize();
        while (len(self.f_list) > 0):
            if (len(self.f_list)+len(self.e_list)>self.max_nodes):self.max_nodes=len(self.f_list)+len(self.e_list);
            self.num_nodes+=1;
            node = self.f_list.pop(0);
            self.e_list.append(node);
            self.num_expansion+=1;
            if (self.problem.Goal_test(node)):
                return self.problem.Solution(node);
            children = self.problem.expand(node);
            for i in children:
                self.insert_with_heuristic(i);
        print("no solution found");
        return None;

    def check_e(self,child):
        for i in self.e_list:
            if (self.problem.check_state(i,child)):
                return True;
        return False;

    def check_f(self,child):
        for i in self.f_list:
            if (self.problem.check_state(i, child)):
                return True;
        return False;

    def insert_with_cost(self,child):
        if (self.check_e(child)):
                return;
        k=0;
        for i in self.f_list:
            if (self.problem.check_state(i, child)):
                if(child.cost>=i.cost):
                  return ;
                self.f_list.pop(k);
                self.insert_with_cost(child);
                return;
            k+=1;
        k = 0;
        for i in self.f_list:
                if (child.cost <= i.cost):
                    self.f_list.insert(k,child);
                    return ;
                k += 1;
        self.f_list.insert(k, child);
        return ;

    def insert_with_heuristic(self, child):
        if (self.check_e(child)):
            return;
        k = 0;
        for i in self.f_list:
            if (self.problem.check_state(i, child)):
                if (child.heu >= i.heu):
                    return;
                self.f_list.pop(k);
                self.num_nodes -= 1;
                self.insert_with_heuristic(child);
                return;
            k += 1;
        k = 0;
        self.num_nodes += 1;
        for i in self.f_list:
            if (child.heu <= i.heu):
                self.f_list.insert(k, child);
                return;
            k += 1;
        self.f_list.insert(k, child);
        return;
