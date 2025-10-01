# Pattern 1
# *
# **
# ***
# ****
# *****

print("Pattern 1", "\n")

for i in range(1, 6):
    print("* " * i)

# Pattern 2
#     *
#    ***
#   *****
#  *******
# *********

print("\nPattern 2", "\n")

for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)

# Pattern 3
#     *
#    **
#   ***
#  ****
# *****

print("\nPattern 3", "\n")

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

# Pattern 4
# *******
#  *****
#   ***
#    *

print("\nPattern 4", "\n")

for i in range(4):
    print(" " * i + "*" * (7 - 2 * i))
