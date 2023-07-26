# CS331 Assignment 5, 03/12/2023

# In this assignment, you're asked to implement methods in several classes:
# 1. A Linked-Queue using a Singly LinkedList.
# 2. A Stack that's implemented using one or more Queues.
# 3. A Linked-Stack using a Singly LinkedList.
# You're also asked to implement a method valid_parentheses that uses Linked-Stack.

####################    DO NOT CHANGE THIS CLASS   ####################
class Node:
    # The Node class for a Singly LinkedList is implemented. Do not change anything in this class.

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)


# This is the class StackUsingQueue.
# You need to use Queue methods to simulate each method in a Stack.
class StackUsingQueue:
    # This is the class Queue, it is implemented using a Singly LinkedList.
    class Queue:
        # Please implement each of the following methods in class Queue following the guide.
        # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

        def __init__(self):
            # A new Queue contains two pointers head and tail both pointing to None.

            ####################    DO NOT CHANGE THIS   ####################
            self.head = self.tail = None

        def empty(self):
            # Return whether the Queue is empty or not.
            return self.head is None

        def enqueue(self, item):
            # Enqueue item to the tail of the Queue.
            # Note that, while enqueuing item to an empty Queue, both head and tail pointers need to be updated.
            # Do not return anything in the method.
            n = Node(item)
            if self.head is None:
                self.head = self.tail = n
            else:
                self.tail.next = n
                self.tail = n

        def dequeue(self):
            assert not self.empty()
            # Dequeue the item at the head of the Queue.
            # Note that, after dequeuing the last item, both head and tail pointers need to be updated.
            # Return the dequeued item.
            n = self.head
            self.head = n.next
            if self.head is None:
                self.tail = None
            return n.val

        def __iter__(self):
            # This implements "for item in Queue"
            # Yield each node from head to tail.
            # (We don't need to yield node.val since when implemented __repr__(Node) already.)
            n = self.head
            while n is not None:
                yield n
                n = n.next

        def __repr__(self):
            # This method implements "print(Queue)"

            ####################    DO NOT CHANGE THIS  ####################
            return "[" + ",".join(repr(n) for n in self) + "]"

    # Please implement each of the following methods in class StackUsingQueue following the guide.
    # Remind that, you may use ONLY Queue methods to implement each Stack method in this class.
    # Here, our design is that the "head" of self.data (which is a Queue) is the "top" of self (which is a Stack).
    # I've only implemented the construction method, peek(), and the dunder __repr__ method. Do not change them.

    def __init__(self):
        # A new StackUsingQueue contains a Queue as its data.

        ####################    DO NOT CHANGE THIS  ####################
        self.data = StackUsingQueue.Queue()

    def empty(self):
        # Return whether self.data is empty or not.
        return self.data.empty()

    def peek(self):
        # This implementation shows that we consider the "head" of self.data (which is a Queue)
        # as the "top" of self (which is a Stack).

        ####################    DO NOT CHANGE THIS  ####################
        assert not self.empty()
        return self.data.head

    def push(self, item):
        # Push item to the "top" of self (aka, the "head" of self.data).
        # Remind that, you may ONLY use methods in Queue class to implement this method.
        # Note that, we cannot insert item directly to the head of a queue.
        # Do not return anything in this method.
        q = StackUsingQueue.Queue()
        while not self.empty():
            temp1 = self.data.dequeue()
            q.enqueue(temp1)
        self.data.enqueue(item)
        while not q.empty():
            temp2 = q.dequeue()
            self.data.enqueue(temp2)

    def pop(self):
        assert not self.empty()
        # Pop out the "top" of self (aka, the "head" of self.data).
        # Remind that, you may ONLY use methods in Queue class to implement this method.
        # Note that, we can dequeue item directly from the head of a queue.
        # Return the popped out item.
        return self.data.dequeue()

    def __iter__(self):
        # This implements "for item in StackUsingQueue"
        # Yield each node from "top" to "bottom" of self (aka, head to tail of self.data).
        # (We don't need to yield node.val since when implemented __repr__(Node) already.)
        n = self.data.head
        while n is not None:
            yield n
            n = n.next

    def __repr__(self):
        # This method implements "print(StackUsingQueue)"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ",".join(repr(n) for n in self) + "]"


