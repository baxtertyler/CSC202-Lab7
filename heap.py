class MaxHeap:

    def __init__(self, capacity=50):
        '''Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created.'''
        self.cap = capacity
        self.heap = [None] * (self.cap+1)

    def enqueue(self, item):
        '''inserts "item" into the heap, returns true if successful, false if there is no room in the heap
           "item" can be any primitive or ***object*** that can be compared with other 
           items using the < operator'''
        # Should call perc_up
        if self.is_full():
            return False
        else:
            self.heap[self.get_size()+1] = item
            self.perc_up(self.get_size())
            return True

    def peek(self):
        '''returns max without changing the heap, returns None if the heap is empty'''
        if self.get_size() == 0:
            return None
        return self.heap[1]

    def dequeue(self):
        '''returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty'''
        # Should call perc_down
        if self.get_size() == 0:
            return None
        root = self.heap[1]
        self.heap[1] = self.heap[self.get_size()]
        self.heap[self.get_size()] = None
        self.perc_down(1)
        return root

    def contents(self):
        '''returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)'''
        l = []
        for i in range(1, len(self.heap), 1):
            if self.heap[i] is not None:
                l.append(self.heap[i])
        return l

    def build_heap(self, alist):
        '''Discards all items in the current heap and builds a heap from 
        the items in alist using the bottom-up construction method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased to accommodate 
        exactly the number of items in alist'''
        # Bottom-Up construction.  Do NOT call enqueue
        for i in range(len(alist)):
            try:
                self.heap[i + 1] = alist[i]
            except IndexError:
                self.cap += 1
                self.heap.append(alist[i])
        j = 0
        while True:
            j += 1
            if j > self.get_size():
                break
            self.perc_up(j)

    def is_empty(self):
        '''returns True if the heap is empty, false otherwise'''
        for i in range(self.cap):
            if self.heap[i] is not None:
                return False
        return True

    def is_full(self):
        cnt = 0
        for i in range(0, self.cap+1):
            if self.heap[i] is not None:
                cnt += 1
        return cnt == self.cap

    def get_capacity(self):
        '''this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold'''
        return len(self.heap)-1

    def get_size(self):
        '''the actual number of elements in the heap, not the capacity'''
        cnt = 0
        for entry in self.heap:
            if entry is not None:
                cnt += 1
        return cnt

    def perc_down(self, i):
        '''where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        while True:
            if self.get_size() == 2 * i:
                l = 2 * i
            elif self.get_size() >= 2 * i + 1:
                if self.heap[2 * i] < self.heap[2 * i + 1]:
                    l = 2 * i + 1
                else:
                    l = 2 * i
            if self.get_size() < 2 * i:
                break
            if self.heap[i] < self.heap[l]:
                temp = self.heap[i]
                self.heap[i] = self.heap[l]
                self.heap[l] = temp
            else:
                break
            i = l

    def perc_up(self, i):
        '''where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes.'''
        parent_idx = i // 2
        while self.heap[parent_idx] is not None and self.heap[i] > self.heap[parent_idx]:
            temp = self.heap[parent_idx]
            self.heap[parent_idx] = self.heap[i]
            self.heap[i] = temp
            i = parent_idx
            parent_idx = i // 2

    def heap_sort_ascending(self, alist):
        '''perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order'''
        self.build_heap(alist)
        for i in range(len(alist)-1, -1, -1):
            alist[i] = self.dequeue()
