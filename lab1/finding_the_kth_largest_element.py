"""Module main-"""


def finding_the_kth_largest_element(array, k):
    """Function to find the k-th largest element in a given array of integers"""
    copy_array = array[:]

    if k <= 0 or k > len(array):
        print(f"k - is larger than array length or less than zero ")
        return None

    def partition(array, left, right):
        pivot = array[right]
        i = left-1
        for j in range(left, right):
            if array[j] >= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[right] = array[right], array[i + 1]
        return i + 1

    def kth_larger_sort(array, left, right, k):
        if left <= right:
            pivot_index = partition(array, left, right)
            if pivot_index == k - 1:
                return search_index_of_elem(copy_array, array[pivot_index])
            elif pivot_index > k - 1:
                return kth_larger_sort(array, left, pivot_index - 1, k)
            else:
                return kth_larger_sort(array, pivot_index + 1, right, k)

    def search_index_of_elem(array, element):
        for i in range(len(array)):
            if array[i] == element:
                index = i
        return element, index

    result, index = kth_larger_sort(array, 0, len(array) - 1, k)
    print(f"k’th larger array element is - {result}, his index is - {index}")
    return result, index

if __name__ == '__main__':
    array = [14, 45, 0, 4, 30, 35, 1, 88, 110]
    k = 3
    result = finding_the_kth_largest_element(array, k)
