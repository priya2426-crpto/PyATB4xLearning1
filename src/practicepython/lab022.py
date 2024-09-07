numbers=[1,2,3,4,5,6]
num_search=input("number to search")
found=0
for i in range(len( numbers)):
    if num_search==numbers[i]:
        print("found at index:",i+1)
        found=1
if found==0:
    print("number not found")