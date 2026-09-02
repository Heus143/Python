# ============================================================
# 1. append()
# ============================================================

l = ['a', 'b', 'c']              # Creates a list

l.append(34)                     # Adds 34 as one element
l.append(34.3)                   # Adds 34.3 as one element
l.append(4+3j)                   # Adds complex number as one element
l.append(True)                   # Adds True as one element
l.append(None)                   # Adds None as one element
l.append([0,1,2])                # Adds the complete list as one element
l.append((3,4,5))                # Adds the complete tuple as one element
l.append({6,7,8})                # Adds the complete set as one element
l.append({9:'a', 10:'b', 11:'c'}) # Adds the complete dictionary as one element
l.append('rakesh')               # Adds the complete string as one element
l.append(range(12,15))           # Adds the range object as one element

print(l)                         # ['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3, 4, 5), {6, 7, 8}, {9: 'a', 10: 'b', 11: 'c'}, 'rakesh', range(12, 15)]


# ============================================================
# 2. extend()
# ============================================================

l = ['a', 'b', 'c']              # Creates a list

l.extend(34)                     # TypeError: int is not iterable
# Program stops here because extend() requires an iterable


# ============================================================
# 3. extend() - Correct examples
# ============================================================

l = ['a', 'b', 'c']              # Creates a list

l.extend([0,1,2])                # Adds each list element separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2]

l.extend((3,4,5))                # Adds each tuple element separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5]

l.extend({6,7,8})                # Adds set elements separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8]

l.extend({9:'a', 10:'b', 11:'c'}) # Adds dictionary keys separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

l.extend('rakesh')               # Adds each character separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'r', 'a', 'k', 'e', 's', 'h']

l.extend(range(12,15))           # Adds 12, 13, 14 separately
print(l)                         # ['a', 'b', 'c', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'r', 'a', 'k', 'e', 's', 'h', 12, 13, 14]


# ============================================================
# 4. insert() - positive index
# ============================================================

l = ['a', 'b', 'c', 'd']         # Creates a list

l.insert(2, 'hi')                # Inserts 'hi' at index 2
print(l)                         # ['a', 'b', 'hi', 'c', 'd']

l.insert(10, 'hi')               # Index 10 is outside the list, so adds at the end
print(l)                         # ['a', 'b', 'hi', 'c', 'd', 'hi']


# ============================================================
# 5. insert() - negative index
# ============================================================

l = ['a', 'b', 'c', 'd', 'e']    # Creates a list

l.insert(-2, 'hi')               # Inserts 'hi' before the element at index -2
print(l)                         # ['a', 'b', 'c', 'hi', 'd', 'e']

l.insert(-100, 'hi')             # Very small negative index, so adds at beginning
print(l)                         # ['hi', 'a', 'b', 'c', 'hi', 'd', 'e']


# ============================================================
# 6. pop()
# ============================================================

l = [1, 2, 3, 4, 5]              # Creates a list

a = l.pop()                      # Removes and returns the last element
print(a, l)                      # 5 [1, 2, 3, 4]

b = l.pop(2)                     # Removes and returns element at index 2
print(b, l)                      # 3 [1, 2, 4]

# c = l.pop(7)                   # Would give IndexError because index 7 doesn't exist

del l[0]                         # Deletes the element at index 0
print(l)                         # [2, 4]


# ============================================================
# 7. remove()
# ============================================================

l = [1, 2, 3, 4]                 # Creates a list

a = l.remove(3)                  # Removes the value 3; returns None
print(a, l)                      # None [1, 2, 4]

# print(l.remove(5))             # ValueError: list.remove(x): x not in list


# ============================================================
# 8. clear()
# ============================================================

l = [1, 2, 3, 4, 5]              # Creates a list

l.clear()                        # Removes all elements from the list
print(l)                         # []


# ============================================================
# 9. reverse()
# ============================================================

l = [1, 2, 3, 4, 5]              # Creates a list

print(id(l))                     # ID of the list object

a = l.reverse()                  # Reverses the list; returns None
print(a, l)                      # None [5, 4, 3, 2, 1]

print(id(l))                     # Same ID because reverse() changes the same list


# ============================================================
# 10. sort()
# ============================================================

l = [1,4,2,6,5,3]                # Creates an unsorted list

print(id(l))                     # ID of the list object

a = l.sort()                     # Sorts the list in ascending order; returns None
print(a, l)                      # None [1, 2, 3, 4, 5, 6]

print(id(l))                     # Same ID because sort() changes the same list


l = [50,10,40,20,30]             # Creates another list

print(l.sort(reverse=True))      # None
print(l)                         # [50, 40, 30, 20, 10]


# ============================================================
# 11. index()
# ============================================================

l = [1, 2, 1, 4, 6, 1, 7]        # Creates a list

print(l.index(1))                # 0
print(l.index(1, 3))             # 5

# print(l.index(1, 3, 5))        # ValueError: 1 is not found between index 3 and 5
# print(l.index(9))               # ValueError: 9 is not in list


# ============================================================
# 12. count()
# ============================================================

l = [1, 2, 1, 4, 1, 6, 7, 1]    # Creates a list

print(l.count(1))                # 4
print(l.count(9))                # 0


# ============================================================
# 13. tuple index()
# ============================================================

l = (1, 2, 1, 4, 6, 1, 7)       # Creates a tuple

print(l.index(1))                # 0
print(l.index(1, 3))             # 5

# print(l.index(1, 3, 5))        # ValueError: tuple.index(x): x not in tuple
# print(l.index(9))               # ValueError: tuple.index(x): x not in tuple


# ============================================================
# 14. tuple count()
# ============================================================

l = (1, 2, 1, 4, 1, 6, 7, 1)    # Creates a tuple

print(l.count(1))                # 4
print(l.count(9))                # 0