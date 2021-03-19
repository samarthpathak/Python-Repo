def heapify(lst,i):
    l=2*i
    r=2*i+1
    if l<=heap_size and lst[i]<lst[l]:
        largest=l
    else:
        largest=i
    if r<=heap_size and lst[r]>lst[largest]:
        largest=r
    if largest!=i:
        lst[largest],lst[i]=lst[i],lst[largest]
        heapify(lst,largest)
def build_heap(lst):
    for i in range((heap_size//2),-1,-1):
        heapify(lst,i)
def heap_sort(lst):
    global heap_size
    build_heap(lst)
    for i in range(len(lst)-1,0,-1):
        lst[i],lst[0]=lst[0],lst[i]
        heap_size-=1
        heapify(lst,0)
lst=[int(x) for x in input("Enter the list: ").split()]
heap_size=len(lst)-1
heap_sort(lst)
print("Sorted list: ",*lst,sep=" ")
