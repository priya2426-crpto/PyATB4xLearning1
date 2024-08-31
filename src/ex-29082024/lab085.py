#set is collection of unique. use parathesis

list_of_uni_items={1,2,3,4,5,5}
print(list_of_uni_items)
print(set(list_of_uni_items))


set1={1,2,3,4,5,6}
set2={4,5,6,7,8}
my_set=set1.intersection(set2)
print(my_set)

my_set=set2.difference(set1)
print(my_set)