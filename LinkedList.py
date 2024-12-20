#!/usr/bin/python3
# *******************************************************************************************************
# linked_list.py - The code defines two classes: Node and LinkedList.
#
# Node Class - This class is used to create a new node. Each node has two attributes:
#   data: It stores the data of the node.
#   next: It is a pointer that points to the next node in the linked list. By default, it is set to None.
#
# LinkedList Class - This class creates a new linked list. It has two methods:
#   insert(data): This method inserts a new node at the end of the linked list. If the linked list is empty
#   (i.e., the head is None), it will add a new node as the head. Otherwise, it will append the new node at
#   the end.
#
# display(): This method returns all the elements in the linked list. It starts from the head of the
#   linked list and traverses through the linked list until it reaches the end (i.e., None). It adds
#   the data of each node to the element list.
#
# ASC and DESC: These are class-level attributes defined in the LinkedList class. They are used to specify
#   the sort order in the sort method. ASC stands for ascending order, and DESC stands for descending order.
#   You can refer to these attributes as LinkedList.ASC and LinkedList.DESC when you call the sort method.
#
# sort method: This is a method of the LinkedList class. It sorts the linked list in either ascending or
#   descending order, depending on the argument passed to it. The method takes one argument, order, which
#   should be either LinkedList.ASC or LinkedList.DESC. If order is LinkedList.ASC, the method sorts the
#   linked list in ascending order. If order is LinkedList.DESC, the method sorts the linked list in
#   descending order. The method uses a simple bubble sort algorithm to sort the linked list. If the order
#   argument is not LinkedList.ASC or LinkedList.DESC, the method prints an error message and returns.
#
# The usage example creates a linked list, inserts the numbers 1, 2, and 3 into the list, and then prints
# these numbers. The output of the print statement is [1, 2, 3], which are the elements of the linked list.
# -------------------------------------------------------------------------------------------------------
# Author:       Patrik Eigenmann
# eMail:        p.eigenmann@gmx.net
# -------------------------------------------------------------------------------------------------------
# Sun 2023-12-31 File created.                                                              Version: 00.01
# Fri 2024-01-05 Add variables static ASC/DESC and the method sort.                         Version: 00.02
# Fri 2024-01-05 Add parameter to sort and the methods bubble sort and quick sort.          Version: 00.03
# *******************************************************************************************************

class Node: 
    """
    A class representing a node in a linked list.
    This class is designed to store data and a reference to the next node in the linked list, forming
    the building blocks of the linked list structure.
    """
    
    def __init__(self, data=None):
        """
        Initialize a node with given data and set the next node to None.
        This constructor sets the `data` attribute to the provided value and initializes the `next`
        attribute to None. The `next` attribute is used to link to the next node in the linked list,
        enabling the creation of a chain of nodes.
        
        Args:
        data (any, optional): The data to store in the node. Default is None.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list with sorting capabilities.
    This class allows for insertion of nodes, displaying the list, and sorting the list using either
    bubble sort or quick sort algorithms. It supports sorting in ascending or descending order.
    """
    
    ASC = "asc"
    DESC = "desc"
    BUBBLE_SORT = "bubble_sort"
    QUICK_SORT = "quick_sort"

    def __init__(self):
        """
        Initialize an empty linked list.
        This constructor sets the head of the linked list to None, indicating that the list is initially empty.
        """
        self.head = None

    def insert(self, data):
        """
        Insert a new node with the given data into the linked list.
        This method creates a new node with the provided data and adds it to the end of the linked list.

        Args:
            data (any): The data to be stored in the new node.
        """
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        """
        Display the data in the linked list as a list.
        This method traverses the linked list and collects the data from each node, returning it as a list.
        
        Returns:
            list: A list containing all the data elements in the linked list.
        """
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.next
        return elements

    def sort(self, order, algorithm):
        """
        Sort the linked list using the specified order and algorithm.
        This method sorts the linked list according to the specified order and algorithm. It supports both
        bubble sort and quick sort algorithms for sorting.
        
        Args:
            order (str): The order in which to sort the list. Must be either 'asc' or 'desc'.
            algorithm (str): The sorting algorithm to use. Must be either 'bubble_sort' or 'quick_sort'.
        """
        if self.head is None:
            return

        if order not in [self.ASC, self.DESC]:
            print(f"Order must be either '{self.ASC}' or '{self.DESC}'")
            return

        if algorithm == self.BUBBLE_SORT:
            self.bubble_sort(order)
        elif algorithm == self.QUICK_SORT:
            self.head = self.quick_sort(self.head, order)
        else:
            print(f"Algorithm must be either '{self.BUBBLE_SORT}' or '{self.QUICK_SORT}'")

    def bubble_sort(self, order):
        """
        Perform bubble sort on the linked list.

        Args:
            order (str): The order in which to sort the list. Must be either 'asc' or 'desc'.

        This method sorts the linked list using the bubble sort algorithm in the specified order.
        """
        swapped = True
        while swapped:
            swapped = False
            node = self.head
            while node.next:
                if (order == self.ASC and node.data > node.next.data) or (order == self.DESC and node.data < node.next.data):
                    node.data, node.next.data = node.next.data, node.data
                    swapped = True
                node = node.next

    def quick_sort(self, head, order):
        """
        Perform quick sort on the linked list.
        This method sorts the linked list using the quick sort algorithm in the specified order.

        Args:
            head (Node): The head node of the sublist to sort.
            order (str): The order in which to sort the list. Must be either 'asc' or 'desc'.

        Returns:
            Node: The head node of the sorted sublist.
        """
        if head is None or head.next is None:
            return head

        pivot_prev = None
        pivot = head
        node = head
        while node:
            if (order == self.ASC and node.data < pivot.data) or (order == self.DESC and node.data > pivot.data):
                if pivot_prev:
                    pivot_prev.next = node.next
                else:
                    head = node.next
                node.next = pivot
                pivot_prev = node
                node = pivot.next
            else:
                pivot_prev = pivot
                pivot = pivot.next
                node = node.next

        head = self.quick_sort(head, order)
        pivot.next = self.quick_sort(pivot.next, order)
        return head

# Usage
linked_list = LinkedList()
linked_list.insert(3)
linked_list.insert(23)
linked_list.insert(1)

print(linked_list.display())  # Output: [1, 2, 3]

linked_list.sort(LinkedList.ASC, LinkedList.BUBBLE_SORT)

print(linked_list.display())  # Output: [1, 2, 3]

linked_list.sort(LinkedList.DESC, LinkedList.BUBBLE_SORT)

print(linked_list.display())  # Output: [1, 2, 3]