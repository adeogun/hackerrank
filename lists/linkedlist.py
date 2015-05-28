#!/usr/bin/env python3

class LinkedListNode:    

    def __init__(self, value):
       self._value = value
       self._next = None       

class LinkedList:    
    
    def __init__(self, value=None):
        self._head = LinkedListNode(value)
        
    def add(self, item):
        newitem = LinkedListNode(item)
        newitem._next = self._head        
        self._head = newitem
        
    def remove(self, item):
        if self._head is None:
            return
        if self._head._value == item:
            self._head = self._head._next
        else:
            self._remove(item, self._head, self._head._next)
    
    def _remove(self, item, previousNode, currentNode):
        if currentNode is None:
            return
        if currentNode._value == item:
            previousNode._next = currentNode._next            
        else:
            self._remove(item, currentNode, currentNode._next)
    
    def contains(self, item):
        if self._head is None:
            return
        return self._contains(item, self._head)   

    def _contains(self, item, node):        
        if node._value == item:
            return True
        elif node._next is None:            
            return False
        else:
            return self._contains(item, node._next)
    
    def _walk_linked_list(self, node, lists):        
        lists.append(node._value)        
        if node._next is not None:
            return self._walk_linked_list(node._next, lists)
        else:
            return lists
    
    def walk(self):                
        if self._head is None:
            return            
        return self._walk_linked_list(self._head, [])

    def count(self):        
        if self._head is None:
            return
        return self._count(self._head)
        
    def _count(self, node):        
        if node._next is None:
            return 1
        return self._count(node._next) + 1

#### USAGE
# CREATE linked = LinkedList(10)
# ADD linked.add(20)
# RETURN LIST REPRESENTATION linked.walk()
# COUNT (linked.count())
# REMOVE linked.remove(20)
