# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:45:02 2022

@author: Nick
"""

class LinkedList: 
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    def add_first(self, node):
        node.next = self.head 
        self.head = node
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self: 
            pass
        current_node.next = node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self: 
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with data {} not found".format(target_node_data))
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self: 
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("Node with data {} not found".format(target_node_data))            
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data
    
    
llist = LinkedList(['a','b','c','d','e'])
llist.add_first(Node('aa'))
llist.add_last(Node('f'))
llist.add_after('c', Node('cc'))
llist.add_before('c',Node('bb'))
for node in llist:
    print(node)