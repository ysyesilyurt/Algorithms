#!/usr/bin/env python3

# A Python function to solve towers of hanoi puzzle

# A high-level outline of the algorithm is as follows:
#    Move height-1 disks from source rod to auxiliary rod, using the destination rod.
#    Move last disk to from source rod to destination rod.
#    Move height-1 disks from auxiliary rod to destination rod, using the source rod.

def towersofHanoi(n=3, source_rod='A', aux_rod='B', dest_rod='C'):

    '''
    :param n: number of the disks (default = 3)
    :param source_rod: name of the source rod (default = 'A')
    :param aux_rod: name of the auxiliary rod (default = 'B')
    :param dest_rod: name of the destination rod (default = 'C')
    :return: there is no return value, function just prints moves of the disks
    '''

    if n == 1:
        moveDisk(n, source_rod, dest_rod)
        return
    towersofHanoi(n - 1, source_rod, dest_rod, aux_rod)
    moveDisk(n, source_rod, dest_rod)
    towersofHanoi(n - 1, aux_rod, source_rod, dest_rod)

def moveDisk(disk_number, source_rod, dest_rod):
    '''
    Helper print function for towerofHanoi
    '''
    print "Moving disk ", disk_number, " from ", source_rod, " to ", dest_rod


