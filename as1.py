# Question 1: Palindrome Number
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    forward = x
    backward = 0
    while x > 0:
        backward = backward * 10 + x % 10
        x = x // 10
    return backward == forward


print("\nQuestion 1: Palindrome Number")
print(isPalindrome(0))
print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(2147447412))
print(isPalindrome(12345432))


# Question 2: Remove Duplicates from Sorted Array
def removeDuplicates(nums: list[int]) -> int:
    index = 1
    k = 1
    for i in range(0, len(nums)-1):
        if nums[i] != nums[i + 1]:
            k = k + 1
            nums[index] = nums[i + 1]
            index = index + 1

    for j in range(index, len(nums)):
        nums[j] = "_"
    print(nums)
    return k


print("\nQuestion 2: Remove Duplicates from Sorted Array")
print(removeDuplicates([0, 0, 0]))
print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([-5, -5, -3, -3, -1, -1]))
print(removeDuplicates([0, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 100]))
print(removeDuplicates(
    [-10, -10, -10, -10, -10, -10, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]))


# Question 3: Multiples of 3 or 5
def multiples(num):
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    return sum


print("\nQuestion 3: Multiples of 3 or 5")
print(multiples(5))
print(multiples(10))
print(multiples(500))
print(multiples(1000))
print(multiples(33))


# Question 4: Number of Words
def numberOfWords(str1: str):
    myComp = str1.split('\n')
    sortedVals = []
    for i in range(len(myComp)):
        current = myComp[i]
        temp = current.split(' ')
        for j in range(len(temp)):
            sortedVals.append(temp[j])
    return (len(sortedVals))


print("\nQuestion 4: Number of Words")
print(numberOfWords("It’s a closed-book-closed-notes exam."))
print(numberOfWords("""-How much money do you have?
-50 dollars."""))
print(numberOfWords("www.google.com is a website."))
print(numberOfWords("""Starting the Fall of 2021, the Academic Resource Center is
moving to in person tutoring for most subject areas. There are some online
tutoring sessions available for some subjects"""))
print(numberOfWords("Academic Calendar\nAcademic Programs- Graduate\nAcademic Programs- Undergraduate"))


# Question 5: ASCII Art
def pyramidArt(x: str):
    st = ""
    n = len(x)
    for i in range(n):
        half1 = x[n - 1 - i: n]
        half2 = x[n: n - i - 1: -1]
        half = half2 + half1
        half = ".".join(half)
        st += half.center(4 * n - 3, ".")
        if i != n - 1:
            st += "\n"

    st += "\n"

    for i in range(n - 1):
        half1 = x[i + 1: n]
        half2 = x[n - 1: i + 1: -1]
        half = half2 + half1
        half = ".".join(half)
        st += half.center(4 * n - 3, ".")
        if i != n - 1:
            st += "\n"
    return st


print("\nQuestion 5: ASCII Art")
print(pyramidArt('@'))
print(pyramidArt('@%'))
print(pyramidArt('ABC'))
print(pyramidArt('#####'))
print(pyramidArt('abcdefghijklmnop'))
print(pyramidArt('WXYZ'))

