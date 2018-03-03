# A Multi-level Linked List Implementation

This is a Multi-Level (augmented) Linked List Implementation for faster insert, remove and search methods, written in C.  List will consist of multiple levels which are directly bound to each other with their head nodes (they have key values as node counts in their own levels so that updates in levels are deterministic but they dont have datas) and these head nodes have internal nodes (which have both datas and key values) connected to them. Duplications to upper levels of the list is based on a rule which is described below.

The node definition and function prototypes are given in the header file multilevel_ll.h. The operations for the Multi-Level Linked List are returning the number of levels in the list, returning the number of nodes in the lowest level of the list, inserting node to the list, deleting node from list, finding node in list, printing the path to the any node in list, printing the contents of the list, printing only the given level in list and deleting the whole list. Their descriptions are also given in the header file. 

The list contain dummy nodes at each level. These nodes do not contain data (key:value pairs). Head node of the list connects to the first level's dummy head node in list, these dummy head nodes do not contain any values. The keys of the heads (of the levels) are used to keep information about the linked list. User will give a number when the linked list is created. This number is the branch factor number (B). This number will be kept at the list head and used in the duplication rule. The list head will also keep the number of nodes in the list (N), which is always less than 1000.

The duplications to upper levels will be decided based on the number of nodes in the list. Let’s say, when you insert a new node there will be N nodes in the linked list with the branch factor B, here are the rules:
• If B does not divide N, the new node will only be inserted to the lowest level.
• If some BD divides N, the new node will be inserted to all D levels above the lowest level.
When B=2:
if N is odd, only insert to level 0
if N = 2(2 == 21), insert to levels 0 and 1 if N = 4(4 == 22), insert to levels 0, 1, 2
if N = 6(6%21 == 0), insert to levels 0 and 1 if N = 8(8 == 23), insert to levels 0, 1, 2, 3
if N = 12(12%22 == 0), insert to levels 0, 1, 2 if N = 16(16 == 24), insert to 0, 1, 2, 3, 4

Some Example usages of the operations:

node *list = init(2);

clear(list);

printf("is_empty: %d\n", is_empty(list));	printf("num_levels: %d\n", num_levels(list));	printf("num_nodes: %d\n", num_nodes(list));

	is_empty: 0
	num_levels: 4
	num_nodes: 10

insert(list, 123, "abc");

delete(list, 123);

print_level(list, 2);

					   890: htv ->
						  |
	-2: -> 456: rqe -> 890: htv ->

node = find(list, 234);

print(list);
path(list, 234);
path(list, 1);
path(list, 678);
path(list, 901);
	
	11 0 1 2 3
	+ + + + -
	1: ilk +
	12: bnm + +
	123:abcty +
	234:cdehg + + +
	345: werf +
	456: rqe + +
	567: rr +
	678: y + + + +
	789: rtrd +
	890: htv + +
	901:bghdf +
	2011 v -3 v -2 > 234:cdehg
	2011 v -3 v -2 v -1 v 0 > 1: ilk
	2011 v -3 > 678: y
	2011 v -3 > 678 v 678 v 678 > 890 v 890 > 901:bghdf

