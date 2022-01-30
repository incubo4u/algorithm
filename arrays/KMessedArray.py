from heapq import heapify, heappop, heappush


def sort_k_messed_array(arr, k):
    length = len(arr)
    heap = arr[:k+1]
    heapify(heap)
    result_index = 0
    for i in range(k+1, length):
        arr[result_index] = heappop(heap)
        heappush(heap, arr[i])
        result_index += 1
    while heap:
        arr[result_index] = heappop(heap)
        result_index += 1
    return arr


print(sort_k_messed_array([1, 0, 3, 2], 1))
