my_list=[1,2,3]
#my_list_2=[1,true,priya]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[2])
#print(my_list[10])  #out of range

my_list[0]="priya"
print("element at the inex 0-",my_list[0])
print(my_list)
for element in my_list:
    print(element)

for i in range(1,10):#1,2,3,4,5,6,7,8,9
    print(i)
    print("___________________")
my_list.append(4)   # appen objectto the enof the list.
my_list.append(5)   #take only one argument,use multiple time
my_list.append(6)
print(my_list)

my_list.extend([7,8,9])
print(my_list)
my_list.insert(1,"saini")
print(my_list)

#how  i replace

my_list[1]="reyansh"
print(my_list)
my_list.insert(-1,"saini")
print(my_list)

my_list.remove("saini")
print(my_list)

my_copy_list=my_list_copy()
print(my_list)
print(my_copy_list()

my_copy_list.remove("priya")
my_copy_list.sort()
print(my_copy_list()

my_copy_list.sort(reverse=false)
print(my_copy_list)


my_list.clear()
print(my_list)
my_copy_list.reverse()
print(my_copy_list)