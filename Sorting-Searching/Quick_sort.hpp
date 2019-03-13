#ifndef _QUICK_SORT_HPP_
#define _QUICK_SORT_HPP_

#include <cstddef>
#include <vector>

void partition(std::vector<int>&,int,int,int&);
void helper_qs(std::vector<int>&,int,int);

void quick_sort(std::vector<int> & vect)
{
    int start = 0;
    int end = vect.size();
    helper_qs(vect,start,end);
}

void helper_qs(std::vector<int>& vect,int start,int end)
{
    int pivot;
    if (start < end)
    {
        partition(vect,start,end,pivot);
        helper_qs(vect,start,pivot-1);
        helper_qs(vect,pivot+1,end);
    }
}

void partition(std::vector<int>& vect,int start,int end,int & pivot)
{
    pivot = start;
    int i = start;
    int j = i + 1;
    for (; j < end ; j++) {
        if(vect[j] < vect[pivot])
        {
            i++;
            std::swap(vect[i],vect[j]);
        }
    }
    std::swap(vect[pivot],vect[i]);
    pivot = i;
}

#endif /* _QUICK_SORT_HPP_ */
