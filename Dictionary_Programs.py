# 1. Write a Python program to create a dictionary of n students and their marks
#   and count the number of students whose marks are greater than or equal to 40.
def dict_students_pass():
    students = {"Aman": 45, "Riya": 38, "John": 60, "Neha": 42}
    count = 0
    for name in students:
        if students[name] >= 40:
            count += 1
    print("Number of students passed:", count)


# 2. Write a program to display all keys and values of a dictionary using a loop.
def dict_display_keys_values():
    d = {"a": 10, "b": 20, "c": 30}
    print("Keys and Values:")
    for key, value in d.items():
        print(key, ":", value)


# 3. Write a program to check whether a given key exists in a dictionary.
def dict_check_key():
    d = {"name": "Aman", "age": 20}
    key = "age"
    if key in d:
        print("Key exists in dictionary")
    else:
        print("Key does not exist")


# 4. Write a program to count the total number of key-value pairs in a dictionary.
def dict_count_pairs():
    d = {"x": 1, "y": 2, "z": 3}
    print("Total key-value pairs:", len(d))


# 5. Write a program to delete a key from a dictionary after checking its existence.
def dict_delete_key():
    d = {"a": 1, "b": 2, "c": 3}
    key = "b"
    if key in d:
        del d[key]
        print("Key deleted")
    else:
        print("Key not found")
    print("Dictionary:", d)


# 6. Write a program to separate keys and values into two lists.
def dict_separate_keys_values():
    d = {"a": 10, "b": 20, "c": 30}
    keys = []
    values = []
    for k, v in d.items():
        keys.append(k)
        values.append(v)
    print("Keys list:", keys)
    print("Values list:", values)


# 7. Write a program to create a dictionary of numbers and their squares.
def dict_numbers_squares():
    n = 5
    squares = {}
    for i in range(1, n + 1):
        squares[i] = i * i
    print("Dictionary of squares:", squares)


# 8. Write a program to find the key with the maximum value in a dictionary.
def dict_max_value_key():
    d = {"A": 50, "B": 70, "C": 60}
    max_key = max(d, key=d.get)
    print("Key with maximum value:", max_key)


# 9. Write a program to merge two dictionaries.
def dict_merge_two():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    d1.update(d2)
    print("Merged dictionary:", d1)


# 10. Write a program to sort a dictionary based on values using loops.
def dict_sort_by_values():
    d = {"a": 30, "b": 10, "c": 20}
    sorted_dict = {}
    for key in sorted(d, key=d.get):
        sorted_dict[key] = d[key]
    print("Dictionary sorted by values:", sorted_dict)
  
