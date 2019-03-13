#ifndef _RADIX_SORT_HPP_
#define _RADIX_SORT_HPP_

#include <cstddef>
#include <vector>

int get_max(std::vector<int> &);
void cs_radix(std::vector<int> &,int);

void radix_sort(std::vector<int> & vect)
{
    int max = get_max(vect);
    for (int exp = 1; max/exp > 0 ; exp *=10)
        cs_radix(vect,exp);
}

void cs_radix(std::vector<int> & vect, int exp)
{
    std::vector<int> count(10,0);
    std::vector<int> output(vect.size());
    int len = vect.size();


    for (int i = 0; i < vect.size(); ++i)
        count[(vect[i]/exp)%10]++;

    for (int i = 0; i+1 < 10; ++i)
        count[i+1] += count[i];

    for (int i = len - 1; i >= 0 ; --i) {
        output[count[(vect[i]/exp)%10] - 1] = vect[i];
        count[(vect[i]/exp)%10]--;
    }

    for (int i = 0; i < vect.size(); ++i)
        vect[i] = output[i];
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


#endif /* _RADIX_SORT_HPP_ */





