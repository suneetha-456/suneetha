#1st problem basic list operations
l = list(map(int,input("enter list elements:").split()))
print(l)

#2nd problem - list manipulation
l = list(map(int,input("enter list elements:").split()))
l.append(25)
print(l)
l.remove(25)
print(l)

#sum and average - 3rd problem
l = list(map(int,input("enter list elements:").split()))
sum = 0
avg = 0
for i in l:
    sum += i
avg = sum / len(l)
print("total sum is:",sum)
print("total avg is:",avg)

#reverse a list - 4th problem
l = list(map(int,input("enter list elements:").split()))
rev = l[::-1]
print(rev)

#every list item into square - 5
l = list(map(int,input("enter list elements:").split()))
new = []
for i in l:
    new.append(i*i)
print(new)

#max and min - 6
l = [12,5,27,69,11,43,25]
ma = 0
mi = float('inf')
for i in l:
    if i > ma:
        ma = i
print("maximum:",ma)
for i in l:
    if i < mi:
        mi = i
print("minimum:",mi)

#count occurrences - 7
l = [1,1,2,3,3,2,5,6,7,1,2,3]
freq = {}
for i in l:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#sort the list - 8
l = list(map(int,input("enter list elements:").split()))
l.sort()
print(l)


#copy of list - 9
l = list(map(int,input("enter list elements:").split()))
new = l.copy()
print("copy list:",new)

#combine two lists - 10
l1 = [1,2,3]
l2 = [4,5,6]
new = l1 + l2
print("combined list:",new)

#remove empty string from list of string - 11
l = ["abc", "","bcd","apple","banana","",""]
for i in l[:]:
    if i == "":
        l.remove(i)
print(l)

#remove duplicates - 12
l = [1,2,1,3,45,5,3,2,1,67,23]
dup = []
for i in l:
    if i not in dup:
        dup.append(i)
print(dup)

#remove all occurences - 13
l = list(map(int, input("Enter list elements: ").split()))
item = int(input("Enter item to remove: "))
for i in l[:]:  
    if i == item:
        l.remove(i)
print("Updated list:", l)

#list comprehension for numbers - 14
l = list(map(int, input("Enter list elements: ").split()))
even = []
for i in l:
    if i % 2 == 0:
        even.append(i)
print(even)

#access nested list - 15
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(l[0])  
print(l[1][2])     
print(l[2][0])   

#flatten the list - 16
l = [[1, 2], [3, 4], [5, 6]]
flatten = []
for i in l:
    for j in i:
        flatten.append(j)
print(flatten)

#concate two list index wise - 17
l1 = [1,2,3]
l2 = [4,5,6]
res = []
for i in range(len(l1)):
    res.append(l1[i] + l2[i])
print(res)

#or
l1 = [1,2,3]
l2 = [4,5,6]
res = []
for i in range(len(l1)):
    res.append(str(l1[i]) + str(l2[i]))
print(res)


#concatenate 2 lists in order - 18
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [i + j for i in list1 for j in list2]
print(res)


#iterate both list simultaneously - 19
list1 = [10, 20, 30]
list2 = [100, 200, 300]
for x, y in zip(list1, list2):
    print(x, y)

#add new items after specific item - 20
l1 = [10,20,30,40]
index = l1.index(20)
l1.insert(index + 1, 25)
print(l1)

#extend nested list with sublist - 21
list1 = ["a", ["b", "c"], "d"]
list1[1].extend(["e", "f"])
print(list1)

#replace lists items with new value - 22
l = [10,20,40,30,50]
for i in range(len(l)):
    if l[i] == 30:
        l[i] = 100
print(l)


#dictionaries
#basic operation - 1
d = {"a":1,"b":2}
for k,v in d.items():
    print(k,v)

#dictionary operations - 2
d = {"a":12,"b":3,"c":22}
d["d"] = 230
print(d)

#dictionary from list - 3
l1 = ["a","b","c"]
l2 = [1,2,3]
d = dict(zip(l1,l2))
print(d)

#clear dictionary - 4
d = {
    "a":1,
    "b":2,
    "c":3
}
d.clear()
print(d)

#merge two into one dict - 5
d1 = {
    "a":1,
    "b":2
}
d2 = {
    "c":3,
    "d":4
}
d1.update(d2)
print(d1)

#count character frequency - 6
s = "this is for demo purpose"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

#access nested dict - 7
d = {
    "a": 1,
    "b": {
        "b": 2,
        "c": 3
    }
}
print(d["b"]["b"])
print(d["b"]["c"]) 

#print value of key'history' from nested - 8
d = {
    "a":1,
    "b": {
        "history":23,
        "hii":178
    }
}
print("the value of key is:",d["b"]["history"])

#modify nested list - 9
d = {
    "a":1,
    "b":{
        "b":3,
        "c":4
    }
}
d["b"]["c"] = 290
print(d)

#initialize dict - 10
employees = ["Kelly", "Emma", "John"]
defaults = {"designation": "Developer", "salary": 8000}
res = {}
for emp in employees:
    res[emp] = defaults.copy()   
print(res)


#create dict  - 11
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
new_dict = {}
for k in keys:
    new_dict[k] = sample_dict[k]
print(new_dict)


#delete dict from list - 12
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys_to_remove = ["name", "salary"]
for k in keys_to_remove:
    if k in sample_dict:
        del sample_dict[k]
print(sample_dict)


#check is value exists - 13
d = {
    "a":1,
    "b":2,
    "c":3
}
check = 3
for v in d.values():
    if v == check:
        print("exist")
        break
else:
    print("not exist")

#rename key of a dict - 14
d = {
    "a":1,
    "b":2
}
d["c"] = d["a"]
del d["a"]
print(d)

