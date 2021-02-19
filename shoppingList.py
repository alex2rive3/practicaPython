shoppingList = input("write your shopping list separated by one (,)")
arrList = shoppingList.split(",")
print("your shopping list is: \n")
for x in range(0,len(arrList)):
    print(arrList[x],"\n")
input()