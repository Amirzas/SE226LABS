
userNumber=int(input("Enter number of users:\n "))
users={}
for i in range(userNumber):
    username=input("Enter username: \n")
    itemNumber=int(input("Enter number of items:\n "))
    items=[]
    for i in range(itemNumber):
        item=input("item "+str(i+1)+"\n")
        items.append(item)
    users[username] = items
print("\nUSER DATA:")
for user, items in users.items():
 print(user+" -> "+str(items))

 all_items = []
for items in users.values():
     all_items.extend(items)
unique_set = set(all_items)
common_items = []
unique_items = []
for item in unique_set:
    if all_items.count(item) > 1:
        common_items.append(item)
    else:
        unique_items.append(item)
max_count = 0
most_popular = []

for item in unique_set:
    count = all_items.count(item)
    if count > max_count:
        max_count = count
        most_popular = [item]
    elif count == max_count:
        most_popular.append(item)
print("common items:")
for item in common_items:
    print(item)

print("unique items:")
for item in unique_items:
    print(item)

print("most popular item:")
for item in most_popular:
    print(item)