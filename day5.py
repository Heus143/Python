# ============================================================
# 1. strip(), lstrip(), rstrip()
# ============================================================

a = ' ---python---   '              # String 

b = a.strip()                       # Removes spaces from both left and right sides
c = a.lstrip()                      # Removes spaces only from the left side
d = a.rstrip()                      # Removes spaces only from the right side

print(a, len(a))                    #  ---python---    12
print(b, len(b))                    # ---python--- 6
print(c, len(c))                    # ---python---    9
print(d, len(d))                    #  ---python--- 9


# ============================================================
# 2. replace()
# ============================================================

a = 'python is simple, python is easy to learn, python is all rounder'  # Original string

b = a.replace('python', 'java')     # Replaces every 'python' with 'java'

print(a)                            # python is simple, python is easy to learn, python is all rounder
print(b)                            # java is simple, java is easy to learn, java is all rounder


# ============================================================
# 3. lower(), upper(), swapcase(), title(), capitalize()
# ============================================================

a = 'PYTHON is simple, PYTHON is easy to LEARN'   # Original string

b = a.lower()                    # Converts all letters to lowercase
c = a.upper()                    # Converts all letters to uppercase
d = a.swapcase()                 # Converts uppercase to lowercase and lowercase to uppercase
e = a.title()                    # Makes the first letter of every word uppercase
f = a.capitalize()               # Makes only the first character of the whole string uppercase

print('original', a)             # original PYTHON is simple, PYTHON is easy to LEARN
print('lower:', b)               # lower: python is simple, python is easy to learn
print('upper:', c)               # upper: PYTHON IS SIMPLE, PYTHON IS EASY TO LEARN
print('swapcase:', d)            # swapcase: python IS SIMPLE, python IS EASY TO learn
print('title:', e)               # title: Python Is Simple, Python Is Easy To Learn
print('capitalize:', f)          # capitalize: Python is simple, python is easy to learn


# ============================================================
# 4. count(), startswith(), endswith()
# ============================================================

s = 'python is python'           # Creates a string

print(s.count('th'))             # 2
print(s.startswith('py'))        # True
print(s.endswith('onn'))         # False


# ============================================================
# 5. find() and index()
# ============================================================

#      0123456789
s = 'abdcdefdgh'                 # Creates string with index positions

print(s.find('d'))               # 2
print(s.find('d', 5))            # 7
print(s.find('d', 5, 7))         # -1

print(s.index('d'))              # 2
print(s.index('d', 5))           # 7
print(s.index('d', 5, 7))        # ValueError: substring not found

print()                          # blank line
print()                          # blank line


# ============================================================
# 6. rfind() and rindex()
# ============================================================

#      0123456789
s = 'abdcddddgh'                 # Creates string with multiple 'd' characters

print(s.rfind('d'))              # 7
print(s.rfind('z'))              # -1
print(s.rfind('d', 5))           # 7
print(s.rfind('d', 5, 7))        # 6

print(s.rindex('d'))             # 7
# print(s.rindex('z'))           # ValueError: substring not found
print(s.rindex('d', 5))          # 7
print(s.rindex('d', 5, 7))       # 6

print()                          # blank line
print()                          # blank line


# ============================================================
# 7. isalpha()
# ============================================================

a = 'aBcD'                       # Contains only alphabet characters
b = 'abc1'                       # Contains alphabets and a number
c = ''                           # Empty string

print(a.isalpha())               # True
print(b.isalpha())               # False
print(c.isalpha())               # False

print()                          # blank line
print()                          # blank line


# ============================================================
# 8. isdigit()
# ============================================================

a = '123'                        # Contains only digits
b = '12.3'                       # Contains digits and a decimal point
c = '-123'                       # Contains digits and a minus sign

print(a.isdigit())               # True
print(b.isdigit())               # False
print(c.isdigit())               # False

print()                          # blank line
print()                          # blank line


# ============================================================
# 9. isalnum()
# ============================================================

a = 'Abc123'                     # Contains alphabets and numbers
b = 'Abc@123'                    # Contains alphabets, numbers and special character
c = ' '                          # Contains only a space

print(a.isalnum())               # True
print(b.isalnum())               # False
print(c.isalnum())               # False

print()                          # blank line
print()                          # blank line


# ============================================================
# 10. isupper()
# ============================================================

a = 'ABC@123'                    # Contains uppercase letters, special character and numbers
b = '123'                        # Contains no alphabet characters
c = 'ABC123a'                    # Contains uppercase and lowercase letters

print(a.isupper())               # True
print(b.isupper())               # False
print(c.isupper())               # False

print()                          # blank line
print()                          # blank line


# ============================================================
# 11. islower()
# ============================================================

a = 'abc@123'                    # Contains lowercase letters, special character and numbers
b = '123'                        # Contains no alphabet characters
c = 'abc123A'                    # Contains lowercase and uppercase letters

print(a.islower())               # True
print(b.islower())               # False
print(c.islower())               # False


# ============================================================
# 12. split()
# ============================================================

s = 'abaca'                      # Creates a string

print(s.split('a'))              # ['', 'b', 'c', '']

s = '   '                        # String contains only spaces

print(s.split(' '))              # ['', '', '', '']
print(s.split())                 # []


# ============================================================
# 13. join()
# ============================================================

a = [1, 2, 3, 4]                 # List contains integers
b = ['1', '2', '3']              # List contains strings

print('@'.join(a))               # TypeError: sequence item 0: expected str instance, int found
print('@'.join(b))               # 1@2@3