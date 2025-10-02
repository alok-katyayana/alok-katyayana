
def bubble_sort(lst:list):
    l = len(lst)
    for i in range(l):
        for j in range(l-i-1):
            if lst[j] > lst[j+1]:
                lst[j] , lst[j+1] = lst[j+1] , lst[j]

    return lst



if __name__ == "__main__":
    print(bubble_sort([4,2,6,5,1,3]))