# This is the class Stack, it is implemented using a Singly LinkedList.
# We have implemented most of the methods in this class in Lecture 7.
class Stack:
    # Please implement each of the following methods in class Stack following the guide.
    # Here, I've only implemented the construction method and the dunder __repr__ method. Do not change them.

    def __init__(self):
        # A new Stack contains a pointer called "top" points to None.

        ####################    DO NOT CHANGE THIS  ####################
        self.top = None

    def empty(self):
        # Return whether Stack is empty or not
        return self.top is None

    def push(self, item):
        # Push item to the top of the Stack.
        n = Node(item, self.top)
        self.top = n

    def pop(self):
        assert not self.empty()
        # Pop out the top item from Stack.
        # Return the popped out item.
        item = self.top.val
        self.top = self.top.next
        return item

    def peek(self):
        assert not self.empty()
        # Return the item on the top of the Stack without popping it out.
        return self.top.val

    def __iter__(self):
        # This implements "for item in Stack"
        # Yield each node from "top" to "bottom" of the Stack.
        # (We don't need to yield node.val since when implemented __repr__(Node) already.)
        n = self.top
        while n is not None:
            yield n
            n = n.next

    def __repr__(self):
        # This implements "print Stack"

        ####################    DO NOT CHANGE THIS  ####################
        return "[" + ",".join(repr(n) for n in self) + "]"


# This is a question on LeetCode https://leetcode.com/problems/valid-parentheses/
# The input of this method is a string that contains "{}", "[]" and "()".
# Return whether the parentheses in the input string is valid or not.
# You should use Stack to solve this question.
def valid_parentheses(expr: str):
    st1 = Stack()
    st2 = Stack()
    st3 = Stack()
    for p in expr:
        if p == "{":
            st1.push("{")
        elif p == "[":
            st2.push("[")
        elif p == "(":
            st3.push("(")
        elif p == "}":
            if st1.empty():
                return False
            else:
                st1.pop()
        elif p == "]":
            if st2.empty():
                return False
            else:
                st2.pop()
        elif p == ")":
            if st3.empty():
                return False
            else:
                st3.pop()

    return st1.empty() and st2.empty() and st3.empty()


########################################################################################################################
######################################                                      ############################################
######################################     DO NOT CHANGE ANYTHING BELOW     ############################################
######################################                                      ############################################
########################################################################################################################
print("First, let's test whether the Linked Queue is correctly implemented.")
q1 = StackUsingQueue.Queue()
for x in range(6):
    q1.enqueue(x)
print("Let q1 be an empty Linked Queue. After enqueuing numbers 0 ~ 5 to q1, q1 =", q1, ".")

for _ in range(2):
    q1.dequeue()
print("After calling dequeue twice, then q1 =", q1, ".")

print("Then, let's test both Stack classes.")
s1 = StackUsingQueue()
for x in range(6):
    s1.push(x)
print("Let s1 be an empty Stack implemented with a Queue. After pushing numbers 0 ~ 5 to s1, s1 =", s1, ".")
s2 = Stack()
for x in range(6):
    s2.push(x)
print("Let s2 be an empty Linked Stack. After pushing numbers 0 ~ 5 to s2, s2 =", s2, ".")

for _ in range(2):
    s1.pop()
    s2.pop()
print("Pop out two elements from each Stack, then s1 =", s1, "; and s2 =", s2, ".")

print("In the end, let's test method \"valid_parentheses()\".")
str1 = "{[()](())(){}}{}[]"
print("Let string str1 = " + str1 + ", which is a series of valid parentheses. "
                                    "Our method returns", valid_parentheses(str1), ".")
str2 = "([])}"
print("Let string str2 = " + str2 + ", which is a series of invalid parentheses. "
                                    "Our method returns", valid_parentheses(str2), ".")
