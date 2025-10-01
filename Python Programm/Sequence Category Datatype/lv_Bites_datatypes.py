# Slicing  
L1=[2,4,"ABC",0]
L2=L1[1:3]   
print(L2)



# Indexing
l1 = [2, 4, 'ABC', 0]
print(l1[2])
l1[2] = 5
print(l1)
# Output: [2, 4, 5, 0]
print(type(l1))
# Output: <class 'list'>

l1 = [2, 4, 'ABC', 0]
l1[2] = 5
print(l1)  # Output: [2, 4, 5, 0]
print(type(l1))  # Output: <class 'list'>



L3=[2,4,5,0]
L4=bytes(l1)
print(L4, type(L4))  # Output: b'\x02\x04\x05\x00' <class 'bytes'>
try:
    L4[1]=3        # bytes are immutable 
except TypeError as L4:
    print(L4)  # Output: 'bytes' object does not support item assignment

