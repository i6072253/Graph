# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:07:25 2016

@author: Mok
"""


class arc:
    def __init__(self,coord_x,coord_y,distance):
            self.dist = distance
            self.x = coord_x
            self.y = coord_y
            self._connected = False

class graph:        
    
    def __init__(self):
        self._edges = []
        self._vertices = []
        self._arcs = []

    def add_vertices_and_edges(self,a):
        self._vertices.append(a[0])
        self._edges.append(a[1]+a[2])
        n = arc(a[0],a[1],a[2])
        self._arcs.append(n)
    
    def write_graph(self,name):
        file_handle = open(name,'x')
        file_handle.close()
    
    def load_graph(self,file):
        file_handle = open(file,'r')
        for line in file_handle:
            for i in line.split(" "):
                a= []
                for j in i.split(","):
                    a.append(int(j))
                self.add_vertices_and_edges(a)      
        file_handle.close()
        
    def connectedness(self):
        check = set()
        i = self._arcs[0]
        check.add(i.x)
        check.add(i.y)
        self._arcs[0]._connected=True
        for i in self._arcs:
            j = 0
            while j < len(self._arcs) and i._connected == False:
                if self._arcs[j].x in check or self._arcs[j].y in check:
                    check.add(self._arcs[j].x)
                    check.add(self._arcs[j].y)
                    self._arcs[j]._connected = True   
                j += 1
            print(check)
            if i._connected == False:
                return False
        return True       
    
    #def  min_tree(self):
    
tree = graph()
tree.load_graph('test.txt') 
print(tree.connectedness())  
        
    