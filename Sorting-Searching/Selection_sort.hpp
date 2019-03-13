#ifndef _SELECTION_SORT_HPP_
#define _SELECTION_SORT_HPP_

#include <cstddef>
#include <vector>

void selection_sort(std::vector<int> & vect)
{
    int min_index;
    for (int i = 0; i < vect.size(); ++i) {
        min_index = i;
        for (int j = i + 1; j < vect.size(); ++j) {
            if (vect[j] < vect[min_index])
                min_index = j;
        }
        std::swap(vect[min_index],vect[i]);
    }
}


#endif /* _SELECTION_SORT_HPP_ */
