
def insertion_sort(lst:list):
    for i in range(1,len(lst)):
        j = i-1
        while j > -1 and lst[i] < lst[j] :
            lst[i], lst[j] = lst[j], lst[i]
            i = j
            j = i - 1



    return lst


if __name__ == "__main__":
    print(insertion_sort([4,2,6,5,1,3]))
