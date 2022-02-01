class TwoStack:
    # Creates two empty stacks stored in a single underlying list with length 2. List must never shrink below this size.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.under = self.stack1 + self.stack2
        self.underSize = 2

    def newList(self):
        n = self.underSize - len(self.stack1+self.stack2)
        between = [None] * n
        self.under = self.stack1 + between + self.stack2
        self.underSize = len(self.under)
        while len(self.under) < 2:
            self.under = self.under + [None]
            self.underSize = len(self.under)

    # Return the size of the underlying list, only used for testing.
    def capacity(self):
        return len(self.under)

    # Returns the number of elements in stack 1
    def size1(self):
        return len(self.stack1)

    # Returns the number of elements in stack 2
    def size2(self):
        return len(self.stack2)

    """
        Empties stack 1. If during this processing the total size occupied by both stacks decreases to ≤ half 
        the underlying list length, then the underlying list must shrink by factors of two until it is just big
        enough to accommodate both stacks. The remaining data needs to be copied into the smaller list correctly
        and then the smaller list should be the one the object references in the future (aka, the new list replaces
        the old list). This method does not return anything.
    """
    def clear1(self):
        self.stack1 = []
        self.under = self.stack1 + self.stack2
        self.underSize = len(self.under)
        power = self.nextPow()
        #print(power)
        self.underSize = 2**power
        self.newList()
    
    # Same as clear1, just on stack 2
    def clear2(self):
        self.stack2 = []
        self.under = self.stack1 + self.stack2
        self.underSize = len(self.under)
        power = self.nextPow()
        self.underSize = 2**power
        self.newList()

    def nextPow(self):
        count = 1
        while 2**count < self.underSize:
            count += 1
        return count

    """
        This method adds v to stack1. If the underlying list is full, then a new underlying list with
        twice the capacity must be allocated, the data from the old list is copied into the new list, and then the
        value specified is added. This method does not return anything.
    """
    def push1(self, v):
        if len(self.under) == len(self.stack1 + self.stack2):
            self.under = self.under + [None] * self.underSize
            self.underSize = len(self.under)
        self.stack1 = self.stack1 + [v]
        self.newList()
    

    # Same as push1, just on stack 2
    def push2(self, v):
        if len(self.under) == len(self.stack1 + self.stack2):
            self.under = self.under + [None] * len(self.under)
            self.underSize = len(self.under)
        self.stack2 = [v] + self.stack2
        self.newList()

    """
        This method removes an item from stack1 and returns it. If the stack is empty, then the pop
        method must throw an exception. After removing the item, if the utilized portion of both stacks decreases
        to ≤ half the underlying list length, then a new underlying list of half the size must be allocated and the
        data from the old list copied into the appropriate places in the new list and then replace the old list with
        the new list within the object. Note that an underlying list of size 2 is never shrunk (that is the minimum
        size).
    """
    def pop1(self):
        if self.stack1[-1] == None:
            #Throw exception if stack is empty
            pass
        val = self.stack1[-1]
        del self.stack1[-1]
        if len(self.under) / 2 >= len(self.stack1 + self.stack2):
            self.under = self.stack1 + self.stack2
            self.underSize = len(self.under)
            self.newList()
        return val
    
    # Same as pop1, but on 2
    def pop2(self):
        if self.stack2[0] == None:
            #Throw exception if stack is empty
            pass
        val = self.stack2[0]
        del self.stack2[0]
        if len(self.under) / 2 >= len(self.stack1 + self.stack2):
            self.under = self.stack1 + self.stack2
            self.underSize = len(self.under)
            self.newList()
        return val

    # Return top value on stack1, if empty, thow exception
    def top1(self):
        if self.stack1[-1] == None:
            #throw exception
            raise Exception("There is nothing here, move along!")
        return self.stack1[-1]

    # Same as top1, but on stack2
    def top2(self):
        if self.stack2[0] == None:
            #throw exception
            raise Exception("There is nothing here, move along!")
        return self.stack2[0]