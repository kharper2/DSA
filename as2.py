# CS331 Assignment 2, 01/31/2023

class ArrayList:

    # Please implement each of the following methods. Here, I've only implemented the construction method.
    # You may assume that each item in the ArrayList is an integer for this assignment.

    # Consider self.data as an array instead of a list, so DO NOT use the build-in methods of a list,
    # such as self.data.append() or self.data.pop().

    # You may use only the following list/array methods:
    # 1. get the length of an array/list, for example: l = len(array)
    # 2. get the value at index i or values between indices i to j, for example: b = array[i], array1 = array[i:j]
    # 3. set value at index i or values between indices i to j, for example: array[i] = c, array [1:3] = [4,6]

    def __init__(self, n: int):
        # An ArrayList has two attributes:
        # 1. an array of with n slots
        # 2. an integer called "length" that represent the number of items in the ArrayList (initially it equals to 0)

        #############################       DO NOT CHANGE THIS       #################################
        self.data = [None] * n
        self.length = 0

    def __len__(self):
        # This implements len(ArrayList)
        # Return the number of items in the ArrayList.
        return self.length

    def isEmpty(self):
        # Return whether the size of the ArrayList is 0.
        return self.length == 0

    def isFull(self):
        # Return whether self.data is a full array.
        # This is a helper method called in append(.) and insert(.).
        return self.length == len(self.data)

    def doubleSize(self):
        # Create a new array and copy all items in self.data to the new array.
        # The new array has doubled length compared to self.data.
        # Assign the new array to be self.data.
        # This method is called in append(.) and insert(.) if self.data is full.
        # Do not return anything.
        nlen = len(self.data)*2
        narr = [None]*nlen
        for i in range(len(self.data)):
            narr[i] = self.data[i]
        self.data = narr

    def __contains__(self, item):
        # This implements "item in ArrayList"
        # Use a linear search algorithm to decide whether item is in self.data.
        # Return True if item is in self.data and return False otherwise.
        for i in range(len(self.data)):
            if self.data[i] == item:
                return True
        return False

    def index(self, item):
        # Assume that item is in the ArrayList, then use a linear search algorithm to find the index of item.
        # Return the index of item in self.data.
        for i in range(len(self.data)):
            if self.data[i] == item:
                return i

    def binarySearch(self, item):
        # Use a binary search algorithm to find the index of item in the SORTED self.data.
        # If the item is not in self.data, return -1.
        # Remind that, items are stored from index 0 to index self.length - 1.
        low = self.data[0]
        high = self.data[self.length - 1]
        while low < high:
            mid = (low + high)//2
            if item > self.data[mid]:
                low = mid + 1
            else:
                high = mid
        if self.data[high] == item:
            return high
        else:
            return -1

    def pop(self):
        # Remove and return the last item in ArrayList.
        # That item will be no longer in the ArrayList after pop().
        # Remind that, the length of the ArrayList will be reduced by 1 after pop().
        last = self.data[len(self.data) - 1]
        self.data[len(self.data) - 1] = [None]
        self.length = self.length - 1
        return last

    def pop_i(self, i):
        # Remove and return the item in an ArrayList at index i.
        # That item will be no longer in the ArrayList after pop_i().
        # Remind that, the size of the ArrayList will be reduced by 1 after pop_i();
        # and all items after index i need to be moved one spot to the left.
        val = self.data[i]
        for j in range (i, len(self.data)-1):
            self.data[j] = self.data[j+1]
        self.data[len(self.data)-1] = [None]
        self.length = self.length - 1
        return val

    def remove(self, item):
        # Assume that item is in the ArrayList.
        # Find the item and remove it from the ArrayList.
        # Do not return anything.
        # Remind that, the size of the ArrayList will be reduced by 1 after remove(.).
        for i in range(self.index(item), len(self.data) - 1):
            self.data[i] = self.data[i+1]
        self.data[len(self.data)-1] = None
        self.length = self.length - 1

    def max(self):
        # Return the item with maximum value in ArrayList.
        maximum = self.data[0]
        for i in range(1, self.length):
            if self.data[i] > maximum:
                maximum = self.data[i]
        return maximum

    def min(self):
        # Return the item with minimum value.
        minimum = self.data[0]
        for i in range(1, self.length):
            if self.data[i] < minimum:
                minimum = self.data[i]
        return minimum

    def append(self, item):
        # Append item to the next available spot in the ArrayList.
        # Remind that, check whether self.data is full first;
        # if it is full, call doubleSize() to enlarge it.
        # Remind that, the length of the ArrayList will be increased by 1 after append(.).
        # Do not return anything.
        if self.isFull():
            self.doubleSize()
        self.data[self.index(None)] = item
        self.length = self.length + 1

    def insert(self, i, item):
        # Insert item at index i, and you may assume that there are at least i-1 items in the ArrayList.
        # Move all items after index i one spot to the right before the insertion.
        # Remind that, you also need to check whether self.data is full first.
        # Remind that, the length of the ArrayList will be increased by 1 after insert(.).
        # Do not return anything.
        if self.isFull():
            self.doubleSize()
        for j in range(len(self.data)-1, i-1, -1):
            self.data[j] = self.data[j-1]
        self.data[i] = item
        self.length = self.length + 1

    def selectionSort(self):
        # Use selection sort algorithm to sort items in self.data.
        # Remind that, items are stored from index 0 to index self.size - 1.
        # Do not return anything.
        for i in range(self.length):
            key = self.data[i]
            spot = i
            for j in range(i+1, self.length):
                if self.data[j] < key:
                    key = self.data[j]
                    spot = j
            self.data[spot] = self.data[i]
            self.data[i] = key

    def bubbleSort(self):
        # Use bubble sort algorithm to sort items in self.data.
        # Remind that, items are stored from index 0 to index self.size - 1.
        # Do not return anything.
        for i in range(self.length-1):
            for j in range(self.length-1, i, -1):
                if self.data[j] < self.data[j-1]:
                    temp = self.data[j]
                    self.data[j] = self.data[j-1]
                    self.data[j-1] = temp

    def __iter__(self):
        # This implements "for item in ArrayList".
        # return an AL_iterator object as the iterator for ArrayList.
        # The iterator object should iterate on self.data, starts at index 0, end at index self.length
        iterator = self.AL_iterator(self.data, 0, self.length)
        return iterator

    class AL_iterator:
        # This is a helper class that's used to create ArrayList iterator object.
        # Here, I've only implemented the construction method.

        def __init__(self, list, start, end):
            # ArrayList iterator has four attributes:
            # 1. a list it iterates on
            # 2. starting index
            # 3. ending index
            # 4. a pointer that point the current location

            #############################       DO NOT CHANGE THIS       #################################
            self.list = list
            self.start = start
            self.end = end
            self.pointer = start

        def __next__(self):
            # If self.pointer is smaller than self.end, then return the item where the self.pointer points to
            # in self.data, then move self.pointer to the next spot.
            # Else, raise the StopIteration() exception
            if self.pointer < self.end:
                p = self.list[self.pointer]
                self.pointer += 1
                return p
            else:
                raise StopIteration


    def __repr__(self):
        # This implements "print(ArrayList)"

        #############################       DO NOT CHANGE THIS       #################################
        return "[" + ", ".join(str(item) for item in self)+ "]"

