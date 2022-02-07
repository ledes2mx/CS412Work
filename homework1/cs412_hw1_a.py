class TwoStack:
    # Creates two empty stacks stored in a single underlying list with length 2. List must never shrink below this size.
    def __init__(self):
        self.stack1 = 0
        self.stack2 = 0
        self.under = [None] * 2
        self.underSize = 2

    # Return the size of the underlying list, only used for testing.
    def capacity(self):
        return self.underSize

    # Returns the number of elements in stack 1
    def size1(self):
        return self.stack1

    # Returns the number of elements in stack 2
    def size2(self):
        return self.stack2

    """
        Empties stack 1. If during this processing the total size occupied by both stacks decreases to ≤ half 
        the underlying list length, then the underlying list must shrink by factors of two until it is just big
        enough to accommodate both stacks. The remaining data needs to be copied into the smaller list correctly
        and then the smaller list should be the one the object references in the future (aka, the new list replaces
        the old list). This method does not return anything.
    """
    def clear1(self):
        #self.stack1 = []
        
        self.underSize = self.stack2
        power = self.nextPow()
        self.underSize = 2**power
        temp = [None]*self.underSize
        for i in range(self.underSize):
            temp[-(i+1)] = self.under[-(i+1)]
        self.stack1 = 0
        self.under = temp
        self.underSize = len(self.under)
    
    # Same as clear1, just on stack 2
    def clear2(self):
        #self.stack2 = []
        
        self.underSize = self.stack1
        power = self.nextPow()
        self.underSize = 2**power
        temp = [None]*self.underSize
        for i in range(self.underSize):
            temp[i] = self.under[i]
        self.stack2 = 0
        self.under = temp
        self.underSize = len(self.under)

    def nextPow(self):
        count = 1
        while 2**count < self.underSize:
            count += 1
        return count

    def push1(self, v):
        if self.underSize == self.stack1 + self.stack2:
            self.doubled()
        self.under[self.stack1] = v
        self.stack1 += 1

    # Same as push1, just on stack 2
    def push2(self, v):
        if len(self.under) == self.stack1 + self.stack2:
            self.doubled()
        self.stack2 += 1
        self.under[-(self.stack2)] = v

    def doubled(self):
        self.underSize *= 2
        temp = [None]*self.underSize
        for i in range(self.stack1):
            temp[i] = self.under[i]
        for i in range(self.stack2):
            temp[-(i+1)] = self.under[-(i+1)]
        self.under = temp

    """
        This method removes an item from stack1 and returns it. If the stack is empty, then the pop
        method must throw an exception. After removing the item, if the utilized portion of both stacks decreases
        to ≤ half the underlying list length, then a new underlying list of half the size must be allocated and the
        data from the old list copied into the appropriate places in the new list and then replace the old list with
        the new list within the object. Note that an underlying list of size 2 is never shrunk (that is the minimum
        size).
    """
    def pop1(self):
        if self.under[0] == None:
            raise Exception("There is nothing here, move along!")
        self.stack1 -= 1
        popped = self.under[self.stack1]
        if self.underSize/2 == self.stack1 + self.stack2:
            self.halved()
        return popped
    
    # Same as pop1, but on 2
    def pop2(self):
        if self.under[-1] == None:
            raise Exception("There is nothing here, move along!")
        popped = self.under[-(self.stack2)]
        self.stack2 -= 1
        if self.underSize/2 >= self.stack1 + self.stack2:
            self.halved()
        return popped

    def halved(self):
        half = int(self.underSize/2)
        if half < 2:
            half = 2
        temp = [None]*half
        for i in range(self.stack1):
            temp[i] = self.under[i]
        for i in range(self.stack2):
            temp[-(i+1)] = self.under[-(i+1)]
        self.under = temp
        self.underSize = len(self.under)

    # Return top value on stack1, if empty, thow exception
    def top1(self):
        if self.under[0] == None:
            #throw exception
            raise Exception("There is nothing here, move along!")
        return self.stack1[-1]

    # Same as top1, but on stack2
    def top2(self):
        if self.under[-1] == None:
            #throw exception
            raise Exception("There is nothing here, move along!")
        return self.under[-(self.stack2)]