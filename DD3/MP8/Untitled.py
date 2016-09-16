
import copy
class NP_Node(object):
    
    def __init__(self, value=-1, number=0, father=None):
        self.value = value
        self.number = number
        self.father = father
        self.sons = {}
    
    
class Tree(object):
    
    def __init__(self, value=-1, father=None, item_tab=None):
        
        self.root = NP_Node(value='null', father=self)
        self.item_tab = item_tab
    
    
    def routing_added(self, routing, root_of_root, number):

        if len(routing) < 1:      
            return
        node = routing.pop(0)
        if node in root_of_root.sons:          
            follow_NP_Node = root_of_root.sons[node]          
        else:                                       
            newNP_Node = NP_Node(value=node, father=root_of_root)         
            root_of_root.sons.setdefault(node,newNP_Node)         
            follow_NP_Node = newNP_Node
        follow_NP_Node.number += number        
        if follow_NP_Node not in self.item_tab[node]:       
            self.item_tab[node].append(follow_NP_Node)
        self.routing_added(routing=routing, root_of_root=follow_NP_Node, number=number)           
        return
class Tree_generation(object):
    
    def __init__(self, routings, min_sup=-1, numbers=[], front__tab={}):
        
        self.routings = routings
        self.numbers = numbers
        self.min_sup = min_sup
        self.items = self.items_got(self.routings)          
        self.items_sorted = self.items_sorted_got(self.items)       
        self.items_tab = self.initialize__tab(front__tab)
        self.tree = self.tree_generator(self.numbers)

    def initialize__tab(self, items_tab):
        
        for item in self.items_sorted:
            items_tab.setdefault(item,[])
        return items_tab
    
    def items_got(self, routings):
        
        items = {}
        for routing in routings:
            for node in routing:
                    items.setdefault(node,0)
                    items[node] += 1
        return items
    
    
    def items_sorted_got(self, items=None):
        
        items_sorted = []
        iii = sorted(items.iteritems(), key=lambda X:X[1], reverse=True)   
        for node in iii:
            if node[1] >= self.min_sup:           
                items_sorted.append(node[0])
        return items_sorted
    
    
    def routing_sorted_got(self, routing):

        route_sorted = []
        for node in self.items_sorted:
            if node in routing:
                route_sorted.append(node)
        return route_sorted
    
    

    
    
    def tree_generator(self, numbers):
        
        tree = Tree(item_tab=self.items_tab)            
        for routing in self.routings:                         
            route_sorted = self.routing_sorted_got(routing)        
            if numbers:                      
                number = numbers.pop(0)
            else:
                number =1
            tree.routing_added(routing=route_sorted, root_of_root=tree.root, number=number)            
        return tree



class tree_analysis(object):
   
    def __init__(self, Tree=None, min_sup=-1, front__tab={}):
        
        self.min_sup = min_sup
        self.tree_analyze(Tree=Tree, front__tab=front__tab)
    
    
    def tree_analyze(self, Tree, A=[], front__tab={}):
       
        B = []
        allnode = {}       
        NP_Node = Tree.root       
        while len(NP_Node.sons) > 0:        
            if len(NP_Node.sons) != 1:         
                break
            NP_Node = NP_Node.sons.values()[0]        
            allnode.setdefault(NP_Node.value,NP_Node.number)       
        if len(NP_Node.sons) < 1:                  
            L = self.List_got(items=allnode, min_sup=self.min_sup, A=A)    
            self.result_print(L)     
            return
        else:
            for item in front__tab:           
                if A:                  
                    for node in A:
                        if node != []:
                            iii = copy.copy(node)
                            B.append(iii)
                            B.append([item]+iii)
                else:
                    B.append([item])
                patterns,numbers = self.Pattern_search(item, front__tab)     
                myfront__tab = {}          
                c_Tree_generation = Tree_generation(routings=patterns, numbers=numbers, front__tab=myfront__tab)        
                if c_Tree_generation.tree.root.sons:            
                    self.tree_analyze(Tree=c_Tree_generation.tree, A=B, front__tab=myfront__tab)       
                B = []
        return
    
    
    def Pattern_search(self, item, front__tab):
        
        pattern = []                
        numbers = []                     
        address = front__tab[item]    
        for item_of_N in address:       
            item_of_p = []               
            p_of_ns = item_of_N.father  
            if p_of_ns.value == 'null':  
                continue
            while p_of_ns.value != 'null':    
                item_of_p.append(p_of_ns.value)          
                p_of_ns = p_of_ns.father         
                
            item_of_p = tuple(item_of_p)
            pattern.append(item_of_p)             
            numbers.append(item_of_N.number)           
        return pattern,numbers
    
    
    def result_print(self, answer=[[]]):
        
        for node in answer:
            num = node.pop()        
            print tuple(node),':',num
        return
    
    
    def joint(self, liist, n): 
        
        ans = []
        a = [0] * n 
        def follow__cell(mi = 0, ni = 0): 
            if ni == n:
                ans.append(copy.copy(a))
                return
            for mi in range(mi, len(liist)):
                a[ni] = liist[mi]
                follow__cell(mi + 1, ni + 1)
        follow__cell()
        return ans
    
    
    def findmini(self, items, node):
       
        mini = items[node[0]]
        for a in node:
            if items[a] < mini:              
                mini = items[a]
        return mini
    
    
    def List_got(self, items, min_sup=-1, A=[]):
        
        iiii = []
        finnalanswer = []
        NP_Nodes = items.keys()        
        for i in range(1,len(NP_Nodes)+1): 
            iiii += self.joint(liist=NP_Nodes, n=i)
        for node in iiii[::-1]:    
            nodemini = self.findmini(items, node)  
            if nodemini < min_sup:               
                iiii.remove(node)
            else:                           
                for Anode in A:         
                    if Anode:
                        iii = node
                        iii += Anode
                        iii.append(nodemini)
                        finnalanswer.append(iii)               
        return finnalanswer

    




routings = [    
           ['Cola','Egg','Ham'],
           ['Cola','Diaper','Beer'],
           ['Cola','Beer','Diaper','Ham'],
           ['Diaper','Beer']
        ]                                 
min_sup = 2                            
front__tab = {}        

treegene = Tree_generation(routings=routings, min_sup=min_sup, front__tab=front__tab)    
tree_analysis(Tree=treegene.tree, min_sup=min_sup, front__tab=front__tab)    





