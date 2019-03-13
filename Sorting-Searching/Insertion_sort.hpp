#ifndef _INSERTION_SORT_HPP_
#define _INSERTION_SORT_HPP_

#include <cstddef>
#include <vector>

void insertion_sort(std::vector<int> & vect) {

    int next, j;
    for (int i = 1; i < vect.size(); ++i) {
        next = vect[i];
        for (j = i - 1; j >= 0 ; --j) {
            if (vect[j] > next)
                vect[j + 1] = vect[j];
            else
                break;
        }
        vect[j + 1] = next;
    }
}


#endif /* _INSERTION_SORT_HPP_ */
