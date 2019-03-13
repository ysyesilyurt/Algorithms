#ifndef _MERGE_SORT_HPP_
#define _MERGE_SORT_HPP_

#include <cstddef>
#include <vector>


void merge_sort(std::vector<int> &, int, int);
void merge(std::vector<int> &, int, int, int);


void merge_sort(std::vector<int> & vect) { // function overloading for calling
    merge_sort(vect, 0, vect.size() - 1);  // merge sort with right parameters
}

void merge_sort(std::vector<int> & vect, int start_index, int end_index) {

    if (start_index < end_index) {
        merge_sort(vect, start_index, (end_index + start_index) / 2); // middle = (end + start)/2
        merge_sort(vect, (end_index + start_index) / 2 + 1, end_index); // second subarray may be smaller than first
        merge(vect, start_index, (end_index + start_index) / 2, end_index);
    }
}

void merge(std::vector<int> & vect, int first, int middle, int last) {

    int len1 = middle - first + 1, len2 = last - middle;
    int arr_index = first, arr1_index = 0, arr2_index = 0;
    std::vector<int> arr1(len1), arr2(len2);

    for (int l = 0; l < len1; ++l) {
        // fill arr1 with first half
        arr1[l] = vect[first + l];
    }
    for (int l = 0; l < len2; ++l) {
        // fill arr2 with second half
        arr2[l] = vect[middle + 1 + l];
    }

    while ((arr1_index < len1) && (arr2_index < len2))
    {
        // merge arr1 and arr2 to arr in a sorted manner
        if (arr1[arr1_index] <= arr2[arr2_index]) {
            vect[arr_index] = arr1[arr1_index];
            arr_index++;
            arr1_index++;
        }
        else {
            vect[arr_index] = arr2[arr2_index];
            arr_index++;
            arr2_index++;
        }
    }

    if (arr1_index < len1) {
        // if arr1 has some remaining numbers push them to vect
        for (; arr1_index < len1; ++arr1_index, ++arr_index) {
            vect[arr_index] = arr1[arr1_index];
        }
    }
    else {
        // if arr2 has some remaining numbers push them to vect
        for (; arr2_index < len2; ++arr2_index, ++arr_index) {
            vect[arr_index] = arr2[arr2_index];
        }
    }
}


#endif /* _MERGE_SORT_HPP_ */
