#ifndef _BINARY_SEARCH_HPP_
#define _BINARY_SEARCH_HPP_

#include <cstddef>
#include <vector>

int binary_search(std::vector<int>& vect, int num)
{
    int start = 0;
    int end = vect.size();
    int mid;
    while (start <= end)
    {
        mid = (start + end) / 2;
        if(vect[mid] == num)
            return mid;
        else if(vect[mid] < num)
            start = mid + 1;
        else if(vect[mid] > num)
            end = mid - 1;
    }
}

#endif /* _BINARY_SEARCH_HPP_ */
