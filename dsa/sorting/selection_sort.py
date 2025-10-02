
def selection_sort(lst:list):
    l = len(lst)
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if lst[j] < lst[min_index]:
                min_index = j

        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]


    return lst


if __name__ == "__main__":
    print(selection_sort([4,2,6,5,1,3]))
