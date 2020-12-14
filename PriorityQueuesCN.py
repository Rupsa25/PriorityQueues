# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:33:38 2020

@author: Rupsa
"""

"""Min Priority Queue using Min heap"""
class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority
        
class PriorityQueue:
    
    def __init__(self):
        self.pq=[]
    
    def  getSize(self):
        return len(self.pq)
    
    def getMin(self):
        if self.getSize()==0:
            return None
        return self.pq[0].value
    
    
    def __percolateUp(self):
        childindex=self.getSize()-1
        while childindex>0:
            parentindex=(childindex-1)//2
            if self.pq[childindex].priority<self.pq[parentindex].priority:
                self.pq[childindex],self.pq[parentindex]=self.pq[parentindex],self.pq[childindex]
                childindex=parentindex
            else:
                break
                
        
    def insert(self,value,priority):
        newNode=PriorityQueueNode(value,priority)
        self.pq.append(newNode)
        self.__percolateUp()
            
    
    def __percolateDown(self):
        parentindex=0
        lcindex=2*(parentindex)+1
        rcindex=2*(parentindex)+2
        while lcindex<self.getSize():
            minindex=parentindex
            if self.pq[minindex].priority>self.pq[lcindex].priority:
                minindex=lcindex
            if rcindex<self.getSize()-1 and self.pq[minindex].priority>self.pq[rcindex].priority:
                minindex=rcindex
            if minindex==parentindex:
                break
            self.pq[minindex],self.pq[parentindex]=self.pq[parentindex],self.pq[minindex]
            parentindex=minindex
            lcindex=2*(parentindex)+1
            rcindex=2*(parentindex)+2
    
    
    def removeMin(self):
        if self.getSize()==0:
            return None
        element=self.pq[0].value
        self.pq[0]=self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return element
        
        