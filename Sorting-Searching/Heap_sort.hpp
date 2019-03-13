#ifndef _HEAP_SORT_HPP_
#define _HEAP_SORT_HPP_

#include <cstddef>
#include <vector>

void build_heap(std::vector<int> &, int, int);

void heap_sort(std::vector<int> & vect)
{
    for (int i = vect.size() / 2 - 1; i >= 0; i--) // first build heap from array with an
        build_heap(vect, vect.size(), i);           // initial index of i = length / 2 - 1

    for (int i = vect.size() - 1; i >= 0 ; i--) // One by one get the maximum element from the heap (arr[0])
    {                                     // and swap it with last index of the array (arr[i])
        std::swap(vect[0],vect[i]);
        build_heap(vect, i, 0);  // fix max heap again with the swapped root (i = new length, 0 = index of whole tree)
    }
}

void build_heap(std::vector<int> & vect, int length, int parent_index) {
    int left_child = (2 * parent_index) + 1;
    int right_child = (2 * parent_index) + 2;
    int greater_index; // index of the greater child

    if (right_child < length) // both children exist
    {
        greater_index = (vect[left_child] > vect[right_child]) ? left_child : right_child;
        if (vect[greater_index] > vect[parent_index])
        {
            std::swap(vect[parent_index],vect[greater_index]);
            // Recursively fix affected sub-tree
            build_heap(vect, length, greater_index);
        }
    }
    else if (left_child < length) // right child does not exist
    {
        greater_index = left_child;
        if (vect[greater_index] > vect[parent_index])
        {
            std::swap(vect[parent_index],vect[greater_index]);
            // Recursively fix affected sub-tree
            build_heap(vect, length, greater_index);
        }
    }
    else // there is no child left
        return;
}

#endif /* _HEAP_SORT_HPP_ */
