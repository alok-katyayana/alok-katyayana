"""
   Exercises related to Leetcode!
"""

## I will use inbuilt hash table, dictionary

def item_in_common(l1: list, l2: list):
    """
       return common items in two lists.
    """
    empty_dict = {}

    for elm in l1:
        empty_dict[elm] = True

    for elm1 in l2:
        val = empty_dict.get(elm1)
        if val is not None:
            yield val

def find_duplicates(nums:list):
    """
       return duplicate items in the lists.
    """
    ed = {}

    for elm in nums:
        ed[elm] = ed.get(elm,0) + 1

    for key, value in ed.items():
        if value > 1:
            yield key

def first_non_repeating_char(s:str):
    """
       return first non repeating character from a string.
    """
    ed = {}

    for c in s:
        ed[c] = ed.get(c,0) + 1

    res_item = None
    for k,v in ed.items():
        if v == 1:
            res_item = k
            break
    return res_item

def group_anagrams(lst:list[str]):
    """
       Return all the anagrams from a string (words need not be meaningful)
    """
    ed = {}
    for elm in lst:
        v = 0
        for c in elm:
            v += ord(c)

        if ed.get(v) is None:
            ed[v] = [elm]
        else:
            ed[v].append(elm)

    return list(ed.values())

def two_sum(nums: list, target: int):
    """
       return two numbers whose sum matches target
    """
    ed = {}
    lst = []
    for i,elm in enumerate(nums):
        next_i = ed.get(target-elm)
        if next_i is not None: 
            lst.extend([ ed[target-elm], i])
            return lst
        ed[elm] = i

    return lst

def subarray_sum(nums, target):
    """
       Brute Force Solution: Sub array whose sum is target
    """
    for i in range(nums):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) == target:
                return [i, j]

    return []





if __name__ == "__main__":
    list1 = [1,3,6]
    list2 = [2,4,5]


    print(list(item_in_common(list1, list2)))
    vals = [1,2,3,4,5,4,5,4,5]

    res = find_duplicates(vals)
    print(list(res))


    print( first_non_repeating_char('leetcode') )

    print( first_non_repeating_char('hello') )

    print( first_non_repeating_char('aabbcc') )

    print("1st set:")
    print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

    print("\n2nd set:")
    print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

    print("\n3rd set:")
    print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )


    print(two_sum([5, 1, 7, 2, 9, 3], 10))
    print(two_sum([4, 2, 11, 7, 6, 3], 9))
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    print(two_sum([1, 3, 5, 7, 9], 10))
    print ( two_sum([1, 2, 3, 4, 5], 10) )
    print ( two_sum([1, 2, 3, 4, 5], 7) )
    print ( two_sum([1, 2, 3, 4, 5], 3) )
    print ( two_sum([], 0) )

    nums1 = [1, 2, 3, 4, 5]
    TARGET1 = 9
    print ( subarray_sum(nums1, TARGET1) )

    nums1 = [-1, 2, 3, -4, 5]
    TARGET1 = 0
    print ( subarray_sum(nums1, TARGET1) )

    nums1 = [2, 3, 4, 5, 6]
    TARGET1 = 3
    print ( subarray_sum(nums1, TARGET1) )

    nums1 = []
    TARGET1 = 0
    print ( subarray_sum(nums1, TARGET1) )
