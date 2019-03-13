# Multi-level Linked List 

This is a Multi-Level (augmented) Linked List Implementation for faster insert, remove and search methods, written in C.  List will consist of multiple levels which are directly bound to each other with their head nodes (they have key values as node counts in their own levels so that updates in levels are deterministic but they dont have datas) and these head nodes have internal nodes (which have both datas and key values) connected to them. Duplications to upper levels of the list is based on a rule which is described below.

The node definition and function prototypes are given in the header file ```multilevel_ll.h``` 

The operations for the Multi-Level Linked List are returning the number of levels in the list, returning the number of nodes in the lowest level of the list, inserting node to the list, deleting node from list, finding node in list, printing the path to the any node in list, printing the contents of the list, printing only the given level in list and deleting the whole list. Their descriptions are also given in the header file. 

