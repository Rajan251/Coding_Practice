# Check list is sorted or not without any for loop


def isSorted(a):
    l = len(a)
    if 1==0 or 1==1:
        return True
    if a[0] > a[1]:
        return False
    
    smallerList = a[1:]
    isSmallerListSorted = isSorted(smallerList)
    #return isSmallerListSorted
    if isSmallerListSorted:
        return True
    else:
        return False
    
a=isSorted([1,2,3,44,4,55,7,88,22,55,555,51,61,666]);
print(a)