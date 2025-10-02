"""
   Leetcode exercises for Minheap and Maxheap
"""

from min_heap import MinHeap
from max_heap import MaxHeap


def find_kth_smallest(nums: list, k: int):
    """
       Find the kth smallest Value from a list
    """
    hp = MinHeap()

    for elm in nums:
        hp.insert(elm)


    for _ in range(k):
        res = hp.remove()

    return res

def stream_max(nums):
    """
       Keep track of max values in a stream
    """
    hp = MaxHeap()
    res = []
    for num in nums:
        hp.insert(num)
        mv = hp.remove()
        hp.insert(mv)
        res.append(mv)

    return res


if __name__ == "__main__":
    nums1 = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
    ks = [2, 3, 4, 7]
    expected_outputs = [2, 3, 4, 5]

    for i, test in enumerate(nums1):
        print(f'Test case {i+1}...')
        print(f'Input: {test} with k = {ks[i]}')
        result = find_kth_smallest(test, ks[i])
        print(f'Output: {result}')
        print(f'Expected output: {expected_outputs[i]}')
        print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')


    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
        ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
    ]

    for i, (nums1, expected) in enumerate(test_cases):
        result = stream_max(nums1)
        print(f'\nTest {i+1}')
        print(f'Input: {nums1}')
        print(f'Expected Output: {expected}')
        print(f'Actual Output: {result}')
        if result == expected:
            print('Status: Passed')
        else:
            print('Status: Failed')
