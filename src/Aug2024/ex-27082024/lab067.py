my_shopping_list=["bread","milk","onion"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    #my_list.append("cheese")
    more_item=input("enter the item\n")
    my_list.insert(0,more_item)
    return my_list
l=bring_more_food(my_shopping_list)
print(l)
