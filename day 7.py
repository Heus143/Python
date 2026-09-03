# ============================================================
# 1. add()
# ============================================================
# CONCEPT: add() adds a single hashable element to a set. Duplicates are ignored.

s = set()
s.add(1)              # Adds integer
s.add(1.6)            # Adds float
s.add(2+3j)           # Adds complex
s.add(True)           # Not added because True == 1
s.add(None)           # Adds None
# s.add([1,2,3])      # TypeError: unhashable type: 'list'
s.add((4,5,6))        # Tuple is hashable, so added
# s.add({7,8,9})      # TypeError: unhashable type: 'set'
# s.add({10:'a'})     # TypeError: unhashable type: 'dict'
s.add('rakesh')       # String is added as a single element
s.add(range(13,16))   # range object is added as a single element
print(s)              # Output: {1, 1.6, (2+3j), None, (4,5,6), 'rakesh', range(13, 16)} - order may vary

# ============================================================
# 2. update()
# ============================================================
# CONCEPT: update() iterates over an iterable and adds each element to the set.

s = set()
# s.update(1)         # TypeError: 'int' object is not iterable
s.update([1,2,3])     # List elements 1,2,3 added
s.update((4,5,6))     # Tuple elements 4,5,6 added
s.update({7,8,9})     # Set elements 7,8,9 added
s.update({10:'a', 11:'b', 12:'c'}) # Only dict keys 10,11,12 added
s.update('rakesh')    # String splits into characters 'r','a','k','e','s','h'
s.update(range(13,16))# range values 13,14,15 added
print(s)              # Output: {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'r','a','k','e','s','h'} - order random

# ============================================================
# 3. pop()
# ============================================================
# CONCEPT: pop() removes and returns a random element. Raises KeyError if set is empty.

s = {1,4,3,2,5,6,7,9}
print(s)              # Output: {1,2,3,4,5,6,7,9} - order may vary
a = s.pop() 
print(a, s)           # Output: 1 {2,3,4,5,6,7,9} - 1 removed
b = s.pop() 
print(b, s)           # Output: 2 {3,4,5,6,7,9} - 2 removed
# c = s.pop(3)        # Output: TypeError: pop() takes no arguments

# ============================================================
# 4. remove() and discard()
# ============================================================
# CONCEPT: Both remove a specific element. remove() raises KeyError if not found, discard() does not.

# remove
s = {4,3,2,5,8}
a = s.remove(8)       # Removes 8, returns None
print(a, s)           # Output: None {2,3,4,5}
# b = s.remove(9)     # Output: KeyError: 9

# discard
s = {4,3,2,5,8}
a = s.discard(8)      # Removes 8, returns None
print(a, s)           # Output: None {2,3,4,5}
b = s.discard(9)      # No error even if 9 not present
print(b, s)           # Output: None {2,3,4,5}

# ============================================================
# 5. clear()
# ============================================================
# CONCEPT: clear() removes all elements and makes the set empty.

s = {4,3,5,2,1}
a = s.clear()         # Clears set, returns None
print(a, s)           # Output: None set()

# ============================================================
# 6. union(), intersection(), difference(), symmetric_difference()
# ============================================================
# CONCEPT: Set operations that work with any iterable.

s = {1,2,3,4}
l = [3,4,5,6]
t = (3,4,5,6)
s2 = {3,4,5,6}
d = {3:'c', 4:'d', 5:'e', 6:'f'} # Keys are 3,4,5,6
r = range(3,7)
w = '3456'
print('Union:', s.union(l))                      # Output: Union: {1,2,3,4,5,6}
print('Intersection:', s.intersection(t))        # Output: Intersection: {3,4}
print('Difference:', s.difference(s2))           # Output: Difference: {1,2}
print('Symmetric Difference:', s.symmetric_difference(d)) # Output: Symmetric Difference: {1,2,5,6}
print('Union:', s.union(w))                      # Output: Union: {1,2,3,4,'3','4','5','6'} - str '3' is different from int 3
print('Union:', s.union(r))                      # Output: Union: {1,2,3,4,5,6}

# ============================================================
# 7. dict update()
# ============================================================
# CONCEPT: dict.update() adds key-value pairs from another dict or iterable of pairs.

d = {}
d.update({10:'j', 11:'k', 12:'l'})
print(d)                              # Output: {10: 'j', 11: 'k', 12: 'l'}
d.update([ [1,'a'], (2,'b'), 'ab' ])  # 'ab' is treated as ['a','b'] pair
print(d)                              # Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b'}
d.update(( 'ra', 'ke', 'sh' ))        # Each 2-char string is a key-value pair
print(d)                              # Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h'}
d.update({ (3,'c'), (4,'d') })        # Set of tuples, each tuple is a pair
print(d)                              # Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h', 3: 'c', 4: 'd'}

# ============================================================
# 8. pop() and popitem()
# ============================================================
# CONCEPT: pop(key) removes key and returns value. popitem() removes and returns last inserted pair.

d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.pop(2)
print(x)                              # Output: b
# y = d.pop(100)                      # Output: KeyError: 100
z = d.pop(100, -1)
print(z)                              # Output: -1 - default value

d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.popitem()
print(x, d)                           # Output: (4, 'd') {3: 'c', 2: 'b', 1: 'a'} - LIFO
y = d.popitem()
print(y, d)                           # Output: (1, 'a') {3: 'c', 2: 'b'}

# ============================================================
# 9. clear(), get(), setdefault()
# ============================================================
# CONCEPT: clear empties dict, get returns value without error, setdefault gets or inserts key with default.

d = {3:'c', 2:'b', 1:'a', 4:'d'} 
d.clear() 
print(d)                              # Output: {}

d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.get(2)
print(x, d)                           # Output: b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
y = d.get(100)
print(y, d)                           # Output: None {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
z = d.get(100, -1)
print(z, d)                           # Output: -1 {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

d = {3:'c', 2:'b', 1:'a', 4:'d'}
x = d.setdefault(2)
print(x, d)                           # Output: b {3: 'c', 2: 'b', 1: 'a', 4: 'd'} - key exists
y = d.setdefault(100)
print(y, d)                           # Output: None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None} - inserted with None
z = d.setdefault(90, -1)
print(z, d)                           # Output: -1 {... 90: -1} - inserted with -1
m = d.setdefault(90, -2)
print(m, d)                           # Output: -1 {... 90: -1} - already exists, -2 not added

# ============================================================
# 10. keys(), values(), items()
# ============================================================
# CONCEPT: Returns dynamic view objects of keys, values, and key-value pairs.

d = {3:'c', 2:'b', 1:'a', 4:'d'}
dk = d.keys()
print(dk, type(dk))                   # Output: dict_keys([3, 2, 1, 4]) <class 'dict_keys'>
dv = d.values()
print(dv, type(dv))                   # Output: dict_values(['c', 'b', 'a', 'd']) <class 'dict_values'>
di = d.items() 
print(di, type(di))                   # Output: dict_items([(3, 'c'), (2, 'b'), (1, 'a'), (4, 'd')]) <class 'dict_items'>