#ifndef _BUBBLE_SORT_HPP_
#define _BUBBLE_SORT_HPP_

#include <cstddef>
#include <vector>

void bubble_sort(std::vector<int> vect)
{
    bool sorted = false;
    while (!sorted)
    {
        sorted = true;
        for (int i = 0; i+1 < vect.size(); ++i) {
            if (vect[i] > vect[i+1] )
            {
                sorted = false;
                std::swap(vect[i],vect[i+1]);
            }
        }
    }
}


#endif /* _BUBBLE_SORT_HPP_ */
