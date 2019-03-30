#ifndef ALGORITHMS_COUNTSWAPS_HPP
#define ALGORITHMS_COUNTSWAPS_HPP

#include <iostream>
#include <vector>

void countSwaps(std::vector <int> a) {
    bool sorted = false;
    int count = 0;
    while(!sorted) {
        sorted = true;
        for(int i = 0; i < a.size() - 1; i++) {
            if (a[i] > a[i+1]) {
                sorted = false;
                count++;
                std::swap(a[i], a[i+1]);
            }
        }
    }
    std::cout << "Array is sorted in " << count << " swaps.\n";
    std::cout << "First Element: " << a[0] << "\n";
    std::cout << "Last Element: " << a[a.size()-1] << "\n";
}

#endif //ALGORITHMS_COUNTSWAPS_HPP
