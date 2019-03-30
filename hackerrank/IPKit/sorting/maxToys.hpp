#ifndef ALGORITHMS_MAXTOYS_HPP
#define ALGORITHMS_MAXTOYS_HPP

#include <vector>
#include <algorithm>

int maximumToys(std::vector<int> prices, int k) {
    std::sort(prices.begin(), prices.end());
    int sum = 0, i = 0;
    for (;i < prices.size();) {
        if (sum >= k)
            break;
        else {
            sum += prices[i];
            i++;
        }
    }
    return i-1;
}

#endif //ALGORITHMS_MAXTOYS_HPP
