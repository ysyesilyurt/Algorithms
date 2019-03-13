#ifndef _SHELL_SORT_HPP_
#define _SHELL_SORT_HPP_

#include <cstddef>
#include <vector>

void shell_sort(std::vector<int> & vect, int length) {
    int next,k;
    for (int h = length / 3; h > 0; h /= 3) // h = gap size between subarrays, will be divided by 3 on each loop
    {
        for (int i = 0; i < h; ++i) // to be able to sort all gapped subarrays first i = 0 to h index
        {                           // will be used as 'first index' for corresponding subarrays
            for (int j = h + i; j < length; j+=h+i) {   // Insertion sort for gapped subarrays
                next = vect[j]; // get the next unsorted number
                k = j - (h + i); // start comparison from previous index
                for (; k >= 0; k-=h+i) {
                    if (next < vect[k])
                        vect[k + (h+i)] = vect[k]; // swap as long as needed
                    else
                        break;
                }
                vect[k + (h + i)] = next; // put the number to its rightful place
            }

        }
    }
}


#endif /* _SHELL_SORT_HPP_ */
