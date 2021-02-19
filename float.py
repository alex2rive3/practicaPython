price=input("write price of the product in euros with 2 decimals: ")
print(price[:price.find('.')], 'euros and', price[price.find('.')+1:], 'cent.')
input()