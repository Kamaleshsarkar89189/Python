# Python - Join Sets

# Join Python Sets Using "|" Operator


s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1|s2
print (s3)

# Join Python Sets Using union() Method

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = s1.union(s2)
print (s3)

# Join Python Sets Using update() Method

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.update(s2)
print (s1)

# Join Python Sets Using Unpacking Operator

s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3 = {*s1, *s2}
print (s3)

# Join Python Sets Using Set Comprehension

set1 = {1, 2, 3}
set2 = {3, 4, 5}

joined_set = {x for s in [set1, set2] for x in s}
print(joined_set) 