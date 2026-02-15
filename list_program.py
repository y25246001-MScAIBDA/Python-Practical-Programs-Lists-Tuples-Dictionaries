"""
PYTHON PRACTICAL PROGRAMS
Lists (15) + Tuples (15) + Dictionaries (10)
Total = 40 Programs
"""

# =====================================================
# 🔵 LIST PROGRAMS
# =====================================================

# 1. Input n elements and display
def list_input_display():
    n = int(input("Enter number of elements: "))
    lst = []
    for i in range(n):
        lst.append(int(input("Enter element: ")))
    print("List:", lst)


# 2. Count even and odd
def list_even_odd(lst):
    even = odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even:", even, "Odd:", odd)


# 3. Sum of list
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    print("Sum:", total)


# 4. Largest and smallest
def list_max_min(lst):
    largest = smallest = lst[0]
    for i in lst:
        if i > largest:
            largest = i
        if i < smallest:
            smallest = i
    print("Largest:", largest, "Smallest:", smallest)


# 5. Count occurrence
def list_count(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    print("Count:", count)


# 6. Reverse list
def list_reverse(lst):
    rev = []
    for i in range(len(lst)-1, -1, -1):
        rev.append(lst[i])
    print("Reversed:", rev)


# 7. Separate positive & negative
def list_positive_negative(lst):
    pos = []
    neg = []
    for i in lst:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)
    print("Positive:", pos)
    print("Negative:", neg)


# 8. Remove duplicates
def list_remove_duplicates(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    print("Without duplicates:", unique)


# 9. Check sorted
def list_is_sorted(lst):
    flag = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            flag = False
            break
    print("Sorted" if flag else "Not Sorted")


# 10. Second largest
def list_second_largest(lst):
    largest = second = float('-inf')
    for i in lst:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i
    print("Second Largest:", second)


# 11. Merge two lists
def list_merge(l1, l2):
    merged = []
    for i in l1:
        merged.append(i)
    for i in l2:
        merged.append(i)
    print("Merged:", merged)


# 12. Common elements
def list_common(l1, l2):
    common = []
    for i in l1:
        if i in l2:
            common.append(i)
    print("Common:", common)


# 13. Rotate list
def list_rotate(lst, k):
    rotated = lst[k:] + lst[:k]
    print("Rotated:", rotated)


# 14. Frequency of elements
def list_frequency(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("Frequency:", freq)


# 15. Split even/odd index
def list_split_index(lst):
    even_index = []
    odd_index = []
    for i in range(len(lst)):
        if i % 2 == 0:
            even_index.append(lst[i])
        else:
            odd_index.append(lst[i])
    print("Even Index:", even_index)
    print("Odd Index:", odd_index)
# =====================================================
# END OF FILE
# =====================================================