########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
print("We start with an empty testList with 4 available slots.")
testList = ArrayList(4)

print("Is the testList empty? The answer is", testList.isEmpty(), ".")

testList.append(10)
testList.append(4)
testList.append(5)
testList.append(9)
string1 = "After appending 4 items, the testList should be full now, and your result is "
if testList.isFull():
    string1 = string1 + "correct."
else:
    string1 = string1 + "wrong."
print(string1)

testList.append(8)
testList.append(2)
testList.append(3)
testList.append(1)
testList.append(6)
testList.append(7)
print("After appending another 6 items, "
      "there should be 10 items in the list now, and your result says", len(testList), ".")
print("The testList should have 16 slots in total at this moment, "
      "and your result says", len(testList.data), ".")
print("The array in testList is currently", testList.data, ".")

testList.remove(10)
testList.insert(2, 11)
print("After removing number 10 and inserting number 11 to the 3rd slot, "
      "the testList becomes" , testList, ".")

string2 = "The testList doesn't contain number 10 anymore, and your result is "
if 10 not in testList:
    string2 += "correct."
else:
    string2 += "wrong."
print(string2)

print("The maximum number in the list is", testList.max(), ", and the minimum is", testList.min(), ".")

testList1 = testList
testList.bubbleSort()
print("If we bubble sort the testList, we get", testList, ".")
print("Then, we can use binary search to find number 11 is at index", testList.binarySearch(11), ".")

testList1.selectionSort()
print("Now we rewind the sorting procedure "
      "and re-sort the testList using selection sort, we also get", testList, ".")

print("We pop out the item at the 4th slot, it is number",
      testList1.pop_i(3),"; the testList becomes", testList, ".")