#key of min value - 15
d = {
    "a":2,
    "b":34,
    "c":12,
    "d":1
}
mi = float('inf')
ke = None
for k,v in d.items():
    if v < mi:
        mi = v
        ke = k
print(ke)


#change value of key in nest dict - 16
d = {
    "a":1,
    "b":2,
    "c":{
        "c":3
    }
}
d["c"]["c"] = 25
print(d)


#invert dict - 17
d = {"a": 1, "b": 2, "c": 3}
inv = {}
for k, v in d.items():
    inv[v] = k
print(inv)


#sort dict by keys - 18
d = {"b": 2, "a": 1, "c": 3}
t = dict(sorted(d.items()))
print(t)


#sort dict by values - 19
d = {"a": 10, "b": 5, "c": 20}
c = dict(sorted(d.items(), key=lambda x: x[1]))
print(c)


#check if all values are unique - 20
d = {"a": 1, "b": 2, "c": 3}
values = list(d.values())
if len(values) == len(set(values)):
    print("unique")
else:
    print("not unique")

        


#tuples

#tuple repetation - 1
t = (1,2,3,4,5)
new = t * 3
print(new)

#basic tuple operations - 2
t = tuple(map(int,input("enter tuple:").split()))
print(t)

#slicing tuples - 3
t = (1,2,3,4,5)
print(t[::-2])

#reverse tuple - 4
t = (1,2,3,4,5,6)
rev = t[::-1]
print(rev)

#access nested tuples - 5
t = (1,2,3,(1,2,3),4,5)
print(t[3][2])

#create a tuple - 6
t = (50,)
print(t)

#unpack the tuple - 7
t = (1,2,3,4,5)
a,b,c,d,e = t
print(a)
print(b)
print(c)
print(d)
print(e)

#swap two tuples - 8
t1 = (1,2,3)
t2 = (4,5,6)
print("before swaping:")
print(t1)
print(t2)
t1, t2 = t2, t1
print("after swaping:")
print("t1:",t1)
print("t2:",t2)

#copy specific element - 9
t = (10, 20, 30, 40, 50)
new_tuple = t[1:4]
print("Original Tuple:", t)
print("Copied Elements:", new_tuple)

#list to tuple - 10
l = [1,2,3,4,5,6]
new = tuple(l)
print(new)


#function returning tuple - 11
def calculate(a, b):
    addition = a + b
    multiplication = a * b
    return addition, multiplication  # returns a tuple
result = calculate(3, 4)
print("Returned Tuple:", result)
print("Addition:", result[0])
print("Multiplication:", result[1])

#comapring tuples - 12
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print("tuple1 == tuple2:", tuple1 == tuple2)
print("tuple1 < tuple2:", tuple1 < tuple2)
print("tuple1 > tuple2:", tuple1 > tuple2)


#removing duplicates - 13
t = (1, 2, 2, 3, 4, 4, 5)
uni = tuple(set(t))
print("Original:", t)
print("Without duplicates:", uni)

#map tuples - 14
my_tuple = (1, 2, 3, 4)
squared = tuple(map(lambda x: x**2, my_tuple))
print("Original:", my_tuple)
print("Squared:", squared)

#modify tuple - 15
t = (10, 20, 30)
temp = list(t)
temp[1] = 99
t = tuple(temp)
print("Modified tuple:", t)

#sort a tuple - 16
t = ((1, 5), (2, 3), (4, 1), (3, 4))
s = tuple(sorted(t, key=lambda x: x[1]))
print("Sorted tuple:", s)

#count elements - 18
t = (1, 2, 3, 2, 4, 2)
count = t.count(2)
print("Count of 2:", count)


#filter tuples - 19
t = (10, 55, 23, 78, 40)
filtered = tuple(x for x in t if x > 50)
print("Filtered Tuple:", filtered)


#set

#basic set operation - 1
s = {1,2,3,4,1,3,4}
print(s)

#union of sets - 2
s1 = {1,2,3,4}
s2 = {4,3,5,6}
print(s1.union(s2))


#intersection of set - 3
s1 = {1,2,32,4}
s2 = {4,2,7,66}
print(s1.intersection(s2))

#difference of sets - 4
s1 = {1,2,32,4}
s2 = {4,2,7,66}
print(s1.difference(s2))
print(s2.difference(s1))


#symmetric difference - 5
s1 = {1,2,32,4}
s2 = {4,2,7,66}
print(s1.symmetric_difference(s2))

#add a list of elements to a set - 6
l = [1,2,3,41,2,3,1,5,4]
new = set(l)
print(new)


#set difference update - 7
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 7}
s1.difference_update(s2)
print(s1)

#remove items from set - 8
s = {1, 2, 3, 4, 5}
remove = {2, 4, 6}
s.difference_update(remove)
print(s)

#check subset - 9
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2))

#check superset - 10
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issuperset(s2))

#set intersection check - 11
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.isdisjoint(s2))

#set symmetric check - 12
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s1.symmetric_difference_update(s2)
print(s1)


#set intersection update - 13
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
s1.intersection_update(s2)
print(s1)

#find common in two lists - 14
l1 = [1,2,3,4]
l2 = [2,3,5,6]
common = []
for i  in l1:
    if i in l2:
        common.append(i)
print(common)
    
#or
l1 = [1, 2, 3, 4]
l2 = [2, 3, 5, 6]
common = list(set(l1) & set(l2))
print(common)

#count unique words - 15
s = "there is is an elephant in the zoo which is the very very big in the size"
word = s.split()
unique = set(word)
print(len(unique))


#frozen set - 16
fs = frozenset([1, 2, 3, 4, 2])
print(fs)
