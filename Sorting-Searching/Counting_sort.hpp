#ifndef _COUNTING_SORT_HPP_
#define _COUNTING_SORT_HPP_

#include <cstddef>
#include <vector>

int get_max(std::vector<int> &);

void counting_sort(std::vector<int> & vect)
{
    int max = get_max(vect);
    std::vector<int> count(max+1,0);
    std::vector<int> output(vect.size());

    for (int i = 0; i < vect.size(); ++i) {
        count[vect[i]]++;
    }

    for (int i = 0; i+1 < max + 1 ; ++i) {
        count[i+1] += count[i];
    }

    for (int i = vect.size() - 1; i >= 0 ; --i) { // start from end come to beginning of array
        output[count[vect[i]] - 1] = vect[i];     // with this way, provide stability
        count[vect[i]]--;
    }

    for (int i = 0; i < vect.size(); ++i) {
        vect[i] = output[i];
    }
}

int get_max(std::vector<int> & vect)
{
    int max = vect[0];
    for (int i = 0; i < vect.size(); ++i) {
        if(vect[i] > max)
            max = vect[i];
    }
    return max;
}


#endif /* _COUNTING_SORT_HPP_ */
