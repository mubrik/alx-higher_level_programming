#!/usr/bin/python3
""" Node Class """


class SinglyLinkedList:
    """ Node class with priv attri """

    def __init__(self):
        """ initialization method """
        self.__head = None

    def __str__(self):
        """ magic method for printing """
        tmp_head = self.__head
        str = ""
        while tmp_head:
            delim = "\n" if tmp_head.next_node else ""
            str = f"{str}{tmp_head.data}{delim}"
            tmp_head = tmp_head.next_node
        return str

    def __repr__(self):
        """ magic method for class repr """
        return f"<Class SinglyLinkedList, len: {self.__len__()}"

    def __len__(self):
        """ magic method for clen """
        if self.__head is None:
            return 0
        count = 0
        tmp_head = self.__head
        while tmp_head:
            count += 1
            tmp_head = tmp_head.next_node
        return count

    def is_empty(self):
        """ checkif list is empty """
        return self.__head is None

    def sorted_insert(self, value):
        """ sort and insert method """
        # create node, safe, will raise error if bad value.
        node = Node(value, None)
        if self.is_empty():
            # insert at start
            self.__head = node
            return 0
        tmp_head = self.__head
        prev = None
        # iterate head
        while tmp_head:
            if node.data <= tmp_head.data:
                # insert before
                node.next_node = tmp_head
                if prev:
                    prev.next_node = node
                else:
                    # start
                    self.__head = node
                return 0
            # if next node is none last node, break
            if tmp_head.next_node is None:
                break
            prev = tmp_head
            tmp_head = tmp_head.next_node
        # node data larger than entire list, insert after
        tmp_head.next_node = node
        return 0


class Node:
    """ Node class with priv attri """

    def __init__(self, data, next_node=None, *args, **kwargs):
        """ initialization method """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter method for data """
        return self.__data

    @property
    def next_node(self):
        """ getter method for next_node """
        return self.__next_node

    @data.setter
    def data(self, value):
        """ setter method for data """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @data.deleter
    def data(self):
        """ deleter method for data """
        del self.__data

    @next_node.setter
    def next_node(self, next_node):
        """ setter method for next_node """
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @next_node.deleter
    def next_node(self):
        """ deleter method for next_node """
        del self.__next_node
