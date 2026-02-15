# 1. Write a Python program to create a tuple and display its elements using a loop.
def tuple_display():
    t = (10, 20, 30, 40)
    print("Tuple elements:")
    for i in t:
        print(i)


# 2. Write a program to count the number of elements in a tuple.
def tuple_count_elements():
    t = (10, 20, 30, 40)
    print("Number of elements:", len(t))


# 3. Write a program to find the sum of elements in a tuple.
def tuple_sum_elements():
    t = (10, 20, 30)
    total = 0
    for i in t:
        total += i
    print("Sum of elements:", total)


# 4. Write a program to check whether a given element exists in a tuple.
def tuple_check_element():
    t = (10, 20, 30, 40)
    x = 20
    if x in t:
        print("Element exists")
    else:
        print("Element does not exist")


# 5. Write a program to count even and odd numbers in a tuple.
def tuple_even_odd():
    t = (1, 2, 3, 4, 5)
    even = odd = 0
    for i in t:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even:", even)
    print("Odd:", odd)


# 6. Write a program to find the maximum and minimum element in a tuple.
def tuple_max_min():
    t = (10, 5, 30, 2)
    print("Maximum:", max(t))
    print("Minimum:", min(t))


# 7. Write a program to convert a tuple into a list.
def tuple_to_list():
    t = (1, 2, 3)
    l = list(t)
    print("List:", l)


# 8. Write a program to reverse a tuple using a loop.
def tuple_reverse():
    t = (1, 2, 3, 4)
    rev = ()
    for i in range(len(t)-1, -1, -1):
        rev += (t[i],)
    print("Reversed tuple:", rev)


# 9. Write a program to count occurrences of each element in a tuple.
def tuple_frequency():
    t = (1, 2, 2, 3, 1)
    freq = {}
    for i in t:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("Frequency:", freq)


# 10. Write a program to create a new tuple containing only positive numbers.
def tuple_positive_numbers():
    t = (10, -5, 20, -2)
    new = ()
    for i in t:
        if i > 0:
            new += (i,)
    print("Positive tuple:", new)


# 11. Write a program to demonstrate immutability of a tuple.
def tuple_immutability():
    t = (1, 2, 3)
    print("Tuple:", t)
    print("Tuple elements cannot be modified (immutable)")


# 12. Write a program to check whether a tuple is a palindrome.
def tuple_palindrome():
    t = (1, 2, 3, 2, 1)
    if t == t[::-1]:
        print("Tuple is Palindrome")
    else:
        print("Tuple is not Palindrome")


# 13. Write a program to extract elements at even positions from a tuple.
def tuple_even_positions():
    t = (10, 20, 30, 40, 50)
    new = ()
    for i in range(len(t)):
        if i % 2 == 0:
            new += (t[i],)
    print("Elements at even positions:", new)


# 14. Write a program to compare two tuples element-wise.
def tuple_compare():
    t1 = (1, 2, 3)
    t2 = (1, 4, 3)
    for i in range(len(t1)):
        print(t1[i] == t2[i])


# 15. Write a program to find common elements between two tuples.
def tuple_common_elements():
    t1 = (1, 2, 3, 4)
    t2 = (3, 4, 5, 6)
    common = ()
    for i in t1:
        if i in t2:
            common += (i,)
    print("Common elements:", common)
